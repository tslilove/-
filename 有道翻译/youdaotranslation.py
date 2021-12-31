#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time    :2022/1/1 2:02
# @Author   : 亮哥
# @Mail    : yxl20160@126.com
# @File      : 有道翻译js.py
# Software  : PyCharm

import requests,execjs

class YouDaoTranslationJs:
    def __init__(self):
        self.headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-438638358@10.169.0.82; OUTFOX_SEARCH_USER_ID_NCOO=2005207257.8077083; JSESSIONID=aaaaC4T3F99-15cILDr4x; ___rl__test__cookies=1640970491751',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'Referer': 'https://fanyi.youdao.com/'
        }
        self.url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    def get_parameter(self,word):
        with open('../js_database/ydfy.js','r',encoding='utf-8') as f:
            ctx_js = execjs.compile(f.read())
        # word = "我爱你"
        data_dict = ctx_js.call("get_param",word)
        data = {
            'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': data_dict['salt'],
            'sign': data_dict['sign'],
            'lts': data_dict['ts'],
            'bv': data_dict['bv'],
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        return data

    def main(self):
        queryWord = input("请输入你要查询的单词：")
        data = self.get_parameter(queryWord)
        res = requests.post(self.url, headers=self.headers, data=data)
        translateResult = res.json()['translateResult'][0][0]['tgt']
        print("结果为：", translateResult)


if __name__ == '__main__':
    yd = YouDaoTranslationJs()
    yd.main()
    # yd.get_parameter("我爱你")
