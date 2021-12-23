# 加入个人信息

将`config-example.json`重命名为`config.json`，并向其中填写学号、密码、姓名。

![image](https://user-images.githubusercontent.com/39238310/147223459-8086e8d5-09a4-43d5-81cf-3814e78e1e6f.png)

之后运行`python3 yqtb.py`即可。

此报文只适用于**在学校**，其余情况请通过浏览器手动抓取报文，替换对应的数据。
# 自动定时运行脚本
+ 首先有一台服务器
+ 执行`crontab -e` 
+ 在最后添加`0 8 * * * python解释器的绝对路径 脚本的绝对路径` 

  例如![image](https://user-images.githubusercontent.com/44970685/117689963-e1957a00-b1ec-11eb-9a2e-df1c83aea207.png)

  
  表示每天8点运行一次执行脚本的命令 
  
