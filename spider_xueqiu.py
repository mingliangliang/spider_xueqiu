# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:30:55 2017

@author: liang.ming
"""

import pymysql  
import urllib2 
import re  
  
def db( title,sign,slogan,detail):  
    #title=str(title)  
    #sign=str(sign)  
    #slogan=str(slogan)  
    #detail=str(detail)  
    
    # 获取数据库连接  
    conn = pymysql.connect(host='192.168.18.165', user='stock', password='111111', db='stock', port=3306, charset='utf8')  
    cur = conn.cursor()  # 获取一个游标  
    #sql = " INSERT INTO xueqiu_strategy ( f_title , f_sign , f_slogan , f_detail ) VALUES (%s,%s,%s,%s);"  
    print title,sign,slogan,detail,'\n本策略已保存至MySQL数据库'
    cur.execute(" REPLACE INTO xueqiu_strategy(f_title, f_sign, f_slogan, f_detail) VALUES(%s,%s,%s,%s)", (title, sign, slogan, detail))
    conn.commit()   
    cur.close()  # 释放游标  
    conn.close()  # 释放资源  
def str_jiequ(s):  
    b=''  
    for i in range(0,int(len(s)/8)):  
        a=str((bytes(r'\u'+s[(3+i*8):(7+i*8)],'ascii')).decode('unicode_escape'))  
        b=b+a  
    return b  
def getdb(url,i):  
        # 读取页面的原始信息并将其转码
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        req = urllib2.Request(url, headers = headers)
        myResponse = urllib2.urlopen(req)
        myPage = myResponse.read()
        unicodePage = myPage.decode("utf-8")
        #提取标题
        myMatch = re.search(r'<h3>(.*?)</h3>', unicodePage, re.S)
        title = u'暂无标题'
        if myMatch:
            title = myMatch.group(1)
        else:
            print u'爬虫报告：无法加载策略标题！'
        title = title.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','')
        #print title
        #标签
        myMatch = re.search(r'<div class="label">(.*?)</div><h3>', unicodePage, re.S)
        sign = u'暂无标签'
        if myMatch:
            sign = myMatch.group(1)
        else:
            print u'爬虫报告：无法加载策略标签！'
        sign = sign.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','')
        #print sign
        #slogan
        myMatch = re.search(r'</h3><p>(.*?)</p></div></div></div>', unicodePage, re.S)
        slogan = u'暂无slogan'
        if myMatch:
            slogan = myMatch.group(1)
        else:
            print u'爬虫报告：无法加载策略slogan！'
        slogan = slogan.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','')
        #print slogan
        #说明
        myMatch = re.search(r'<div class="card-bd">(.*?)</div></div><div class="stock-bar">', unicodePage, re.S)
        detail = u'暂无说明'
        if myMatch:
            detail = myMatch.group(1)
        else:
            print u'爬虫报告：无法加载策略说明！'
        detail = detail.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','')
        #print detail
        db(title,sign,slogan,detail)  
  
def geturl(start):  
    url='https://xueqiu.com/strategy/'  
    i=start  
    while i<70:  
        a="%d"%i  
        a=str(a)  
        url1=url+a  
        print(url1)  
        getdb(url1,i)
        i+=1  
    print u'爬虫报告：策略抓取完毕！'
geturl(1)