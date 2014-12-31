#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Describe: 
Anthor: Aeesky
Version: 0.0.1
Date: 2014-12-04
Languag: Python2.7.8
Editor: Sublime Text3
"""
import os
import subprocess

# git remote -v
def giturl(dir):
	os.chdir(dir)
	cmd = "git remote -v"
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	url = p.stdout.readlines()[0].split(' ')[0]
	return str(url).rstrip()

#svn info
def svnurl(dir):
	os.chdir(dir)
	cmd = 'svn info | find "http"'
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	url = p.stdout.readlines()[0].replace('URL:','')
	return str(url).rstrip()
def svngit(dir):
	git = os.path.join(dir,".git");
	svn = os.path.join(dir,".svn")
	if os.path.exists(git):
		return giturl(dir)
	if os.path.exists(svn):
		return svnurl(dir)

def writeitem(dir):
	item =svngit(dir)
	if item and item.find('http')>0:
		item = '%-40s %2s' %(dir, item) 
		print item
		log = open('../svn-git.log', 'a+')
		log.write(item+'\r')
		log.close()
		pass

def logdir(dir):
	p =  os.listdir(dir);
	for x in p:
		sub =os.path.join(dir,x)
		if(os.path.isdir(sub)):
			writeitem(sub)
	print 'done!'
	pass

path = 'E:\CodeZone'
os.chdir(path)
logdir(path)

