# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:03:41 2019

@author: Josh
"""

import base64
f=open('channel_bonding_use.png','rb') #二进制方式打开图文件
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
print(ls_f)