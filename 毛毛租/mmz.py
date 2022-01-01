#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time    :2021/12/28 16:38
# @Author   : 亮哥
# @Mail    : yxl20160@126.com
# @File      : mmz.py
# Software  : PyCharm

import requests, execjs, time, json,re


with open("../js_database/maomaozu.js", "r", encoding="utf-8") as f:
    ctx = execjs.compile(f.read())

def encrypt(data,addr):
    result = json.dumps(data)
    # addr = ctx.call("addr","shanghai.maomaozu.com")
    result = ctx.call("aes_encrypt", result,addr)
    return result

def decrypt(response,addr):
    result = ctx.call("aes_decrypt", response,addr)
    return json.loads(result)

def get_data(page,url):
    # addr = "shanghai.maomaozu.com"
    addr_list = ['shanghai','beijing']
    addr = re.findall("//(.*?)/", url)[0].split(".")[0]
    if addr in addr_list:
        addr = addr+".maomaozu.com"
    sh_url = url #
    headers = {
        "Cookie": "Hm_lvt_6cd598ca665714ffcd8aca3aafc5e0dc=1639238334,1640598814,1640600669,1640656792; PHPSESSID=8pjg4crrbp52m8n7ppq7bj5i8v; Hm_lpvt_6cd598ca665714ffcd8aca3aafc5e0dc=1640671443; SECKEY_ABVK=tssG+gcHK+67DbH+Zy8QXbwXgl5velYFaCZ+4VIbISw%3D; BMAP_SECKEY=tssG+gcHK+67DbH+Zy8QXa1vfJeRfH0VO8sTwtTaXIreiwCwcO/JI36Utj6DdcBJ0ITIrryLT68ec15LcLf3ZOTX2EzR1GmMtUtd07c8qgX5MkGNwvtur/LHT7ui3BjwxjrjQKVfPcn4OYdemGkpPZlW6Ab6ZosuOjVfoMSHHfe7x/Ylgb497VwxkXwfNIc4",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    data = {
        "Type": "0",
        "page": 0,
        "expire": int(time.time() * 1000)
    }
    data['page'] = page
    data = encrypt(data,addr)
    print(data)
    res = requests.post(sh_url, headers=headers, data=data)
    result = decrypt(res.text,addr)
    print(result)
    # with open("maomaozu.json", 'w', encoding='utf-8') as f:
    #     f.write(json.dumps(result, ensure_ascii=False))
    #     f.flush()
def main():
    url_list = ["http://beijing.maomaozu.com/index/office.json",
                "http://shanghai.maomaozu.com/index/office.json"]

    for url in url_list:
        for page in range(1,2):
            get_data(page,url)
if __name__ == '__main__':
    main()






