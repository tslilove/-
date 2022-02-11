#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import execjs
import requests
import pandas as pd

result_url = "https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/drug/searchDrug"
UA = 你的ua

with open('../js_database/nhsa.js', 'r', encoding='utf-8') as f:
    ctx_js = execjs.compile(f.read())


def get_headers():
    """获取 header 参数，每次请求改变"""
    headers = ctx_js.call("getHeaders")
    headers["User-Agent"] = UA
    headers["Content-Type"] = "application/json"
    headers["Host"] = "fuwu.nhsa.gov.cn"
    headers["Origin"] = "https://fuwu.nhsa.gov.cn"
    headers["Referer"] = "https://fuwu.nhsa.gov.cn/nationalHallSt/"
    return headers

def get_result():
    # q = input("请输入药品名称(默认无): ") or ""
    # drugLv = input("请输入药品等级(默认无): ") or ""
    # drugType = input("请输入剂型(默认1): ") or 1
    # page_num = input("请输入要爬取的页数(默认1): ") or 1

    for page in range(1,2):
        payload = {
            "q": "",
            "drugLv": "",
            "dosformName":"",
            "drugType": "1",
            "pageNum": "",
            "pageSize": 10
        }
        payload["pageNum"] = page
        encrypted_payload = ctx_js.call("getEncryptedData", payload)
        encrypted_data = requests.post(url=result_url, json=encrypted_payload, headers=get_headers()).json()
        decrypted_data = ctx_js.call("gdd", encrypted_data)
        drug_list = decrypted_data['list']
        df = pd.DataFrame(drug_list)
        print(df)




def main():
    get_result()

if __name__ == "__main__":
    main()
