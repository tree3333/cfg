#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import openpyxl
from openpyxl import load_workbook    # 用于操作Excel的模块
import yagmail   # 用于存储邮箱地址和密码的模块
import keyring   # 用于记录你邮箱地址和密码的模块
from datetime import *   # 用于获取当前系统时间的模块

# 加载Excel文件
wb = load_workbook("工资条群发.xlsx",data_only=True)#True会计算公式使结果而不是公式本身
sheet = wb.active

#登录邮箱配置
mailaddr = "31870495@qq.com"
password = "bapujgdgyvkzbhhb" 
yagmail.register(mailaddr,password)
pwd = keyring.get_password("yagmail",mailaddr)
yag = yagmail.SMTP(user=mailaddr,host="smtp.qq.com",password=pwd)

count = 0
table_header = "<thead>"
for row in sheet:
    count += 1
    if count == 1:
        for cell in row:
            if cell.column != "B":
                table_header += f"<th>{cell.value}</th>"
        table_header += "</thead>"
        continue
    else:
        row_text = ""
        for cell in row:
            if cell.column == "B":
                continue
            row_text += f"<td>{cell.value}</td>"
        row_text += "</tr>"
        name = row[2].value
        email = row[1].value
        #邮件正文
        contents = f"""
            <h3>亲爱的{name}:</h3>
            <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;感谢您在上一个月为微喵大家庭的辛苦付出，下面是您上一个月的工资条，如您对工资的核算方式及核发金额有任何的疑问，可直接与我们部门Ivy 白陈艳联系。
 
        行政人资部全体伙伴代表公司再次感谢您的努力工作， 祝您在接下来的日子里工作顺利！</p>
            <table border = "1px solid black">{table_header}{row_text}</table>
        """
        if email != None:
            yag.send(f"{email}",f"{date.today().year}-{date.today().month-1}月工资条",contents)
            print(f"[{count-1}]{name}的工资条发送完毕")
        else:
            count -= 1
print("共",count-1,"人工资条发送完毕")

