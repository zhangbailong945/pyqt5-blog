import os,sys
from PyQt5.QtWidgets import QApplication
from MyWidgets.Do_MainLayout import Do_MainLayout


StyleSheet='''

/*标题栏面板*/
#HeaderTitlebarWidget{
    background-color: rgb(247, 155, 106);
}
/*最小化最大化关闭按钮通用默认背景*/
#pb_Skin,#pb_Maximum,#pb_Minimum,#pb_Close,#pb_Normal{
    border: none;
    background-color: rgb(247, 155, 106);
    color:white;
    font-size:14px;
    font-weight: normal;
}

/*悬停*/
#pb_Skin:hover,#pb_Maximum:hover,#pb_Minimum:hover,#pb_Normal:hover{
    background-color: rgb(247, 229, 229);
}
#pb_Close:hover {
    background-color: rgb(232, 17, 35);
}

/*鼠标按下不放*/
#pb_Skin:pressed,#pb_Skin:pressed,#pb_Minimum:pressed,#pb_Normal:pressed  {
    background-color: rgb(247, 229, 229);
}
#pb_Close:pressed {
    color: white;
    background-color: rgb(161, 73, 92);
}

/*头像logo面板*/
#HeaderImgWidget{
    background-color: rgb(161, 73, 92);
}

#hl_htw_img{
    border:none;
    width:80px;
    height:80px;
}

/*文字面板*/
#HeaderTextWidget{
    background-color: rgb(247, 155, 106);
}

#lb_HeaderText1{
    font-size:30px;
    font-weight:bold;
    color:white;
}

#lb_HeaderText2{
    font-size:30px;
    font-weight:bold;
    color:black;

}

/*菜单面板*/
#HeaderMenuWidget{
    background-color: rgb(255, 255, 255);
}

#pb_Index,#pb_Category,#pb_DateTime,#pb_Tags,#pb_About{
    border:none;
    color:rgb(80,80,80);
}

#pb_Index:hover,#pb_Category:hover,#pb_DateTime:hover,#pb_Tags:hover,#pb_About:hover{
    border:none;
    color:rgb(247, 155, 106);
}

#pb_Index:checked,#pb_Category:checked,#pb_DateTime:checked,#pb_Tags:checked,#pb_About:checked{
    border-bottom:2px solid rgb(247, 155, 106);
}

/*内容面板*/
#centerWidget{
    background-color: rgb(233, 240, 245);
}

/*笔记列表面板*/
#LeftPostWidget{
    background-color: rgb(255, 255, 255);
}


/*登录面板*/
#RightLoginWidget{
    background-color: rgb(255, 255, 255);
}

#lb_Login_Title{
    font-weight:bold;
}


/*版权面板*/
#label_BottomCopyRight_Line{
    margin-right:4px;
}

#label_BottomCopyright_Beian{

}

#label_BottomCopyright_Site{
    margin-right:4px;
}

#label_BottomCopyright_Copyright{
    margin-right:4px;
}

'''

if __name__ == "__main__":
    app=QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    w=Do_MainLayout()
    w.show()
    sys.exit(app.exec_())