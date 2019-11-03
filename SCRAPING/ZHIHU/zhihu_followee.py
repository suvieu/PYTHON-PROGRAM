import requests
import json
import pandas as pd
import time
user_data = []
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'}
for i in range(5):
    print("当前正在爬去第{}页".format(i+1))
    url_2 = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(i*20)
    response = requests.get(url_2, headers=headers)
    data = json.loads(response.text) # 转成字典·
    user_data.extend(data['data']) #注意append和extend方法的区别
    time.sleep(1)
df = pd.DataFrame.from_dict(user_data)
df.to_csv('user_data.csv',encoding='utf_8_sig')


