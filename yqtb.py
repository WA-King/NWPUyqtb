import requests 
import re
import sys
session=requests.session()
url="http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp"
post_url="http://yqtb.nwpu.edu.cn/wx/ry/ry_util.jsp"
login_url="https://uis.nwpu.edu.cn/cas/login"
if len(sys.argv)<2:
    path_config="config.json"
else:
    path_config=sys.argv[1]
with open(path_config) as f:
    from json import load
    j=load(f)
    # 学号
    username=j['username']
    # 密码
    password=j['password']
    # 姓名
    name=j['name']
login_data= {
    #学号
    'username': username,
    #密码
    'password': password,
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
    exit(1)
response=session.get("http://yqtb.nwpu.edu.cn/wx/xg/yz-mobile/index.jsp")
response=session.get("http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp")
pattern=r"url:'ry_util\.jsp\?sign=(.*).*'"
res=re.findall(pattern, response.text)
if len(res) == 0:
    print("error in script, please contact to the author")
    exit(1)
post_url+="?sign="+res[0]
params={
    "hsjc": "1",
    "xasymt": "1",
    "actionType": "addRbxx",
    #学号
    "userLoginId": username,
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
    "userName": name
}
html=session.get(url)
session.headers.update({'referer': 'http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp'})
html=session.post(post_url,data=params)
print(html.text)
