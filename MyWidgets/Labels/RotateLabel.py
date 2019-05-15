from PyQt5.QtCore import Qt,QPropertyAnimation
from PyQt5.QtWidgets import QApplicatin,QWidget,QLabel,QSytleOptinl,QVBoxLayout
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

        #属性动画
        self._animation=QPropertyAnimation(self,b'angle',self)
        self._animation.setLoopCount(1) #循环一次
        self.setPixmap(image)
    
    def mouseMoveEvent(self):
        self._animation.stop()
        cv = self._animation.currentValue() or self.STARTVALUE
        self._animation.setDuration(self.DURATION if cv == 0 else int(
            cv / self.ENDVALUE * self.DURATION))
        self._animation.setStartValue(cv)
        self._animation.setEndValue(self.ENDVALUE)
        self._animation.start()
    
    def leaveEvent(self, _):
        """鼠标离开事件"""
        # 旋转动画
        self._animation.stop()
        cv = self._animation.currentValue() or self.ENDVALUE
        self._animation.setDuration(int(cv / self.ENDVALUE * self.DURATION))
        self._animation.setStartValue(cv)
        self._animation.setEndValue(self.STARTVALUE)
        self._animation.start()




if __name__ == "__main__":
    app=QApplicatin(sys.argv)
    w=QWidget()
    layout=
    
