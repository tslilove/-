import requests
import execjs
import re

class BaiduTranslation:
    def __init__(self,query_word):
        self.url = 'https://fanyi.baidu.com/'
        self.post_url = 'https://fanyi.baidu.com/v2transapi'
        self.query_word =  query_word
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'origin': 'https://fanyi.baidu.com'
        }
        self.session = requests.session()

    def get_tokenAndsign(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        res = self.session.get(url=self.url,headers=headers)
        html_ = res.text  #res.content.decode()
        token = re.findall(r"token: '(.*?)',", html_)[0]
        # print(token,gtk)
        gtk = re.findall(r"window.gtk = '(.*?)';", html_)[0]
        with open('bdfy.js', 'r',encoding='utf-8') as f:
            ctx_js = f.read()
        ctx = execjs.compile(ctx_js)
        sign = ctx.call("sign_", self.query_word,gtk)
        return token,sign

    def get_data(self,token,sign,from_language,to_language):
        data = {
            'from': from_language,
            'to': to_language,
            'query': self.query_word,
            'transtype': 'translang',
            'simple_means_flag': '3',
            'sign': sign,
            'token': token,
            'domain': 'common'
        }

        return data

    #检验是否含有中文字符
    def is_contains_chinese(self):
        for _char in self.query_word:
            if '\u4e00' <= _char <= '\u9fa5':
                return 'zh','en'
        return 'en','zh'
    #
    def main(self):
        #我爱你不是因为你是谁，而是我爱的人是谁
        self.get_tokenAndsign()
        token,sign = self.get_tokenAndsign()
        from_language,to_language = self.is_contains_chinese()
        data = self.get_data(token,sign,from_language,to_language)
        # index_url = self.post_url
        res = self.session.post(self.post_url,headers = self.headers,data = data)
        trans_result = res.json()['trans_result']['data'][0]['dst']
        print("你查询的结果为：",trans_result)


if __name__ == '__main__':
    word = input("请输入你要查询的单词：")
    fy = BaiduTranslation(word)
    fy.main()
    # fy.get_tokenAndsign()
