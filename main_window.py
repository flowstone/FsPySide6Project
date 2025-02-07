import sys

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSystemTrayIcon, QMenu
from PySide6.QtGui import QFont, QIcon, QAction

from app_mini import FloatingBall
from batch_file_renamer import RenameFileApp


class MainWindow(QWidget):
    def __init__(self, tray_icon_visible=False):
        super().__init__()
        # 悬浮球可见状态，false可以创建悬浮球，反之。。。
        self.is_floating_ball_visible = False
        # 任务栏托盘标志位，False没有创建  True已创建
        self.is_tray_icon_visible = tray_icon_visible
        self.floating_ball = FloatingBall(self)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("PyQt示例应用")
        self.setGeometry(100, 100, 300, 250)
        self.setStyleSheet("background-color: #F5F5F5;")  # 设置窗口背景色为淡灰色


        layout = QVBoxLayout()


        # 重命名使者
        rename_file_btn = QPushButton("重命名使者")
        rename_file_btn.setFont(QFont('Arial', 14))
        rename_file_btn.setStyleSheet("""
            QPushButton {
                background-color: #9C27B0;
                color: white;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #8E24AA;
            }
        """)
        rename_file_btn.clicked.connect(self.rename_file_btn_clicked)
        layout.addWidget(rename_file_btn)

        self.setLayout(layout)

        # 处理窗口关闭事件，使其最小化到托盘
        self.closeEvent = self.handle_close_event

        # 创建系统托盘图标
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('resources/app_tray.ico'))  # 这里需要一个名为icon.png的图标文件，可以替换为真实路径
        self.tray_icon.activated.connect(self.tray_icon_activated)

        # 创建托盘菜单
        tray_menu = QMenu()
        show_action = QAction("主界面", self)
        show_action.triggered.connect(self.tray_menu_show_main)
        quit_action = QAction("退出", self)
        quit_action.triggered.connect(sys.exit)
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)

    # 从托盘菜单点击显示窗口
    def tray_menu_show_main(self):
        self.show()
        # 悬浮球退出
        if self.is_floating_ball_visible:
            self.floating_ball.close()
            self.is_floating_ball_visible = False

    # 处理窗口关闭事件
    def handle_close_event(self, event):

        event.ignore()
        self.hide()

        if not self.is_tray_icon_visible:
            self.tray_icon.show()
            self.is_tray_icon_visible = True

        if not self.is_floating_ball_visible:
            self.create_floating_ball()


    def create_floating_ball(self):
        self.floating_ball.show()
        self.is_floating_ball_visible = True

    # 双击托盘，打开窗口
    def tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self.show()
            # 悬浮球退出
            if self.is_floating_ball_visible:
                self.floating_ball.close()
                self.is_floating_ball_visible = False

    def rename_file_btn_clicked(self):
        print("按钮<重命名使者>被点击了")
        self.rename_file = RenameFileApp()
        self.rename_file.show()

