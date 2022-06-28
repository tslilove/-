import requests
import logging
import re
from bs4 import BeautifulSoup
import json
import time
import pandas as pd
import warnings
warnings.filterwarnings("ignore") #忽略警告
logging.basicConfig(level=logging.INFO,format = '%(asctime)s-%(levelname)s:%(message)s')

#获取页数构造
def get_s(page):
    i = page
    if i<=1:
        start = 1
        return start
    else:
        start = (i-1)*30 -4
        return start
#获取评论数
def scrapy_comment(referenceIds,headers):
    cm_url = 'https://club.jd.com/comment/productCommentSummaries.action?'
    params = {
        "referenceIds": referenceIds,
        "callback": "jQuery8920559",
        "_": str(int(time.time() * 1000))
    }
    comment_text = requests.get(cm_url, headers=headers, params=params,verify = False)
    comment = json.loads(comment_text.text[14:][:-2])
    cm_list = comment.get('CommentsCount')
    skuIdList = []
    commentList = []
    for item in cm_list:
        skuIdList.append(item.get('SkuId'))
        commentList.append(item.get('CommentCountStr'))
    return skuIdList,commentList
#返回DataFrame表格
def trans_df(dd):
    df = pd.DataFrame(dd)
    return df
#获取每一页数据
def scrapy_page(page):
    url = 'https://search.jd.com/s_new.php'
    headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "cookie": "__jda=122270672.1648956133727188726100.1648956134.1648956134.1648956134.1; __jdb=122270672.1.1648956133727188726100|1.1648956134; __jdc=122270672; __jdv=122270672|direct|-|none|-|%s; __jdu=1648956133727188726100; qrsc=1; shshshfpb=usa4w8nrVxHVxHwMxDdtSyA; shshshfp=b469c2ab5ffd426b5009aafb636123cb; shshshfpa=94d128b3-9e9c-3f34-c5f2-591018ad5306-1642586801; shshshsID=42736decfeb8b7afbd553d0ea58c8019_1_1648956134390; rkv=1.0; areaId=1; ipLoc-djd=1-2802-0-0; 3AB9D23F7A4B3C9B=K5BMO6QSWSXCVAA5IXB5YX3T42GTB6ALNGN2HPV3NISFXPEXJXWPUI5PFAN2TY4JNIRHT6VIUQ6S2KZ46PB5GSMTRI"%(int(time.time()*1000)),
    "referer": "https://search.jd.com/Search?keyword=%E5%81%A5%E8%BA%AB%E5%99%A8%E6%9D%90&suggest=1.def.0.SAK7%7CMIXTAG_SAK7R%2CSAK7_M_AM_L5396%2CSAK7_M_COL_R%2CSAK7_S_AM_R%2CSAK7_SC_PD_R%2CSAK7_SM_PB_L16675%2CSAK7_SS_PM_R%7C&wq=%E5%81%A5%E8%BA%AB%E5%99%A8%E6%9D%90&pvid=f69927e6322447c783545706e3e4c6a2&page=1&s=1&click=0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55",
    "x-requested-with": "XMLHttpRequest"
    }
    s = get_s(page)
    if page%2 == 0:
        data = {
            "keyword": "健身器材",
            "suggest": "1.def.0.SAK7|MIXTAG_SAK7R,SAK7_M_AM_L5396,SAK7_M_COL_R,SAK7_S_AM_R,SAK7_SC_PD_R,SAK7_SM_PB_L16675,SAK7_SS_PM_R|",
            "wq": "健身器材",
            "pvid": "f69927e6322447c783545706e3e4c6a2",
            "page": str(page),
            "s": str(s),
            "scrolling": "y",
            "log_id": str(time.time()*1000),
            "tpl": "3_M",
            "isList": "0",
            "show_items": ""
        }
    else:
        data = {
        "keyword": "健身器材",
        "suggest": "1.def.0.SAK7|MIXTAG_SAK7R,SAK7_M_AM_L5396,SAK7_M_COL_R,SAK7_S_AM_R,SAK7_SC_PD_R,SAK7_SM_PB_L16675,SAK7_SS_PM_R|",
        "wq": "健身器材",
        "pvid": "f69927e6322447c783545706e3e4c6a2",
        "page": str(page),
        "s": str(s),
        "click": "0"
        }
    resq = requests.get(url,headers=headers,params=data,verify=False)
    if resq.status_code == 200:
        html = resq.text
        referenceIds = re.findall("log:\{wids:'(.*?)',uuid",html)[0]
        soup = BeautifulSoup(html,"lxml")
        shop_list = []
        title_list = []
        price_list = []
        link_list = []
        if page%2 != 0:
            items = soup.select('#J_goodsList > ul>li')
        else:
            items = soup.select('.gl-item>.gl-i-wrap')
        for item in items:
            """-------------标题------------"""
            title = item.select('.p-name.p-name-type-2>a>em')
            if title:
                tl = title[0].text.replace("\n",'').replace("\t",'').replace(" ",'')
                if tl[:4] == "线下同款":
                    tll = tl[:4]+ " " + tl[4:]
                    title_list.append(tll)
                else:
                    title_list.append(tl)
            else:
                title_list.append('')
            """-------------price------------"""
            price = item.select('.p-price>strong>i')
            if price:
                price_list.append(price[0].text)
            else:
                price_list.append('')
            """-------------详情链接------------"""
            link = item.select('.p-name.p-name-type-2>a')
            if link:
                link_list.append("https:"+link[0].attrs['href'])
            else:
                link_list.append('')
            """-------------旗舰店------------"""
            shop = item.select('.p-shop>span>a')
            if shop:
                shop_list.append(shop[0].text)
            else:
                shop_list.append('')
        skuIdList, commentList = scrapy_comment(referenceIds,headers)
        return {'skuId':skuIdList,'title':title_list,'price':price_list,'link':link_list,'shop':shop_list,'comment':commentList}
#总方法
def run():

    df = []
    try:
        for page in range(1,11):
            # scrapy_page(page)
            dd = scrapy_page(page)
            # trans_df(dd).to_excel('ces.xlsx',index=False)
            # print(trans_df(dd))
            # print('正在获取第%s页'%page)
            logging.info("正在获取第%s页,数据为%s",page,dd)
            time.sleep(2)

    except:
        logging.error('长度不一致')


if __name__ == '__main__':
    run()
