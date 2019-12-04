import requests
from lxml import html
class Login(object):
    def __init__(self):
        self.headers={
            'Referer':'https://github.com',
            'User-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
            'Host':'github.com'
        }
        self.login_url='https://github.com/login'
        self.post_url='https://github.com/session'
        self.logined_url='https://github.com/'
        self.session=requests.Session()

    def token(self):
        response = self.session.get(self.login_url,headers=self.headers)
        selector = html.etree.HTML(response.text)
        token =selector.xpath('//*[@id="login"]/form/input[2]/@value')[0]
        return token



    def login(self,email,password):
        post_data={
            'commit':'Sign in',
            'utf8':'✓',
            'authenticity_token':self.token(),
            'login':email,
            'password':password
        }
        response = self.session.post(self.post_url,data=post_data,headers=self.headers)
        print(self.session.get(self.logined_url).content)






