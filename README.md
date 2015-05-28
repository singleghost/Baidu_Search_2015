2015百度搜索大赛django框架

-------------------------------------------------
settings.py中的ALLOWED_HOSTS = ['127.0.0.1']可能需要改一下
当debug改为false,ALLOWED_HOSTS = ['127.0.0.1']的时候,在本机浏览器上运行127.0.0.1:8000时
图片无法加载,404 216错误
-------------------------------------------------
python manage.py runserver运行该框架
浏览器输入127.0.0.1:8000/为大赛主页
/admin	后台管理界面
/competion	比赛界面
----------------------------------------------
home            主页模块
competition     比赛网页模块
login           登录模块
register        注册模块
questions       题目模块
score_query     成绩查询模块
templates       网页模板(html文件)

-------------------------------------------
templates文件夹下
about.html      大赛介绍网页
competition     比赛网页
home.html       主页
register_form.html  报名网页
rule.html       规则介绍网页
query.html	成绩查询网页
base.html	模板
404.html	出错界面
500.html	出错界面
gameover.html	暂时不用
----------------------------------------------
数据库文件  db.sqlite3

---------------------------------------------
static文件夹存放静态文件CSS,IMAGE,JS等

---------------------------------------------
剩余问题:
考虑队伍注册后能自动向邮箱发送一封包含账号和密码的email
,尚未实现
电子图片题
答对一定题目后会出现纸质图片题的提示
题目答案允许多样化,允许多一些助词
------------------------------------------------
在<head>标签内加入{% load static files %}
表示载入静态文件.
元素属性引用静态文件方法(jpg\js\css等)例如<body background="{% static "images/baidu_home.jpg/" %}">
相对路径对应的绝对路径为/baidu_search_2015/static/images/baidu_home.jpg
