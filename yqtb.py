import requests 
session=requests.session()
url="http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp"
post_url="http://yqtb.nwpu.edu.cn/wx/ry/ry_util.jsp"
login_url="https://uis.nwpu.edu.cn/cas/login"
login_data= {
    #学号
    'username': '2018xxxxxx',
    #密码
    'password': '123123',
    'currentMenu': '1',
    'execution': 'e1s1',
    "_eventId":"submit"
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}
response=session.get(login_url,headers=header)
response=session.post(login_url,data=login_data)
if "欢迎使用" in response.text:
    print("login successfully")
else:
    print("login unsuccessfully")
params={
    "xasymt": "1",
    "actionType": "addRbxx",
    #学号
    "userLoginId": "123123",
    "szcsbm": "1",
    "bdzt": "1",
    "szcsmc": "在学校",
    "sfyzz": "0",
    "sfqz": "0",
    "tbly": "sso",
    "qtqksm": "",
    "ycqksm": "",
    "userType": "2",
    #姓名
    "userName": "瓜皮"
}
html=session.get(url)
session.headers.update({'referer': 'http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp'})
html=session.post(post_url,data=params)
print(html.text)
