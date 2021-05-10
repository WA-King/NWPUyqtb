# 加入个人信息
填写学号和密码


![image](https://user-images.githubusercontent.com/44970685/117688063-04269380-b1eb-11eb-9cce-14e6ff6f8bbc.png)


填写学号和姓名(中文)

![image](https://user-images.githubusercontent.com/44970685/117688097-0daffb80-b1eb-11eb-898c-13fbbf9a7de3.png)

# 自动定时运行脚本
+ 首先有一台服务器
+ `crontab -e` 
+ 在最后添加`0 8 * * * python解释器的绝对路径 脚本的绝对路径` 
+ 
  例如`0 8 * * * /usr/bin/python3 /home/ubuntu/scripts/yqtb/yqtb.py`
  
  表示每天8点运行一次执行脚本的命令 
  
