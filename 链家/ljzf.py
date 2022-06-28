import requests
from lxml import etree

def get_page(page):
    if page == 1:
        url = f'https://bj.lianjia.com/ershoufang/'
    else:
        url = f'https://bj.lianjia.com/ershoufang/pg{page}'
    headers = {
        "Cookie":  'lianjia_uuid=4ce5f96c-a1ea-4819-9a33-11fd9ac039b5; _smt_uid=620a1220.5af6be36; UM_distinctid=17ef756ce96182-00bf480853e95b-5b161c50-144000-17ef756ce979d3; _ga=GA1.2.1412650028.1644827171; select_city=110000; lianjia_ssid=af5701ab-3f37-4102-92dc-b937a3e90432; CNZZDATA1254525948=498159228-1648357006-https%253A%252F%252Fwww.baidu.com%252F%7C1648357006; CNZZDATA1255633284=174928217-1648351471-https%253A%252F%252Fwww.baidu.com%252F%7C1648351471; CNZZDATA1255604082=839240575-1648350569-https%253A%252F%252Fwww.baidu.com%252F%7C1648350569; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217ef756d294d39-02ad4b297ad79e-5b161c50-1327104-17ef756d295e39%22%2C%22%24device_id%22%3A%2217ef756d294d39-02ad4b297ad79e-5b161c50-1327104-17ef756d295e39%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; _jzqa=1.3479926393740567000.1644827168.1644827168.1648359209.2; _jzqc=1; _jzqckmp=1; _jzqy=1.1648359209.1648359209.1.jzqsr=baidu.-; _qzjc=1; _gid=GA1.2.1129189862.1648359210; _jzqb=1.2.10.1648359209.1; _qzja=1.2143410604.1648359209026.1648359209026.1648359209026.1648359209026.1648359311590.0.0.0.2.1; _qzjb=1.1648359209026.2.0.0.0; _qzjto=2.1.0; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1648359312; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1648359312; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMWRiZDM3MDQ3NTlkNmU2ODVlOTZjNDUyZGYzN2EyOGE5YWJjZTc3NDJkNWNkMDhmNzM4NDM3YmI1MjllOWZkODMzYjcxYjExYjM1MGVlYWExYzQyN2Q4M2Q4ZGZhYzVkYTQ2M2VjNDdhNjJkMTRiYTU0NzBkNzI5NjM4MmM1ZDJkMTMxZTA4MzMzZTFhZDViYjNhYjk2ZWQ5OTgwNDQyMDBjMDYyN2U2MTMwNWJkNDc3NWZiYzcxOTRjMjVhMjAwNTdmYzU2YTc5ZGEwZWE3Y2U3NzQ0NTA4MDQxNzZlYWUxZjQ4MjQ2M2I0OTMyZWVlNzQ3NTMzZGQyMWU0N2Q2NVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI1MmQyOGE0OFwifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52"
    }
    resq = requests.get(url, headers=headers, verify=False)
    if resq.status_code == 200:
        etree_element = etree.HTML(resq.text)
        title = etree_element.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[1]/a/text()')
        position =  etree_element.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[2]/div')
        position_list = []
        for p in position:
            po = "-".join([i.strip() for i in p.xpath('a/text()')])
            position_list.append(po)
        houseInfo = etree_element.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[3]/div/text()')
        houseInfo_list = []
        for house in [i.replace(" ", '').replace("\n", '') for i in houseInfo]:
            if house:
                houseInfo_list.append(house)
        followInfo = etree_element.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[4]/text()')
        followInfo_list = []
        for follow in [i.replace(" ", '').replace("\n", '') for i in followInfo]:
            if follow:
                followInfo_list.append(follow)
        tags = etree_element.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[5]')
        tag_list = []
        for tag in tags:
            tag = ",".join(tag.xpath('span/text()'))
            tag_list.append(tag)
        price = etree_element.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[1]/span/text()')
        price = [i.strip()+"万" for i in price]
        area = etree_element.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[2]/span/text()')
        print(len(title),title)
        print(len(position_list),position_list)
        print(len(houseInfo_list),houseInfo_list)
        print(len(followInfo_list),followInfo_list)
        print(len(tag_list),tag_list)
        print(len(price),price)
        print(len(area),area)

def run():

    for page in range(1,2):
        get_page(page)

if __name__ == '__main__':
    run()
