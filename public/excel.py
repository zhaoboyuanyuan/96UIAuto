# coding=utf-8
'''
Created on 2018年6月14日
@author: 赵永健   把excel中的数据读取为字典并使用，用于在Excel中保存控件库
'''
import xlrd
from copy import deepcopy


excel_path = 'D:\\code\\WebConLibr.xlsx'
dict = {}


# ID控件
def idCon(text):
    data = xlrd.open_workbook(excel_path)
    # table = data.sheets()[1]
    table = data.sheet_by_name('id')
    rows = table.nrows
    cols = table.ncols

    for i in range(0, rows):
        for j in range(cols):
            title = table.cell_value(i, 0)
            value = table.cell_value(i, 1)
            dict[title] = value
    return dict[text]


# xpath控件            
def xpathCon(text):
    data = xlrd.open_workbook(excel_path)
    # table = data.sheets()[2]
    table = data.sheet_by_name('xpath')
    # print(table)
    rows = table.nrows
    cols = table.ncols
    for i in range(0, rows):
        for j in range(cols):
            title = table.cell_value(i, 0)
            value = table.cell_value(i, 1)
            dict[title] = value
    return dict[text]


# className控件
def classNameCon(text):
    data = xlrd.open_workbook(excel_path)
    # table = data.sheets()[3]
    table = data.sheet_by_name('className')
    rows = table.nrows
    cols = table.ncols
    for i in range(0, rows):
        for j in range(cols):
            title = table.cell_value(i, 0)
            value = table.cell_value(i, 1)
            dict[title] = value
    return dict[text]

# 网站数据
def dataCon(text):
    data = xlrd.open_workbook(excel_path)
    table = data.sheet_by_name('webdata')
    rows = table.nrows
    cols = table.ncols
    for i in range(0, rows):
        for j in range(cols):
            title = table.cell_value(i, 0)
            value = table.cell_value(i, 1)
            dict[title] = value
    return dict[text]


# 处理testcase,获取数据与验证点
def case(caseId):
    data = xlrd.open_workbook(excel_path)
    fileName = 'testcase'
    table = data.sheet_by_name(fileName)
    value = table.row_values(caseId, 0, 10)
    list = []
    list.append(value[3])
    list.append(value[4])
    return list


def newSheet():
    data = xlrd.open_workbook(excel_path)
    fileName = 'Sheet2'
    table = data.sheet_by_name(fileName)
    rows = table.nrows
    cols = table.ncols
    dict = {}
    k = 0
    for i in range(1, rows):
        for j in range(2, cols):
            url = table.cell_value(i, 0)
            username = table.cell_value(i, 1)
            password = table.cell_value(i, 2)
            dict[k] = url + ',' + username + ',' + password
            k = k + 1
    return dict


def newSheet01():
    data = xlrd.open_workbook(excel_path)
    fileName = 'Sheet2'
    table = data.sheet_by_name(fileName)
    rows = table.nrows
    cols = table.ncols
    list = []
    for i in range(1, rows):
        for j in range(2, cols):
            url = table.cell_value(i, 0)
            username = table.cell_value(i, 1)
            password = table.cell_value(i, 2)
            list.append(url)
            list.append(username)
            list.append(password)

    # 大列表中几个数据组成一个小列表
    n = 3
    a = [list[i:i + n] for i in range(0, len(list), n)]
    return a


#逗号拆分字符串
def fejie(string):
    strlist = string.split(',')	# 用逗号分割str字符串，并保存到列表
    for value in strlist:	# 循环输出列表值
        print(value)



# print(xpathCon('workbench'))
