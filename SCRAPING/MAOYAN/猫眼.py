import requests
import re
import pandas as pd
import time
movie = []
title = ['RANK','NAME','RELEASE TIME','INTEGER','FRACTION']
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'}
headers2={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
for i in range(10):
    url = 'https://maoyan.com/board/4?offset={}'.format(i*10)
    response = requests.get(url,headers=headers2).text
    pattern = re.compile(r'<dd>.*?board-index.*?>(\d+)</i>.*?data-src=".*?".*?name"><a.*?>(.*?)</a>.*?star">.*?</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,response)
    time.sleep(1)
    for item in items:
        movie.append(item)

movie_info=pd.DataFrame(movie,columns=title)
movie_info.to_excel('MAOYAN.xlsx')

