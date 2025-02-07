from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import QFont
from batch_file_renamer import RenameFileApp


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
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



    def rename_file_btn_clicked(self):
        print("按钮<重命名使者>被点击了")
        self.rename_file = RenameFileApp()
        self.rename_file.show()

