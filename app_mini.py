import sys
from PySide6.QtWidgets import  QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import  QMouseEvent, QPixmap, QGuiApplication
from PySide6.QtCore import Qt, QTimer


class FloatingBall(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setStyleSheet("background-color: transparent;")
        self.main_window = main_window

        self.init_ui()

    def init_ui(self):
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)

        self.setGeometry(0, 0, 80, 80)  # 设置悬浮球大小
        self.setWindowOpacity(0.8)  # 设置透明度
        self.setup_background_image()


        self.move_to_top_right()


        self.dragPosition = None
        self.setMouseTracking(True)

        # 启动呼吸灯效果（透明度周期性变化）
        self.breathing_light_window()
    def breathing_light_window(self):
        # 初始透明度
        self.opacity = 0.2
        # 透明度每次变化的值，控制呼吸的速度和节奏
        self.direction = 0.02
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_opacity)
        # 设置定时器间隔为50毫秒，可根据需要调整呼吸节奏快慢
        self.timer.start(50)

    # 更新透明度
    def update_opacity(self):
        self.opacity += self.direction
        if self.opacity >= 1.0:
            self.direction = -0.02  # 达到最大透明度后开始减小透明度
        elif self.opacity <= 0.2:
            self.direction = 0.02  # 达到最小透明度后开始增大透明度
        self.setWindowOpacity(self.opacity)
    def setup_background_image(self):
        layout = QVBoxLayout()
        pixmap = QPixmap('resources/app_mini.ico')
        pixmap = pixmap.scaled(self.size())
        self.background_label = QLabel(self)
        self.background_label.setPixmap(pixmap)
        self.background_label.resize(self.size())
        layout.addWidget(self.background_label)
        self.setLayout(layout)

    def move_to_top_right(self):
        screen_geo = QGuiApplication.primaryScreen().geometry()
        x = screen_geo.width() - self.width() - 10
        y = 10
        self.move(x, y)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.MouseButton.LeftButton and self.dragPosition:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    # 鼠标释放
    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragPosition = None

    def show_main_window(self):
        self.main_window.show()
        self.main_window.is_floating_ball_visible = False
        self.hide()

    # 鼠标双击，打开主界面
    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.show_main_window()

