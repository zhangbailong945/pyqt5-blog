from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog,QApplication



class MoveDialog(QDialog):
    
    def __init__(self,*args,**kwargs):
        super(MoveDialog,self).__init__(*args,**kwargs)
        self._pos=None
        self._rect=QApplication.instance().desktop().availableGeometry(self)
    
    def mousePressEvent(self,event):
        super(MoveDialog,self).mousePressEvent(event)
        if event.button()==Qt.LeftButton:
            self._pos=event.pos()
    
    def mouseReleaseEvent(self,event):
        super(MoveDialog,self).mouseReleaseEvent(event)
        self._pos=None
        y=self.qBound(0,self.y(),self._rect.height()-int(2*self.height()/3))
        self.move(self.x(),y)
    
    def mouseMoveEvent(self,event):
        super(MoveDialog,self).mouseMoveEvent(event)
        if not self._pos:
            return
        
        if self.isMaximized() or self.isFullScreen():
            return
        
        pos=event.pos()-self._pos
        x=self.x()+pos.x()
        y=self.y()+pos.y()
        self.move(x,y)
    
    def qBound(self,miv, cv, mxv):
        return max(min(cv, mxv), miv)
'''
if __name__ == "__main__":
    import sys
    app=QApplication(sys.argv)
    w=MoveDialog()
    w.show()
    sys.exit(app.exec_())
'''