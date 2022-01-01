#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time    :2021/12/28 16:38
# @Author   : 亮哥
# @Mail    : yxl20160@126.com
# @File      : youdaotranslation.py
# Software  : PyCharm

import time
import requests
import random
import hashlib


class YoudaoTranslation:
    def __init__(self):
        self.headers =  {
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'Referer': 'http://fanyi.youdao.com/',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-438638358@10.169.0.82; OUTFOX_SEARCH_USER_ID_NCOO=2005207257.8077083; JSESSIONID=aaaLkYJtA8nQUcSYDYH2x; ___rl__test__cookies=1639097704867'
    }
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    def get_parameter(self,word):
        data = {
            'i': '',
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': '',
            'sign': '',
            'lts': '',
            'bv': '',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        lts = str(int(time.time() * 1000))
        salt = lts + str(int(random.random() * 10))
        sign = 'fanyideskweb' + word + salt + 'Y2FYu%TNSbMCxc3t2u^XT'
        sign = hashlib.md5(sign.encode('utf-8')).hexdigest()
        bv = hashlib.md5(self.headers['User-Agent'].encode('utf-8')).hexdigest()
        data['i'] = word
        data['salt'] = salt
        data['sign'] = sign
        data['lts'] = lts
        data['bv'] = bv
        return data


    def main(self):
        queryWord = input("请输入你要查询的单词：")
        res = requests.post(self.url, headers=self.headers, data=self.get_parameter(queryWord))
        translateResult = res.json()['translateResult'][0][0]['tgt']
        print("结果为：",translateResult)

if __name__ == "__main__":
    yd = YoudaoTranslation()
    yd.main()

