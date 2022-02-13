from gne import GeneralNewsExtractor
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = Chrome(chrome_options=chrome_options)#(r'D:\Anaconda3\chromedriver.exe')
url = 'https://finance.sina.com.cn/tech/2022-02-12/doc-ikyakumy5528418.shtml?cre=tianyi&mod=pchp&loc=1&r=0&rfunc=48&tj=cxvertical_pc_hp&tr=12'
driver.get(url)
time.sleep(3)

extractor = GeneralNewsExtractor()
result = extractor.extract(driver.page_source)
print(result['title'])
print(result['author'])
print(result['publish_time'])
print(result['content'])
