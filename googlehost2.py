#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Describe: 自动更新host文件，用xpath处理网页内容
Anthor: Aeesky
Version: 0.0.1
Date: 2014-12-04
Languag: Python2.7.8
Editor: Sublime Text3
""" 

from HTMLParser import HTMLParser
import os
import shutil
import urllib
from lxml import etree
import re

__author__ = 'Aeesky'
 
urlpath = "http://www.360kb.com/kb/2_122.html"
hostsBack = "C:\Windows\System32\drivers\etc\hosts_back"
hosts = "C:\Windows\System32\drivers\etc\hosts"

# Fetch the target html  
def gethtml(url):  
    '''''
    获取网页正文
    '''  
    response = urllib.urlopen(url)  
    result = response.read()  
    return  result  
# end def gethtml  

def GetHosts(text):
    '''
    用xpath解析host内容
    '''
    try:  
        tree = etree.HTML(text)  
        nodes = tree.xpath("//*[@id='storybox']/div/p[7]",smart_strings=True)
        return etree.tostring(nodes[0])
    except:  
        print("error to resolve the html ")  
    pass

if __name__ == "__main__":
    text = gethtml(urlpath)
    # Dom(text)
    datas = GetHosts(text)
    # 格式替换
    datas = datas.replace('&#160;','').replace('<br/>','').replace('<p>','').replace('</p>','').replace('<span>','').replace('</span>','').strip()
    print datas
    print("backup hosts")
    shutil.copy(hosts, hostsBack)
    if os.path.exists(hosts):
        os.remove(hosts)
    print("update hosts")
    hostsFile = open(hosts, "a")
    hostsFile.write(datas)
    hostsFile.close()
