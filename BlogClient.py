import os,sys
from PyQt5.QtWidgets import QApplication
from MyWidgets.Do_MainLayout import Do_MainLayout


StyleSheet='''
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
'''

if __name__ == "__main__":
    app=QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    w=Do_MainLayout()
    w.show()
    sys.exit(app.exec_())