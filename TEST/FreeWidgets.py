# 导入模块
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QBitmap, QPainter, QPen, QBrush, QColor
from PyQt6.QtCore import Qt

# 创建一个悬浮球类，继承自QWidget
class FloatingBall(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口标志，使其无边框、无按钮、无任务栏
        self.setWindowFlags(Qt.WindowType.Tool | Qt.WindowType.FramelessWindowHint)
        # 设置窗口大小和位置
        self.resize(100, 100)
        self.move(300, 300)
        # 设置窗口背景透明
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # 设置窗口可拖动
        self.setMouseTracking(True)
        self.draggable = False
        self.offset = None

    # 重写绘图事件，绘制一个圆形的悬浮球
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        pen = QPen(Qt.GlobalColor.black)
        pen.setWidth(2)
        painter.setPen(pen)
        brush = QBrush(Qt.GlobalColor.red)
        painter.setBrush(brush)
        painter.drawEllipse(0, 0, 100, 100)

    # 重写鼠标按下事件，记录鼠标位置和窗口位置的偏移量
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.draggable = True
            self.offset = event.pos()

    # 重写鼠标移动事件，根据偏移量移动窗口位置
    def mouseMoveEvent(self, event):
        if self.draggable:
            x = event.globalX()
            y = event.globalY()
            x_w = self.offset.x()
            y_w = self.offset.y()
            self.move(x - x_w, y - y_w)

    # 重写鼠标释放事件，停止拖动
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.draggable = False

# 创建应用程序对象和悬浮球对象
app = QApplication([])
ball = FloatingBall()
# 显示悬浮球
ball.show()
# 运行应用程序
app.exec()
