import requests
from lxml import etree
import pandas as pd

def get_data(city):
    get_url = f'http://www.air-level.com/air/{city}/'

    headers = {
        'Cookie': '你的cookie',
        'Referer': 'http://www.air-level.com/',
        'User-Agent': '你的ua'

    }
    html = requests.get(get_url, headers=headers)
    res = etree.HTML(html.text)
    items = res.xpath('/html/body/div[1]/div[3]/div[1]/div[2]/table/tr')
    air_data_list = []
    for item in items:
        if item.xpath('th[1]'):
            continue

        data = {
            'city': item.xpath('td[1]/text()')[0],
            'aqi': item.xpath('td[2]/text()')[0],
            'aqi_level': item.xpath('td[3]/span/text()')[0],
            'pm_25': item.xpath('td[4]/text()')[0] + item.xpath('td[4]/sup/text()')[0],
            'pm_10': item.xpath('td[5]/text()')[0] + item.xpath('td[5]/sup/text()')[0],
            'primary_pollutant': item.xpath('td[6]/text()')[0] if item.xpath('td[6]/text()') else ''
        }
        air_data_list.append(data)
    df = pd.DataFrame(air_data_list)
    print(df)

if __name__ == '__main__':
    city = input("请输入你要查询的城市：") #这里可以换成城市列表

    try:
        get_data(city)
    except:
        print("这个城市不存在")
