#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
1.必须使用自定义函数，完成对函数程序的模块化
2.学生信息至少包含：姓名，年龄，学号，除此以外可以适当添加
3.必须完成的功能：添加，删除，修改，查询，退出

大体框架:

函数1
函数2
函数3
....

主体：
while Ture:
    if xxxx:
        pass
    elif xxxx:
        pass
    elif xxxx:
        pass
    else:
        报错程序
"""
import time


# 菜单程序
def menuInfo():
    print("------------menu-----------")
    print("|调用菜单信息------> 1      |")
    print("|添加学生信息------> 2      |")
    print("|删除学生信息------> 3      |")
    print("|查询学生信息------> 4      |")
    print("|打印学生信息------> 5      |")
    print("|修改学生信息------> 6      |")
    print("|退出学生信息管理系统-----> 7|")
    print("---------------------------")


# 添加学生信息
def addInfo(stuInfo):
    i = int(input("你想要输入几个学生的信息:"))
    k = 0
    while k < i:
        print("添加第%d个学生的信息====>" % (k + 1))
        name = input("请输入你要添加学生的名字:")
        age = int(input("请输入你要添加学生的年龄:"))
        stuNumber = int(input("请输入你要添加学生的学号:"))

        stuInfo[name] = str(age) + ',' + str(stuNumber)
        k += 1
    return stuInfo


# 删除学生信息
def delInfo(stuInfo):
    name = input("请输入你想删除学生的姓名:")
    # stuInfo[name].pop()
    if stuInfo.get(name, 0):
        del stuInfo[name]
        return stuInfo
    else:
        print("该数据库里面没有找到该学生，请核对正确后再输入!")


# 查询学生信息
def searchInfo(stuInfo):
    name = input("请输入你想查询学生的姓名:")
    # stuInfo[name].pop()
    tempNum = {}
    if stuInfo.get(name, 0):
        tempNum[name] = stuInfo[name]
        printInfo(tempNum)
    else:
        print("该数据库里面没有找到该学生，请核对正确后再输入!")


# 打印学生信息
def printInfo(stuInfo):
    i = 0
    for name, key in stuInfo.items():
        print("第%d学生的信息为：" % (i + 1))
        print("姓名为:%s" % name)
        print("年龄为:" + key[:key.find(',')])
        print("学号为:" + key[key.find(',') + 1:])
        i += 1
# print(stuInfo)


# 修改学生信息
def changeInfo(stuInfo):
    name = input("请输入你想修改学生的姓名:")
    # stuInfo[name].pop()
    if name in stuInfo.keys():
        del stuInfo[name]
        print("开始修改....")
        name = input("请输入你想修改后学生的姓名:")
        age = input("请输入要修改的年龄:")
        stuInfo[name] = age + ',' + input("请输入要修改的学号:")
        return stuInfo
    else:
        print("学生不存在！请重新查找!")


# 退出程序
def exitWorkPlace():
    print("程序正在退出，请稍后....")
    time.sleep(3)
    exit()


studentInfoDepot = {}  # 创建学生信息仓库
menuInfo()
# 选择功能
while True:
    choice = int(input("请输入您的选择:"))
    if choice == 1:
        menuInfo()
    elif choice == 2:
        temp = addInfo(studentInfoDepot)  # 导入学生信息
        studentInfoDepot = temp
    elif choice == 3:
        temp = delInfo(studentInfoDepot)  # 删除学生信息
        studentInfoDepot = temp
    elif choice == 4:
        searchInfo(studentInfoDepot)  # 对学生信息进行查询
    elif choice == 5:
        printInfo(studentInfoDepot)   # 打印学生信息
        time.sleep(2)  # 睡眠俩秒，方便查看
    elif choice == 6:
        temp = changeInfo(studentInfoDepot)  # 修改学生信息
        studentInfoDepot = temp
    elif choice == 7:
        exitWorkPlace()  # 退出学生管理系统
    else:
        print("输入错误，请核对正确后再输入!")
