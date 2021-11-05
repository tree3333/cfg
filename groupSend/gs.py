#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import openpyxl
import yagmail    
from openpyxl import load_workbook    # 用于操作Excel的
from datetime import *  
import sys
class groupSend:
    def __init__(self):
        ###发送邮箱配置
        self.mailaddr = "liyao@lamic.cn"
        self.password = "cJuktXSCFk8vv3yy" 
        self.host = "smtp.exmail.qq.com"
        ###其他配置
        self.headlines = 3 #表头行数
        self.filename = "工资表.xlsx"
        ###全局变量
        self.headers = []#存放表头
        self.emails = []#有序存放email
        self.employees = {}#存放所有人的信息
        self.time_cost_str = ""
        self.start_time = datetime.now()
        ##邮件标题
        self.title = ""
    ##获取输入参数
    def get_argvs(self):
        if len(sys.argv) >= 2:
            self.filename = str(sys.argv[1])
    ##启动时调用一次
    def prepare(self):
        self.get_argvs()
        #生成邮件标题
        y = date.today().year
        m = date.today().month - 1
        if m == 0:
            m = 12
            y = y - 1
        self.title = f"{y}年{m}月工资条"
    ##结束时调用一次
    def final(self):
        sec_cost = datetime.now() - self.start_time
        self.time_cost_str = str(sec_cost) + "秒" 
        print("共",len(self.emails),"人工资条发送完毕！耗时",self.time_cost_str)
    ##解析excel
    def parse(self):
        # 加载Excel文件
        wb = load_workbook(self.filename,data_only=True)#True会计算公式使结果而不是公式本身
        sheet = wb.active
        count = 0
        for row in sheet:
            count += 1
            if count <= 2:#跳过标题两行
                continue
            elif count == self.headlines: ##标题
                for cell in row:
                    self.headers.append(cell.value)
            else: ##正文
                self.employees[row[1].value] = []
                self.emails.append(row[1].value)
                for cell in row:
                    self.employees[row[1].value].append(cell.value)
    ##发送邮件
    def send(self):
        yagmail.register(self.mailaddr,self.password)
        yag = yagmail.SMTP(user=self.mailaddr,host=self.host,password=self.password)
        for email in self.emails:
            contents = self.genContents(self.headers,self.employees[email])
            yag.send(email,self.title,contents)
            print(f"[{self.employees[email][0]}]{self.employees[email][3]}的工资条发送完毕")

    ##主程序
    def run(self):
        self.prepare()
        self.parse()
        self.send()
        self.final()
    ##生成邮件内容
    def genContents(self,headers,employee):
        ## 1是邮箱，只用于发送，不需要展示，只有市场部有8，9列，10-15列是扣款，用红色
        table_header = "<thead>"
        row_text = ""
        for i in range(len(headers)):
            if employee[i] == None:
                employee[i] = ""
            if i == 1:
                continue
            elif i>= 8 and i <= 9:
                if employee[2] == "市场" or employee[2] == "市场部":
                    table_header += f'<th width="380">{headers[i]}</th>' 
                    row_text += f'<td align="center"  width="380">{employee[i]}</td>'
            elif i>=10 and i <=15:
                table_header += f'<th width="380"><font color="red">{headers[i]}</font></th>'
                row_text += f'<td align="center" width="380"><font color="red">{employee[i]}</font></td>'
            else:
                table_header += f'<th width="380">{headers[i]}</th>'
                row_text += f'<td align="center" width="380">{employee[i]}</td>'
        table_header += "</thead>"
        row_text += "</tr>"
        contents = f'''
            <h3>亲爱的{employee[3]}:</h3>
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;感谢您在上一个月为微喵大家庭的辛苦付出，下面是您上一个月的工资条，如您对工资的核算方式及核发金额有任何的疑问，可直接与我们部门Ivy 白陈艳联系。
 
            行政人资部全体伙伴代表公司再次感谢您的努力工作， 祝您在接下来的日子里工作顺利！</p>
            <table border="1px solid" cellspacing="0">{table_header}{row_text}</table>
        '''
        return contents
###
s1 = groupSend()
s1.run()
