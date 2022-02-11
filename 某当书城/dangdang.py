#导入包
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

class ddBook:
    def get_ht(self):
        url = 'https://search.dangdang.com/'
        headers = {
            'Cookie': 你的cookie,
            'User-Agent': 你的ua,
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }
        params = {
            'key': 'python',
            'act': 'input',
            'page_index': self.page
        }

        res = requests.get(url, headers=headers, params=params)
        ht_text = res.text
        return ht_text
    def get_data(self):
        ht_text = self.get_ht()
        soup = BeautifulSoup(ht_text, "lxml")
        items = soup.select('.bigimg>li')
        title_list = []
        resume_list = []
        now_price_list = []
        decoration_price_list = []
        discount_list = []
        e_price_list = []
        review_count_list = []
        author_list = []
        date_list = []
        pubulish_list = []
        # print(len(items))
        for item in items:
            #获取标题
            title = item.select('.name>a')
            for t in title:
                title_list.append(t.attrs['title'])
            #获取简介
            resume = item.select('.detail')
            for r in resume:
                resume_list.append(r.string)
            #获取现价
            now_price = item.select('.price>.search_now_price')
            for np in now_price:
                now_price_list.append(np.string.replace('¥',''))
            #获取定价
            decoration_price = item.select('.price>.search_pre_price')
            for dp in decoration_price:
                decoration_price_list.append(dp.string.replace('¥', ''))
            #获取折扣
            discount = item.select('.price>span.search_discount')
            if discount:
                for d in discount:
                    discount_list.append(d.string.replace("\xa0(",'').replace(')',''))
            else:
                discount_list.append('')
            #获取电子书价格
            e_price = item.select('.price>a.search_e_price>i')
            if e_price:
                for ep in e_price:
                    e_price_list.append(ep.string.replace('¥', ''))
            else:
                e_price_list.append('')
            #获取评论数
            review_count = item.select('.search_star_line>a.search_comment_num')
            if review_count:
                for rc in review_count:
                    review_count_list.append(rc.string.replace('条评论', ''))
            else:
                review_count_list.append('')
            #作者，日期，出版社
            ar = item.select('.search_book_author>span')
            # 获取作者
            if ar:
                try:
                    author = ar[0]
                    author_list.append(author.select('a')[0].attrs['title'])
                except:
                    author_list.append('')
            else:
                author_list.append('')
            #获取日期
            if ar:
                date = ar[1]
                date_list.append(date.string.replace(' /',''))
            else:
                date_list.append('')
            #获取出版社
            try:
                if ar:
                    pubulish = ar[2]
                    pubulish_list.append(pubulish.select('a')[0].attrs['title'])
                else:
                    pubulish_list.append('')
            except:
                pubulish_list.append('')
        data = {
            '标题':title_list,
            '简介':resume_list,
            '现价':now_price_list,
            '定价':decoration_price_list,
            '折扣':discount_list,
            '电子书价格':e_price_list,
            '评论数':review_count_list,
            '作者':author_list,
            '日期':date_list,
            '出版社':pubulish_list
        }
        return data
    def get_df(self):
        data = self.get_data()
        df = pd.DataFrame(data)
        return df
    def run(self):
        df_list = []
        for page in range(1,5):
            time.sleep(3)
            self.page = page
            df = self.get_df()
            df_list.append(df)
        dfs = pd.concat(df_list)
        dfs.to_excel(r"C:\xxx\当当.xlsx",index=None)

if __name__ == '__main__':
    dd = ddBook()
    dd.run()

