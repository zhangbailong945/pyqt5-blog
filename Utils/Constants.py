#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   CommonUtil.py
@Time    :   2019/05/15 11:00:53
@Author  :   Loach 
@Version :   1.0
@Contact :   1207549344@qq.com
@License :   (C)Copyright 2017-2019, loachblog.com
@Desc    :   共用工具
'''
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFont,QFontDatabase
import sys,os


class Constants(object):
    
    def __init__(self,*args,**kwargs):
        super(Constants,self).__init__(*args,**kwargs)
        self.path=os.path.abspath(os.path.dirname(os.path.dirname(__file__))).replace('\\','/')
        self.myLogo=self.initLogo()

    
    
    
    def initLogo(self):
        """
        初始化logo
        """
        return self.path+'/Resources/Images/logo.png'
        
    def initTbHeader(self):
        return """
 
<!DOCTYPE html>
<html lang="zh-CN">

<head>

    <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
    <script>
        (adsbygoogle = window.adsbygoogle || []).push({
        google_ad_client: "ca-pub-7462113579725650",
        enable_page_level_ads: true
        });
    </script>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    
    
<title>LoachBlog</title>
<meta name="description" content="LoachBlog个人笔记,程序笔记,python笔记">
<meta name="keywords" content="首页,LoachBlog,LoachBlog个人笔记">

    <meta name="HandheldFriendly" content="True">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="/static/blog/favicon.ico">
    <link rel="stylesheet" href="/static/blog/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/blog/css/font-awesome.min.css">
    <link rel="stylesheet" type="text/css" href="/static/blog/css/screen.css">

    <!--live2d-->
    <link rel="stylesheet" type="text/css" href="/static/blog/live2d/css/live2d.css">

    <script type="text/javascript" src="/static/blog/js/jquery.min.js"></script>
    <script type="text/javascript" src="/static/blog/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="/static/blog/js/jquery-1.7.2.min.js"></script>
    <!--引入时间轴js和css-->
    <link rel="stylesheet" href="/static/blog/dates/css/timeline.css">
    <script type="text/javascript" src="/static/blog/dates/js/modernizr.js"></script>
    <!--火箭-->
    <script type="text/javascript" src="/static/blog/js/data.js"></script>
    <!--鼠标点击爱心-->
    <script type="text/javascript" src="/static/blog/js/love.js"></script>

    <!--live2d 二次元-->
    <script>
    var message_Path = "/static/blog/live2d/";//资源目录，如果目录不对请更改
    var talkAPI = "/tuling/";//如果有类似图灵机器人的聊天接口请填写接口路径
    </script>
    <script type="text/javascript" src="/static/blog/live2d/js/live2d.js"></script>
    <script type="text/javascript">
    $.ajaxSetup({
        data: {csrfmiddlewaretoken: 'vnIDXb5Wfnvw674KfRgS1WWDZAbIJphs9x7pVPajRHN58NHiXnB3dlNbjE7xAXad' },
    });
    </script>
    <script type="text/javascript" src="/static/blog/live2d/js/message.js"></script>
    <link href="https://cdn.bootcss.com/aplayer/1.10.1/APlayer.min.css" rel="stylesheet">




    
    

    
    

    <!-- 代码样式-->
    
    

</head>


<body class="home-template">
        """
    
    def initTbBody(self,other):
        return """
 <!-- start site's main content area -->
    <section class="content-wrap">
        <div class="container">
            <div class="row">

                <main class="col-md-8 main-content">
                %s
                </main>
            </div>
        </div>
    </section>
        """ %other
    
    def initTbFooter(self):
        return """
</body>
</html>
        """
        

