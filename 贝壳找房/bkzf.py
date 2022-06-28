import requests
from lxml import etree

def get_page(page):
    if page == 1:
        url = f'https://bj.ke.com/ershoufang/'
    else:
        url = f'https://bj.ke.com/ershoufang/pg{page}'
    headers = {
    "Cookie": "lianjia_uuid=ca2bd021-a4ab-4362-bc0b-cba8cce60a32; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1646628788; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217f62b9585d87f-00f90eb50fde98-56171d58-1327104-17f62b9585ed74%22%2C%22%24device_id%22%3A%2217f62b9585d87f-00f90eb50fde98-56171d58-1327104-17f62b9585ed74%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E8%B4%9D%E5%A3%B3%E6%89%BE%E6%88%BF%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wybeijing%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; select_city=110000; lianjia_ssid=dc8a789c-1d2a-43b8-aeb0-16466b6a7c31; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1648348483; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMWRiZDM3MDQ3NTlkNmU2ODVlOTZjNDUyZGYzN2EyOGE5YWJjZTc3NDJkNWNkMDhmNzM4NDM3YmI1MjllOWZkODMzYjcxYjExYjM1MGVlYWExYzQyN2Q4M2Q4ZGZhYzVkYTQ2M2VjNDdhNjJkMTRiYTU0NzBkNzI5NjM4MmM1ZDJkMTMxZTA4MzMzZTFhZDViYjNhYjk2ZWQ5OTgwNDQyMDZjMTM5Y2M1MzBkZjMzODE3MTE0OTUxNTliZWYxMzMzMmJhYzQ4MGE5MzYwNTg4ODJhNDM2NjMyN2Y3NTc4YTE5NjMzMzQxZjg2MzUyNTI5ZDljY2U1OWFmZjJiOWU0MFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI4ZDY3NzM0Y1wifSIsInIiOiJodHRwczovL2JqLmtlLmNvbS9lcnNob3VmYW5nL3BnMi8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52"
    }
    resq = requests.get(url,headers=headers,verify = False)
    if resq.status_code == 200:
        etree_element = etree.HTML(resq.text)
        title = etree_element.xpath('//li[@class="clear"]/div/div[1]/a/text()')
        title = title[:-1]
        position = etree_element.xpath('//li[@class="clear"]/div/div[2]/div[1]/div/a/text()')
        houseInfo = etree_element.xpath('//li[@class="clear"]/div/div[2]/div[2]/text()')
        houseInfo_list = []
        for house in [i.replace(" ", '').replace("\n", '') for i in houseInfo]:
            if house:
                houseInfo_list.append(house)
        stars = etree_element.xpath('//li[@class="clear"]/div/div[2]/div[3]/text()')
        stars_list = []
        for star in [i.replace(" ", '').replace("\n", '') for i in stars]:
            if star:
                stars_list.append(star)
        tags = etree_element.xpath('//li[@class="clear"]/div/div[2]/div[4]')
        tags_list = []
        for tag in tags:
            tag = ",".join(tag.xpath('span/text()'))
            tags_list.append(tag)
        price = etree_element.xpath('//li[@class="clear"]/div/div[2]/div[5]/div[1]/span/text()')
        area = etree_element.xpath('//li[@class="clear"]/div/div[2]/div[5]/div[2]/span/text()')
        print(len(title),title)
        print(len(position),position)
        print(len(houseInfo_list),houseInfo_list)
        print(len(stars_list),stars_list)
        print(len(tags_list),tags_list)
        print(len(price),price)
        print(len(area),area)
def run():
    for page in range(1,3):
        get_page(page)

if __name__ == '__main__':
    run()
