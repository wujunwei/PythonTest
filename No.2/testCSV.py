import csv

import chardet


def detect(path):
    f = open(path, 'rb')
    data = f.readline()
    data += f.readline()
    print(chardet.detect(data))


num = 0
detect(r'C:\Users\wjw33\Desktop\dl-item201611021026-1.csv')
exit()
csv_reader = csv.reader(open(r'C:\Users\wjw33\Desktop\dl-item201611021026-1.csv', encoding='cp932'))
# for row in csv_reader:
#     num += 1
print(num)
