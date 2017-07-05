from datetime import *
import time


def getWeekEndPrice(hour):
    if 9 <= hour < 12:
        return 40
    elif 12 <= hour < 18:
        return 50
    elif 18 <= hour < 22:
        return 60


def getWeekDayPrice(hour):
    if 9 <= hour < 12:
        return 30
    elif 12 <= hour < 18:
        return 50
    elif 18 <= hour < 20:
        return 80
    elif 20 <= hour < 22:
        return 60


def countField(M):
    T = M // 6
    X = M % 6
    result = {
        0: lambda x: 0 if x < 4 else 1,
        1: lambda x: 2,
        2: lambda x: 2 if x < 4 else 3,
        3: lambda x: 3 if x < 4 else 4,
    }
    if T > 3:
        return T
    else:
        return result[T](X)


def dealEachInput(str):
    day, hour, num = str.split(' ')
    fieldCount = countField(int(num))

    # 转换为星期几:
    timeArray = time.strptime(day, "%Y-%m-%d")
    week = time.strftime("%w", timeArray)
    startHour, endHour = hour.split('~')
    startHour = int(startHour.replace(':00', ''))
    endHour = int(endHour.replace(':00', ''))
    price = 0
    if int(week) > 4:  # 判断是否是周末
        while startHour < endHour:
            price += getWeekEndPrice(startHour)
            startHour += 1
    else:
        while startHour < endHour:
            price += getWeekDayPrice(startHour)
            startHour += 1
    inCome = num * 30
    outPut = price * fieldCount
    print(day+" "+hour, inCome, outPut, inCome - outPut)


def generateSummary(input_str):
    print("[summary]\n")
    for inp in input_str:
        dealEachInput(inp)


# 主循环
if __name__ == '__main__':
    input_arr = []
    while True:
        try:
            s = input()
            input_arr.append(s)
        except:  # 检测到文件尾 EOF 退出循输入
            break
    generateSummary(input_arr)
