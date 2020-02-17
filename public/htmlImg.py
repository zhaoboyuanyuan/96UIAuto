# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2020/1/8 13:20
# -*- coding: utf-8 -*-
# 本地图片在html中显示

import os
import re
import base64

import time


def findimg(content):
    '''
    查找网页中所有的img,类似img src='1.png'，返回1.png
    :param content: 网页内容
    :return: 返回找到的所有图片文件名列表
    '''
    patt = re.compile("<img src='(.+)'") #正则表达式查找所有的img
    grp = re.findall(patt,content)
    # print(grp)
    return grp

def findcomment(content):
    '''
    查找注释，删除注释
    :param content: 网页源内容
    :return: 删除注释后的网页内容
    '''
    patt = re.compile('(<!--.+-->)')
    grp = re.findall(patt,content)
    # print(grp)
    for g in grp:
        content = content.replace(g,'')
    return content

def imgbase64(pic_path):
    '''
    实现图片的base64编码，返回编码字符串
    :param pic_path:
    :return:
    '''
    pic_basename = os.path.basename(pic_path)
    file_ext = pic_basename.split('.')[-1].lower()
    # print(file_ext)

    if file_ext == "jpg" :
        tag = "jpg"
    elif file_ext == "jpeg" :
        tag = "jpg"
    elif file_ext == "png" :
        tag = "png"
    elif file_ext == "bmp" :
        tag = "bmp"
    else:
        print("Unsupported image format !")
        return None

    with open(pic_path, "rb") as imageFile:
        str_pic = base64.b64encode(imageFile.read()).decode('ascii')
        # print(str_pic)

    str_begin = 'data:image/' + tag + ';base64,'
    result_str = str_begin + str_pic
    # print(result_str)
    return result_str

def readhtml():
    '''
    读取当前目录下的所有html文件，并查找本地图片，实现嵌入图片的base64编码
    :return: 无
    '''
    for file in os.listdir('./result'):
        if file.endswith(".html"):
            root = 'D:/code/SafetyappEducate/result/'
            with open(root+file,'r+',encoding='utf-8') as html:
                content = html.read()       # 读取html文件内容
                pics = findimg(content)     # 查找所有内容中的本地图片
                for pic in pics:
                    # log_path = os.path.join(os.getcwd(), 'result')
                    # if os.path.exists(pic):
                    picPath='D:/code/SafetyappEducate/save_img/'+pic[12:]
                    # print(picPath)
                    base64code = imgbase64(picPath)     # base64编码图片文件
                    content = content.replace(pic,base64code)   # 替换html文件内容

                content = findcomment(content)      # 去除html文件中的注释
                html.seek(0)
                html.write(content)                 # 覆写




# 打包生成可执行程序的命令
# pyinstaller --noupx -F -w --icon=mylogo.ico imgbase64.py
# if __name__ == '__main__':
#     readhtml()

