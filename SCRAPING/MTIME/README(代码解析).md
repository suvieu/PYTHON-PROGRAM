## 注意：本人是python新手，以下所有解析主要目的是记录本人在学习中的探索过程，拿出来与大家分享，写出来的代码一定有很多能改进的地方，还请各位大神不吝赐教。非常感谢！！

**从时光网爬取指定年份 评分在7-10分之间的电影信息(包括电影名/链接/评分/年代)**  
**时光网的分类查询页面：http://movie.mtime.com/movie/search/section/#**
<br>

**时光网的页面是通过AJAX异步加载的，在浏览器上关闭JAVASCRPIT 会发现网页变成如下的样子(图1)，如果直接用request对上面的URL进行请求，只能得到这个页面的HTML代码，但是这个页面是没有分类查询的任何功能和信息的。**

图1
![Image](https://github.com/suvieu/PYTHON-PROGRAM/blob/master/SCRAPING/MTIME/PIC/1.png)


**所以我们要通过审查元素中的NETWORK找到真正属于分类查询页面的URL。**

**在分类查询页面内查询后(我这里按2015年 评分7-10分进行查询)。在NETWORK中刷新后得到响应文件，可以看到下面红圈中(图2)都是筛选结果的电影海报图片**

图2

![image](https://github.com/suvieu/PYTHON-PROGRAM/blob/master/SCRAPING/MTIME/PIC/1.png)

**在这些JPG上面有一个叫search.msc?...的文件，点进去粗略地看了下response，能看到电影名称，感觉应该就是这个文件了。再进一步查看这个文件请求的URL(图3)，很长一段，直接在浏览器中访问这个链接(图4) 又获得一大段HTML代码。可以看到这段代码里有我们需要的所有信息了(电影名称/链接/评分/年代)，所以这才是我们需要用request进行请求的URL**

图3

![image](https://github.com/suvieu/PYTHON-PROGRAM/blob/master/SCRAPING/MTIME/PIC/3.png)

图4

![image](https://github.com/suvieu/PYTHON-PROGRAM/blob/master/SCRAPING/MTIME/PIC/4.png)

**接下来就是对这段response进行解析；这里用正则表达式去抓我们需要的信息。这里的正则表达式并不难，需要注意的是评分是分整数和小数的。把抓取到的内容都放在movie_info变量中，再把movie_info放到movie_list列表中

```python
import re
name_pattern = re.compile(r'<a title=\\"(.*?)/[\s\S]*?href=\\"(.*?)\\"[\s\S]*?class=total>(\d)<[\s\S]*?class=total2>(.*?)<[\s\S]*?span class=\\"c_666\\">\((.*?)\)<')
movie_info=name_pattern.findall(response)
movie_list.extend(movie_info)
```

**下一步就是要实现翻页功能，主要还是通过比较不同页URL之间的区别，找到控制页码/年代/评分的参数，在后续写for循环的时候用变量替换。具体区别如下图**

![image](https://github.com/suvieu/PYTHON-PROGRAM/blob/master/SCRAPING/MTIME/PIC/5.png)

**黄色标注是固定不变的，蓝色部分是相关参数，year/rating/pageindex/t分别代表了年代/评分/页数/请求的时间，后面灰色部分看augument就知道也是参数，一共20个参数，其中也有代表年代/评分/页数的参数(图中标蓝的部分)，在翻页时需要同步更改，具体每个AUGMENT控制了哪个变量在我不断的尝试下终于弄清了大部分**

Ajax_CallBackArgument2: 国家/地区，如美国275，中国138

Ajax_CallBackArgument3: 类型，

Ajax_CallBackArgument11:评分下限

Ajax_CallBackArgument12:评分上限

Ajax_CallBackArgument14：中文名首字母

Ajax_CallBackArgument16: 英文名首字母

Ajax_CallBackArgument17:排序方法·

Ajax_CallBackArgument18:页数

**找到了翻页的规律，我们只要在URL对应的位置换成变量就行了。还有个问题是要怎么知道这一页是最后一页呢？**
**查看最后一页的URL，发现最后一页有一行特有的HTML代码<a class=\\"mr10 false\\">下一页，所以只要加一个if语句，如果正则表达式能抓到这段，就说明时最后一页，那么就终止循环。**
```python
next_pattern = re.compile(r'<a class=\\"mr10 false\\">下一页')
next = next_pattern.search(response)
if next != None:
    break
```
**最后是数据的输出。等全部循环完了后，把movie_list导入进pandas中**

```python
movie_df=pd.DataFrame(movie_list,columns=['电影名称','链接','得分—整数','得分—小数','年份'])
```
**在pandas中对数据进行整合，因为一开始抓取的整数和小数其实是文本格式，所以先要转化成数字格式**
```python
movie_df[['得分—整数','得分—小数']] = movie_df[['得分—整数','得分—小数']].apply(pd.to_numeric)
```
**把整数和小数相加，得出总评分**
```python
movie_df['评分']=movie_df['得分—整数']+movie_df['得分—小数']
final_df = movie_df[['年份','电影名称','链接','评分']]
```
**最后用to_csv导出为csv文件,mode a为不覆盖原来的内容导入**
```python
final_df.to_csv('movie.csv',encoding='utf_8_sig',index=False,mode='a')
```
**这样基本就大功告成了！[(查看完整代码)](https://github.com/suvieu/PYTHON-PROGRAM/blob/master/SCRAPING/MTIME/MTIME.py)**

<br>

**还有一种方法是把数据直接导入进MYSQL数据库中**

**导入pymysql模块，对接MYSQL 数据库，插入数据即可，注意这里一定要写db.commit()才会真正实现数据导入**
```python
import pymysql
def Insert(VALUE):
    db = pymysql.connect(host="localhost", user="Simon",password= "******",port=3306, db='movie')
    cursor = db.cursor()
    sql = "INSERT INTO MTIME(NAME,LINK,POINT,POINT2,YEAR) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql,VALUE)
    db.commit()
    db.close()




