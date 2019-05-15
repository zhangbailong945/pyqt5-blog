from PyQt5.QtCore import Qt,QPropertyAnimation,pyqtProperty
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtGui import QPainter,QPixmap,QPainterPath,QImage
import sys

class RotateLabel(QLabel):

    STARTVALUE=0 #起始旋转角度
    ENDVALUE=360 #结束旋转角度
    DURATION=540 #动画完成总时间

    def __init__(self,*args,image='',**kwargs):
        super(RotateLabel,self).__init__(*args,**kwargs)
        self.setCursor(Qt.PointingHandCursor)
        self._angle=0 #角度
        self._image='' #图片路径
        self._pixmap=None #图片对象
        self.setStyleSheet('background-color:white')
        self.resize(90,90)

        #属性动画
        self._animation=QPropertyAnimation(self,b'angle',self)
        self._animation.setLoopCount(1) #循环一次
        self.setPixmap(image)
    
    def mousePressEvent(self,event):
        self._animation.stop()
        cv = self._animation.currentValue() or self.STARTVALUE
        self._animation.setDuration(self.DURATION if cv == 0 else int(
            cv / self.ENDVALUE * self.DURATION))
        self._animation.setStartValue(cv)
        self._animation.setEndValue(self.ENDVALUE)
        self._animation.start()
        print(1111)
    
    def leaveEvent(self,event):
        """鼠标离开事件"""
        # 旋转动画
        self._animation.stop()
        cv = self._animation.currentValue() or self.ENDVALUE
        self._animation.setDuration(int(cv / self.ENDVALUE * self.DURATION))
        self._animation.setStartValue(cv)
        self._animation.setEndValue(self.STARTVALUE)
        self._animation.start()
        print(22222)
    
    @pyqtProperty(int)
    def angle(self):
        return self._angle
    
    @angle.setter
    def angle(self, value):
        self._angle = value
        self.update()
    
    





if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=QWidget()
    w.resize(400,400)
    layout=QVBoxLayout(w)
    mypixmap=QPixmap('F:/pyqt5projects/pyqt5-blog/resources/images/logo.png')
    label1=RotateLabel(image=mypixmap)
    label1.resize(90,90)
    layout.addWidget(label1)
    w.setLayout(layout)
    w.show()
    sys.exit(app.exec_())
    
