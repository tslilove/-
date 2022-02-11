import requests
import execjs
import pandas as pd
import json

def get_encrypt_data(page):
    """
    获取全国建筑市场监管公共服务平台的数据
    :param page: 获取页数
    :return: 返回json数据
    """
    url = 'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?'
    headers = {
        'Connection': 'keep-alive',
        'Content-Encoding': 'gzip',
        'Content-Type': 'text/json;charset=UTF-8',
        'accessToken': 'jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLXyrONVXKc8C6MeV7E6eVaKhpUUKvcMtoMqfGfwdLCb8g==',
        'Cookie': 你的cookie,
        'Referer': 'http://jzsc.mohurd.gov.cn/data/company',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

    data = {
        'pg': '',
        'pgsz': '15',
        'total': '450'
    }
    data['pg'] = str(page)
    res = requests.get(url, headers=headers, params=data)
    encrypt_text = res.text
    # print(encrypt_text)
    key = 'jo8j9wGw%6HbxfFn'
    iv = '0123456789ABCDEF'
    with open('../js_database/jzsc.js','r',encoding='utf-8') as f:
        jzsc_js = execjs.compile(f.read())
    decrypt_data= jzsc_js.call('h',encrypt_text)
    decrypt_data = json.loads(decrypt_data)
    table = decrypt_data['data']['list']
    df = pd.DataFrame(table)
    print(df)

def main():
    for page in range(1):
        get_encrypt_data(page)

if __name__ == '__main__':
    main()
