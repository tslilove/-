#导入包
import time
from DecryptLogin import login
import requests
import json
from DecryptLogin.utils.cookies import *
import pandas as pd

class JD:
    def get_data(self):
        url = 'https://search-x.jd.com/Search'
        params ={
            'area': '1',
            'enc': 'utf - 8',
            'keyword':'母婴',
            'adType': '7',
            'page': '1',
            'ad_ids': '291:33',
            'xtest': 'new_search',
            '_': str(time.time()*1000)
        }
        if os.path.isfile('session.pkl'):
            print('[INFO]: 检测到已有会话文件session.pkl, 将直接导入该文件...')
            session = requests.Session()
            infos_return,session = loadSessionCookies(session=session,cookiespath='session.pkl')
            res = session.get(url, params=params)
            data_json = json.loads(res.text)
            items = data_json.get('291')
            goods = []
            for item in items:
                goods.append({
                    'image_url': item.get('image_url', ''),
                    'price': item.get('pc_price', ''),
                    'shop_name': item.get('shop_link', {}).get('shop_name', ''),
                    'num_comments': item.get('comment_num', ''),
                    'link_url': item.get('link_url', ''),
                    'color': item.get('color', ''),
                    'title': item.get('ad_title', ''),
                    'self_run': item.get('self_run', ''),
                    'good_rate': item.get('good_rate', '')
                })
            # print(goods)
            df = pd.DataFrame(goods)
            print(df)
        else:
            session = requests.Session()
            session.get(url,params=params)
            saveSessionCookies(session=session,cookiespath='session.pkl')


if __name__ == '__main__':
    jd = JD()
    jd.get_data()
