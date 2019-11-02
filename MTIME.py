import requests
import re
import pandas as pd
import time
from lxml import html
start=time.time()
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'}
year = input("请输入想查询的年份")
low_point = input("请输入想查询的评分下限(只能输入整数)")
high_point = input("请输入想查询的评分上限(只能输入整数)")
movie_list=[]
url1='http://service.channel.mtime.com/service/search.mcs?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Channel.Pages.SearchService&Ajax_CallBackMethod=SearchMovieByCategory&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2Fmovie%2Fsearch%2Fsection%2F%23year%3D'
url2 = year +'%26rating%3D'+low_point+'_'+high_point
url3 = '&t=201910311343539916&Ajax_CallBackArgument0=&Ajax_CallBackArgument1=0&Ajax_CallBackArgument2=0&Ajax_CallBackArgument3=0&Ajax_CallBackArgument4=0&Ajax_CallBackArgument5=0&Ajax_CallBackArgument6=0&Ajax_CallBackArgument7=0&Ajax_CallBackArgument8=&Ajax_CallBackArgument9='+year +'&Ajax_CallBackArgument10='+year+'&Ajax_CallBackArgument11='+low_point+'&Ajax_CallBackArgument12='+high_point+'&Ajax_CallBackArgument13=0&Ajax_CallBackArgument14=1&Ajax_CallBackArgument15=0&Ajax_CallBackArgument16=1&Ajax_CallBackArgument17=4&Ajax_CallBackArgument18={}&Ajax_CallBackArgument19=0'
url=url1+url2+url3
print(url)
n=0
while True:
    n=n+1
    print('正在爬去第{}页'.format(n))
    print(time.strftime("%H:%M:%S", time.localtime(time.time())))
    response = requests.get(url.format(n),headers=headers).text
    name_pattern = re.compile(r'<a title=\\"(.*?)/[\s\S]*?href=\\"(.*?)\\"[\s\S]*?class=total>(\d)<[\s\S]*?class=total2>(.*?)<[\s\S]*?span class=\\"c_666\\">\((.*?)\)<')
    movie_info=name_pattern.findall(response)
    movie_list.extend(movie_info)
    next_pattern = re.compile(r'<a class=\\"mr10 false\\">下一页')
    next = next_pattern.search(response)
    if next != None:
        break
    if n ==40:
        break
    time.sleep(4)
print(movie_list)
movie_df=pd.DataFrame(movie_list,columns=['电影名称','链接','得分—整数','得分—小数','年份'])
movie_df[['得分—整数','得分—小数']] = movie_df[['得分—整数','得分—小数']].apply(pd.to_numeric)
movie_df['评分']=movie_df['得分—整数']+movie_df['得分—小数']
final_df = movie_df[['年份','电影名称','链接','评分']]
final_df.to_csv('movie.csv',encoding='utf_8_sig',index=False,mode='a')
end=time.time()
print("Running time: %s seconds"%(end - start))