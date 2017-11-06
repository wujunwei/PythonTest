import csv
import json
import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import chardet
import xlrd

callable_arr = {'.csv': lambda x: read_csv(x), '.txt': lambda x: read_json(x), '.json': lambda x: read_json(x),
                '.xls': lambda x: read_excel(x), '.xlsx': lambda x: read_excel(x)}


def read_excel_for_key_pair(path_):
    data = xlrd.open_workbook(path_)
    table = data.sheets()[0]
    nrows = table.nrows  # 行数
    return_data = {}
    for i in range(0, nrows):
        rowvalue = table.row_values(i)
        key = str(rowvalue[0]).strip()
        if return_data.get(key, None) is None:
            return_data[key] = []
        return_data[key].append(rowvalue[1].strip())
    return return_data


def read_excel(path_):
    if kp.get():
        return read_excel_for_key_pair(path_)
    data = xlrd.open_workbook(path_)
    table = data.sheets()[0]
    nrows = table.nrows  # 行数
    return_data = []
    if is_header.get():
        title = table.row_values(0)
        for i in range(1, nrows):
            rowValues = table.row_values(i)  # 某一行数据
            return_data.append(dict(zip(title, rowValues)))
    else:
        for i in range(0, nrows):
            rowValues = table.row_values(i)  # 某一行数据
            return_data.append(rowValues)
    return return_data


def read_json(path_):
    with open(path_) as f:
        return json.load(f)


def read_csv(path_):
    # print(is_header.get())
    encode = detect(path_)
    if is_header.get():
        csv_reader = csv.DictReader(open(path_, encoding=encode))
    else:
        csv_reader = csv.reader(open(path_, encoding=encode))
    return [row for row in csv_reader]


def detect(file_path):
    f = open(file_path, 'rb')
    data = f.readline()
    data += f.readline()
    # print(data)
    return chardet.detect(data)["encoding"]


def dump(element):
    path_ = path.get()
    if path_ == '':
        return
    file_type = os.path.splitext(path_)[1]
    call = callable_arr.get(file_type)
    try:
        arr = call(path_)
    except Exception as e:
        print(e)
        messagebox.askokcancel('error', '不支持该文件类型')
        return
    if element == 'json':
        content = json.dumps(arr, sort_keys=True)

        with open(os.path.dirname(path_)+r'\target.json', 'w+') as f:
            f.write(content)
            messagebox.askyesno('成功', '转换成功！请查找target文件')
    elif element == 'php':
        php_str = '<?php \n' \
                  'return '
        php_str = php_str + dump_php(arr) + ';'
        with open(os.path.dirname(path_)+r'\target.php', 'wb') as f:
            f.write(php_str.encode())
            messagebox.askyesno('成功', '转换成功！请查找target文件')


def dump_php(arr, level=0):
    blank_str = '    ' * level
    php_str = ''
    if isinstance(arr, dict):  # 判断字典
        php_str += '[ '
        for k in arr.keys():
            php_str += '\n%s\'%s\' => ' % (blank_str + '    ', k.replace('\'', r'\''))
            php_str += dump_php(arr[k], level+1) + ','
        php_str += '\n%s]' % blank_str
    elif isinstance(arr, bool):  # 判断bool型
        php_str += str(arr)
    elif isinstance(arr, float) or isinstance(arr, int):
        php_str = str(float(arr))  # 判断数字
    elif isinstance(arr, list):  # 判断列表
        php_str += '['
        for value in arr:
            php_str += '\n%s' % (blank_str + '    ') + dump_php(value, level+1) + ','
        php_str += '\n%s]' % blank_str
    elif isinstance(arr, str):  # 判断字符串
        php_str += '\'%s\'' % arr.replace('\'', r'\'')
    return php_str


def select_path():
    path_ = askopenfilename()
    path.set(path_)


root = Tk()
root.title('文件转换器')
path = StringVar()
kp = BooleanVar()
is_header = BooleanVar()
is_header.set(False)
Label(root, text="是否使用表头(只针对excel文件)").grid(row=0, column=0, sticky=E, padx=0)
Checkbutton(root, variable=is_header).grid(row=0, column=1, sticky=W, padx=0)
Label(root, text="excel 两列键值对模式(只针对excel文件)").grid(row=0, column=2, sticky=E, padx=0)
Checkbutton(root, variable=kp).grid(row=0, column=3, sticky=W, padx=0)
Entry(root, textvariable=path, width=50).grid(row=1, column=0, sticky=W, padx=0)
Button(root, text="路径选择", command=select_path, width=10).grid(row=1, column=2, sticky=W, padx=0)
Button(root, text="导出json", command=lambda: dump('json')).grid(row=2, column=0, sticky=E, padx=0)
Button(root, text="导出php", command=lambda: dump('php')).grid(row=2, column=2, sticky=W, padx=0)

root.mainloop()
