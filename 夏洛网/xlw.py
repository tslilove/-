import requests
from lxml import etree


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Proxy-Connection": "keep-alive",
    "Referer": "http://nianjian.xiaze.com/info/list_1_2.html",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37"
}
def getData(page):
    url = f"http://nianjian.xiaze.com/info/list_1_{page}.html"
    response = requests.get(url, headers=headers, verify=False)

    html = response.content.decode("utf-8")
    element = etree.HTML(html)
    items = element.xpath("/html/body/div[3]/div[1]/div[2]/ul/li")
    for item in items:
        "-----------------------获取title-------------------------"
        title = item.xpath("a[2]/text()")
        if title:
            title = "[统计年鉴信息] " + title[0]
        if not title:
            title = "[统计年鉴信息] " + item.xpath("a[2]/b/text()")[0]
        "-----------------------获取日期和点击量-------------------------"
        dateAndClick = item.xpath("span/text()")
        date = dateAndClick[1]
        click = dateAndClick[2].replace(" ", "")
        # dateAndClick = etree.tostring(dateAndClick[0],method="text",encoding="utf-8")
        # dateAndClick = dateAndClick.decode().replace("\n","")
        # date = dateAndClick[:23]
        # click = dateAndClick[23:]
        "-----------------------获取摘要-------------------------"
        summary = item.xpath("p/text()")
        if summary:
            summary = summary[0].strip()
        else:
            summary = ''
        result = {"标题": title, "日期": date, "点击": click, "摘要": summary}
        print(result)
def run():
    for page in range(1,10):
        print(f"正在获取第{page}页")
        getData(page)

if __name__ == '__main__':
    run()
