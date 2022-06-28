import requests
import time
import execjs
import random
import pandas as pd
import logging
logging.basicConfig(level=logging.INFO,format = '%(asctime)s-%(levelname)s:%(message)s')

with open("get_headers.js",'r',encoding='utf-8') as f:
    ctx = execjs.compile(f.read())
def activate_randomcode():
    url = "http://search.kongfz.com/product_result/?status=0&key=%E8%87%AA%E6%8E%A7%E5%8A%9B&select=0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39"
    }
    resq = requests.get(url, headers=headers)
    cookies = requests.utils.dict_from_cookiejar(resq.cookies)
    randomcodekey = cookies.get("randomcodekey")
    randomcode = cookies.get("randomcode")
    return randomcodekey,randomcode

def get_data(page):
    randomcodekey, randomcode = activate_randomcode()
    randomcodesign = ctx.call("rqEncrypt",randomcode)
    ts = int(time.time() * 1000)
    url = f"http://search.kongfz.com/product_result"
    X_Tingyun_Id = "OHEPtRD8z8s;r=" + str(int(ts % 1e9))
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Cookie": f"randomcodekey={randomcodekey}; randomcode={randomcode}; randomcodesign={randomcodesign}; acw_tc=2760829316549959699328163e5a61ea6b659b7180a41fdb6e5a6af791af69; PHPSESSID=jak032um8rn410l2fqu4sbj9i3; shoppingCartSessionId=9d47c5320cfa7726a200ed555fe527dc; reciever_area=1006000000; Hm_lvt_bca7840de7b518b3c5e6c6d73ca2662c=1654995971; Hm_lvt_33be6c04e0febc7531a1315c9594b136=1654995971; kfz_uuid=07126066-d071-4e61-9e51-c4bad3a4e933; kfz_trace=07126066-d071-4e61-9e51-c4bad3a4e933|0|5c57614062157fd1|; TY_SESSION_ID=5ab6ec3f-c5b3-47df-8ba5-7cd7f7bf7646; kfz-tid=5fa8563403aa6246eca29a01bba5c681; Hm_lpvt_33be6c04e0febc7531a1315c9594b136=1654997210; Hm_lpvt_bca7840de7b518b3c5e6c6d73ca2662c=1654997210",
        "Host": "search.kongfz.com",
        "Referer": "http://search.kongfz.com/product_result/?status=0&key=%E8%87%AA%E6%8E%A7%E5%8A%9B&select=0&pagenum=2&ajaxdata=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39",
        "X-Requested-With": "XMLHttpRequest",
        "X-Tingyun-Id": X_Tingyun_Id
    }
    params = {
        "status": "0",
        "key": "自控力",
        "select": "0",
        "pagenum": str(page),
        "ajaxdata": "1",
        "type": "1",
        "_": str(ts)
    }
    resq = requests.get(url, headers=headers,params=params)
    logging.info("获取的内容为%s",resq.json())
    data = resq.json().get("data").get('itemList')
    return data

def run():
    results = []
    for page in range(1,3):
        logging.info("正在获取第%s页",page)
        data = get_data(page)
        results.extend(data)
        logging.info("已经获取第%s页",page)
        time.sleep(random.uniform(2,3))
    # df = pd.DataFrame(results)
    # df.to_excel(r"C:\Users\tslilove\Desktop\自控力.xlsx",index=False)

if __name__ == '__main__':
    run()
