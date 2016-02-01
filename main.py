#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from mail.Mail import Mail
# 扫描file文件夹下的文件， 然后判断日期
for parent,dirnames,filenames in os.walk('file'):
    print(filenames)

mail = Mail('youjingqiang@vip.qq.com','2016年01月01日 数据导入结果', '金融-电商-保险')
mail.send()
