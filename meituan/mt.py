#导入包
import base64
import zlib
import time
import urllib.parse
import requests
import pandas as pd
from fake_useragent import UserAgent
import time
import random

def get_query(page):
    # 地点名称
    cityName = '北京'
    # 美食类型
    cateId = 0
    # 地区类型
    areaId = 0
    # 分类方法
    sort = ''
    dinnerCountAttrId = ''
    # 查询页数
    userId = '你的userId'
    uuid = 'f7a37ba044bf4893b818.1644195224.1.0.0'
    platform = 1
    partner = 126
    riskLevel = 1
    optimusCode = 10
    originUrl = 'https://bj.meituan.com/meishi/pn1/'
    query = 'cityName=%s&cateId=%d&areaId=%d&sort=%s&dinnerCountAttrId=%s&page=%d&userId=%s&uuid=%s&platform=%d&partner=%d&originUrl=%s&riskLevel=%d&optimusCode=%d' % (
        cityName, cateId, areaId, sort, dinnerCountAttrId, page, userId, uuid, platform, partner, originUrl, riskLevel,
        optimusCode)
    query_after = query.split('&')
    query_all = []
    true_query = ''
    #参数排序
    for i in query_after:
        i = i.split('=')
        if i == query_after[-1]:
            query_all.append(i[0] + '=' + i[1])
        else:
            query_all.append(i[0] + '=' + i[1] + '&')
    for j in sorted(query_all):
        true_query += j
    true_query = true_query[:-1]
    true_query = "\"" + true_query + "\""
    #获取sign
    sign = get_encrypt(true_query)
    #获取token
    token = get_token(sign,page)
    #编码token
    token = urllib.parse.quote(token)
    return query + '&_token=' + token

def get_encrypt(deflate_text):
    # 直接zlib压缩提示要转字节类型
    info = str(deflate_text).encode()
    # 进行def压缩
    temp = zlib.compress(info)
    # 压缩后进行base64加密
    baseenco = base64.b64encode(temp)
    # 加密后转str文本
    result = str(baseenco,encoding='utf-8')
    return result
def get_token(sign,page):
    #构造token
    first_refer = "https://bj.meituan.com/meishi/pn{}/".format(page)
    second_refer = "https://bj.meituan.com/meishi/pn{}/".format(page + 1)
    token ={
        'rId' : 100900,
        'ver' : "1.0.6",
        'ts' : int(round(time.time() * 1000)-150 * 1000),
        'cts' : int(round(time.time() * 1000)),
        'brVD' : [254, 754],
        'brR' : [[1536, 864],[1536, 824],24,24],
        'bI' : [first_refer,second_refer],
        'mT': [],
        'kT': [],
        'aT': [],
        'tT': [],
        'aM': "",
        'sign':sign
    }
    # print(str(token))
    result = get_encrypt(token)
    return result

def get_df(page):
    ua = UserAgent()
    headers = {
        "Host": "bj.meituan.com",
        "Connection": "keep-alive",
        "Accept": "application/json",
        "Sec-Fetch-Dest": "empty",
        "User-Agent": "",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Referer": "https://bj.meituan.com/meishi/pn1/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "你的cookie",

    }
    headers["User-Agent"] = ua.chrome
    resp = requests.get(url='https://bj.meituan.com/meishi/api/poi/getPoiList?' + get_query(page),
                        headers=headers, verify=False)
    data_list = resp.json()['data']['poiInfos']
    d_list = []
    for data in data_list:
        deals = data['dealList']
        data.pop('dealList')
        for deal in deals:
            data_dict = data
            data_dict['deal_title'] = deal['title']
            data_dict['deal_price'] = deal['price']
            data_dict['deal_soldCounts'] = deal['soldCounts']
            d_list.append(data_dict)
    df = pd.DataFrame(d_list)
    return df
    
def main():
    d_list = []
    for page in range(1,3):
        df = get_df(page)
        d_list.append(df)
        time.sleep(random.randint(5,10))
    table = pd.concat(d_list)
    table.to_excel(r'C:\xxx\美团食品.xlsx',index=False)

if __name__ == '__main__':
    main()
