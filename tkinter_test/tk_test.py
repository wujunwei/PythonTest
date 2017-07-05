import csv
import json
import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import chardet

callable_arr = {'.csv': lambda x: read_csv(x), '.txt': lambda x: read_json(x), '.json': lambda x: read_json(x),
                '.xls': 'xls'}


def read_json(path_):
    with open(path_) as f:
        return json.load(f)


def read_csv(path_, is_header=False):
    encode = detect(path_)
    if is_header:
        print(123)
        csv_reader = csv.DictReader(open(path_, encoding=encode))
    else:
        print(34)
        csv_reader = csv.reader(open(path_, encoding=encode))
    return [row for row in csv_reader]


def detect(file_path):
    f = open(file_path, 'rb')
    data = f.readline()
    data += f.readline()
    return chardet.detect(data)["encoding"]


def dump(element, arr):
    if element == 'json':
        content = json.dumps(arr, sort_keys=True)
        with open('target.json', 'w+') as f:
            f.write(content)
            messagebox.askyesno('成功', '请在当前文件夹查找target.*文件')
    elif element == 'php':
        php_str = '<?php \n' \
                  'return '
        php_str = php_str + dump_php(arr) + ';'
        with open('target.php', 'w+') as f:
            f.write(php_str)
            messagebox.askyesno('成功', '请在当前文件夹查找target.*文件')


def dump_php(arr):
    php_str = ''
    if isinstance(arr, dict):  # 判断字典
        php_str += '[ '
        for k in arr.keys():
            php_str += '\n    \'%s\' => ' % k
            php_str += str(dump_php(arr[k])) + ','
        php_str += '\n]'
    elif isinstance(arr, bool):  # 判断bool型
        php_str += str(arr)
    elif str(arr).isdigit():
        php_str = str(float(arr))  # 判断数字
    elif isinstance(arr, list):
        php_str += '['
        for value in arr:
            php_str += '\n    ' + dump_php(value) + ','
        php_str += '\n]'
    elif isinstance(arr, str):
        php_str += '\'%s\'' % arr
    return php_str


def select_path():
    path_ = askopenfilename()
    path.set(path_)
    if path_ == '':
        return
    file_type = os.path.splitext(path_)[1]
    # print(file_type)
    call = callable_arr.get(file_type)
    try:
        global result_arr
        result_arr = call(path_)
        print(result_arr)
    except Exception as e:
        messagebox.askokcancel('error', str(e))
        return


result_arr = {}
root = Tk()
path = StringVar()
Label(root, text="默认导出到当前文件夹").grid(row=0, column=0)
Entry(root, textvariable=path).grid(row=0, column=1)
Button(root, text="路径选择", command=select_path).grid(row=0, column=2)
Button(root, text="导出json", command=lambda: dump('json', result_arr)).grid(row=1, column=0)
Button(root, text="导出php数组", command=lambda: dump('php', result_arr)).grid(row=1, column=2)

root.mainloop()
