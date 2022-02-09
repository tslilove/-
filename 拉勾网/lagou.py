import time
import requests
import pymysql

def insert(sql,result):
    global cnn,curor

    try:
        cnn = pymysql.connect(user='用户名',host='服务器地址',password='用户密码',database='数据库')
        curor = cnn.cursor()
        curor.execute(sql,result)
        cnn.commit()
    except Exception as e:
        print(e)
        print(sql)
    finally:
        curor.close()
        cnn.close()

def position(page):
    url = 'https://www.lagou.com/jobs/v2/positionAjax.json'
    headers={
        'cookie': 'user_trace_token=20211108122629-e87c157b-d29c-45c3-93d8-7c35ec05dbdd; _ga=GA1.2.204839220.1636345590; LGUID=20211108122630-ff59fb86-abbb-48c1-ab4a-e0a1e5a8bd15; RECOMMEND_TIP=true; JSESSIONID=ABAAABAABEIABCI0B7CE793959598BC278EA919ABC49AFA; WEBTJ-ID=20220101153222-17e148dc51864c-0be0d3f75da033-4303066-1327104-17e148dc5197a9; privacyPolicyPopup=false; LGSID=20220101153222-0749f009-452a-4ff7-990c-8b708a6fb4e2; sensorsdata2015session=%7B%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1641022343; _gid=GA1.2.1921694243.1641022343; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; __SAFETY_CLOSE_TIME__20690118=1; login=false; unick=""; _putrc=""; X_HTTP_TOKEN=01060247481f7f1848332014610097a59f371b9eed; LGRID=20220101154944-e7155d88-cb85-495a-9fe6-f7a5fecadfb5; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1641023385; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2220690118%22%2C%22%24device_id%22%3A%2217cfdcc88dca74-0cf3b514b106a5-57b1a33-1327104-17cfdcc88deb64%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2296.0.4664.110%22%7D%2C%22first_id%22%3A%2217cfdcc88dca74-0cf3b514b106a5-57b1a33-1327104-17cfdcc88deb64%22%7D',
        'Origin': 'https://www.lagou.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    data = {
            'first': 'true',
            'needAddtionalResult': 'false',
            'city': '北京',
            'px': 'new',
            'pn': str(page),
            'labelWords': 'sug',
            'cl':'false',
            'fromSearch': 'true',
            'suginput': '数据分析',
            'kd': '数据分析'
    }
    res = requests.post(url,data=data,headers=headers,verify = False)
    data_json = res.json()
    # print(data_json)
    data_list = data_json.get('content').get('positionResult').get('result')
    # print(data_list)
    sql = "insert into position_detail(city,district,positionName,companyFullName,companySize,industryField,financeStage,companyLabelList,createTime,salary,salaryMonth,workYear,jobNature,education,positionAdvantage,hitags,positionDetail,positionAddress)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    for data in data_list:
        city = data.get('city')
        district = data.get('district')
        positionName = data.get('positionName')
        companyFullName = data.get('companyFullName')
        companySize = data.get('companySize')
        industryField = data.get('industryField')
        financeStage = data.get('financeStage')
        companyLabelList = data.get('companyLabelList')
        if companyLabelList:
            companyLabelList = ','.join(companyLabelList)
        else:
            companyLabelList = ''
        createTime = data.get('createTime')
        salary = data.get('salary')
        salaryMonth = data.get('salaryMonth')
        workYear = data.get('workYear')
        jobNature = data.get('jobNature')
        education = data.get('education')
        positionAdvantage = data.get('positionAdvantage')
        hitags = data.get('hitags')
        if hitags:
            hitags = ','.join(hitags)
        else:
            hitags = ''
        positionDetail = data.get('positionDetail').replace('<p>','').replace('</p>','').replace('<br/>','').replace('<br>','')
        positionAddress = data.get('positionAddress')
        result = (city,district,positionName,companyFullName,companySize,industryField,financeStage,companyLabelList,createTime,salary,salaryMonth,workYear,jobNature,education,positionAdvantage,hitags,positionDetail,positionAddress)
        print(result)
        insert(sql,result)
        print('插入成功',sql)
if __name__ == '__main__':
    for page in range(1,2):
        position(page)
        time.sleep(2)


