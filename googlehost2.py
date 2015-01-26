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
from lxml import html
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
        nodes = tree.xpath("//*[@id='storybox']/div/div[4]",smart_strings=True)
        return nodes
        # return etree.tostring(nodes[0])
    except:  
        print("error to resolve the html ")  
    pass
def GetUpdateTime(text):
    try:  
        tree = etree.HTML(text)  
        nodes = tree.xpath("//*[@id='storybox']/div/p[2]/strong[2]",smart_strings=True)
        return etree.tostring(nodes[0])
    except:  
        print("error to resolve update time ")  
    pass
if __name__ == "__main__":
    text = gethtml(urlpath)
    # print GetUpdateTime(text)
    # Dom(text)
    items = GetHosts(text)
    datas =[]
    for onediv in items: 
        item = html.tostring(onediv,encoding="utf-8",method='text', pretty_print=False)
        if(item.count('.')>4):
            print item
            datas.insert(-1,item)
    print("backup hosts")
    shutil.copy(hosts, hostsBack)
    if os.path.exists(hosts):
        os.remove(hosts)
    print("update hosts")
    hostsFile = open(hosts, "a")
    for x in datas:
        hostsFile.write(x)
        pass
    # hostsFile.write(datas)
    hostsFile.close()
