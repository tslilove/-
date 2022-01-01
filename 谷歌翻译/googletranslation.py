#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time    :2021/12/29 10:45
# @Author   : 亮哥
# @Mail    : yxl20160@126.com
# @File      : 谷歌翻译爬虫.py
# Software  : PyCharm


import requests,re
from language_setting import setting

class GoogleTranslation:
    def __init__(self):
        self.headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        }
        self.url = "https://translate.google.cn/_/TranslateWebserverUi/data/batchexecute?rpcids=MkEWBc&f.sid=1891169464329671092&bl=boq_translate-webserver_20211220.12_p0&hl=zh-CN&soc-app=1&soc-platform=1&soc-device=1&_reqid=1172467&rt=c"
    def get_data(self,queryWord='我爱你', targetLanguage='en'):

        # 数据参数
        from_data = {
            "f.req": r"""[[["MkEWBc","[[\"{}\",\"auto\",\"{}\",true],[null]]",null,"generic"]]]""".\
                format(queryWord,targetLanguage)
        }
        try:
            res = requests.post(self.url, headers=self.headers, data=from_data, timeout=60)
            if res.status_code == 200:
                # 正则匹配结果
                # print(res.text)
                # response = re.findall(r',\[\[\\"(.*?)\\",\[\\', res.text)
                response = re.findall(r',\[\[\\"(.*?)\\",',res.text)
                if response:
                    response = response[1]
                else:
                    response = re.findall(r',\[\[\\"(.*?)\\"]', res.text)
                    if response:
                        response = response[0]
                return response
        except Exception as e:
            print(e)
            return False
    def main(self):
        print("*"*30)
        yuyan = \
        """
        '中文','日语','日语假名','泰语','法语','英语','西班牙语','韩语','土耳其语',
        '越南语','马来语','德语','俄语','伊朗语','阿拉伯语','爱沙尼亚语','白俄罗斯语',
        '保加利亚语','印地语','冰岛语','波兰语','波斯语','丹麦语','菲律宾语', '芬兰语',
        '荷兰语','加泰罗尼亚语','捷克语','克罗地亚语','拉脱维亚语','立陶宛语','罗马尼亚语',
        '南非语','挪威语','巴西语','葡萄牙语', '瑞典语','塞尔维亚语','世界语','斯洛伐克语',
        '斯洛文尼亚语','斯瓦希里语','乌克兰语','希伯来语','希腊语','匈牙利语','亚美尼亚语',
        '意大利语','印尼语','阿尔巴尼亚语','阿姆哈拉语','阿萨姆语','阿塞拜疆语','巴斯克语',
        '孟加拉语','波斯尼亚语','加利西亚语','格鲁吉亚语','古吉拉特语','豪萨语','伊博语',
        '因纽特语','爱尔兰语','祖鲁语','卡纳达语','哈萨克语','吉尔吉斯语','卢森堡语','马其顿语',
        '马耳他语','毛利语','马拉提语','尼泊尔语','奥利亚语','旁遮普语','凯楚亚语','塞茨瓦纳语',
        '僧加罗语','泰米尔语','塔塔尔语','泰卢固语','乌尔都语','乌兹别克语','威尔士语','约鲁巴语',
        '粤语','文言文','中文繁体'
        """
        print(yuyan)
        print("*" * 30)
        translateWord = input("请输入你要查询的句子或者单词：")  # "我爱你不是因为你是谁，而是我爱的人是谁"
        # 翻译各个国家语言
        language = input("请输入你要翻译的语言：")
        response = self.get_data(translateWord, setting(language))
        print(response)

if __name__ == '__main__':
    gl = GoogleTranslation()
    gl.main()
    # gl.get_data()





