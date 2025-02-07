import os
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMessageBox


class RenameFileApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("文件名批量修改工具")


        layout = QVBoxLayout()



        # 选择文件夹相关部件
        folder_path_layout = QHBoxLayout()
        self.folder_path_label = QLabel("选择文件夹：")
        self.folder_path_label.setStyleSheet("color: #333; font-size: 14px;")
        self.folder_path_entry = QLineEdit()
        self.folder_path_entry.setFixedWidth(300)
        self.folder_path_entry.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 3px;
                padding: 2px 5px;
            }
        """)
        self.browse_button = QPushButton("浏览")
        self.browse_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 3px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.browse_button.clicked.connect(self.browse_folder)

        folder_path_layout.addWidget(self.folder_path_label)
        folder_path_layout.addWidget(self.folder_path_entry)
        folder_path_layout.addWidget(self.browse_button)
        layout.addLayout(folder_path_layout)

        # 文件名前缀输入部件
        prefix_layout = QHBoxLayout()
        self.prefix_label = QLabel("文件名前缀：")
        self.prefix_label.setStyleSheet("color: #333; font-size: 14px;")
        self.prefix_entry = QLineEdit()
        self.prefix_entry.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 3px;
                padding: 2px 5px;
            }
        """)
        prefix_layout.addWidget(self.prefix_label)
        prefix_layout.addWidget(self.prefix_entry)
        layout.addLayout(prefix_layout)

        # 文件名后缀输入部件
        suffix_layout = QHBoxLayout()
        self.suffix_label = QLabel("文件名后缀：")
        self.suffix_label.setStyleSheet("color: #333; font-size: 14px;")
        self.suffix_entry = QLineEdit()
        self.suffix_entry.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 3px;
                padding: 2px 5px;
            }
        """)
        suffix_layout.addWidget(self.suffix_label)
        suffix_layout.addWidget(self.suffix_entry)
        layout.addLayout(suffix_layout)

        # 查找字符输入部件
        char_to_find_layout = QHBoxLayout()
        self.char_to_find_label = QLabel("查找字符：")
        self.char_to_find_label.setStyleSheet("color: #333; font-size: 14px;")
        self.char_to_find_entry = QLineEdit()
        self.char_to_find_entry.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 3px;
                padding: 2px 5px;
            }
        """)
        char_to_find_layout.addWidget(self.char_to_find_label)
        char_to_find_layout.addWidget(self.char_to_find_entry)
        layout.addLayout(char_to_find_layout)

        # 替换字符输入部件
        replace_char_layout = QHBoxLayout()
        self.replace_char_label = QLabel("替换字符：")
        self.replace_char_label.setStyleSheet("color: #333; font-size: 14px;")
        self.replace_char_entry = QLineEdit()
        self.replace_char_entry.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 3px;
                padding: 2px 5px;
            }
        """)
        replace_char_layout.addWidget(self.replace_char_label)
        replace_char_layout.addWidget(self.replace_char_entry)
        layout.addLayout(replace_char_layout)

        # 作者和Github信息文本
        author_font = QFont("楷体", 11)
        self.author_label = QLabel("Author：xueyao.me@gmail.com")
        self.author_label.setFont(author_font)
        self.author_label.setStyleSheet("color: #007BFF;")
        self.github_label = QLabel("Github：https://github.com/flowstone/FsPySide6Project")
        self.github_label.setFont(author_font)
        self.github_label.setStyleSheet("color: #007BFF;")

        info_layout = QVBoxLayout()
        info_layout.addWidget(self.author_label)
        info_layout.addWidget(self.github_label)
        layout.addLayout(info_layout)

        # 操作按钮
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("开始修改")
        self.start_button.setStyleSheet("""
            QPushButton {
                background-color: #008CBA;
                color: white;
                border-radius: 3px;
                padding: 5px 15px;
            }
            QPushButton:hover {
                background-color: #007B9A;
            }
        """)
        self.start_button.clicked.connect(self.start_operation)
        self.exit_button = QPushButton("退出")
        self.exit_button.setStyleSheet("""
            QPushButton {
                background-color: #F44336;
                color: white;
                border-radius: 3px;
                padding: 5px 15px;
            }
            QPushButton:hover {
                background-color: #D32F2F;
            }
        """)
        self.exit_button.clicked.connect(self.close)

        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.exit_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def browse_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹")
        self.folder_path_entry.setText(folder_path)



    def start_operation(self):
        folder_path = self.folder_path_entry.text()
        prefix = self.prefix_entry.text()
        suffix = self.suffix_entry.text()
        char_to_find = self.char_to_find_entry.text()
        replace_char = self.replace_char_entry.text()
        if folder_path:
            self.rename_files(folder_path, prefix, suffix, char_to_find, replace_char)
            QMessageBox.information(self, "提示", "批量文件名修改完成！")
        else:
            QMessageBox.warning(self, "警告", "请选择要修改的文件夹！")

    # 修改文件名
    def rename_files(self, folder_path, prefix, suffix, char_to_find, replace_char):
        # 遍历文件夹下的文件名
        for filename in os.listdir(folder_path):
            old_path = os.path.join(folder_path, filename)
            # 判断是否是文件
            if os.path.isfile(old_path):
                new_filename = f"{prefix}{filename}{suffix}"
                # 判断是否需要进行文件替换操作
                if char_to_find and replace_char:
                    # 替换字符
                    new_filename = new_filename.replace(char_to_find, replace_char)
                new_path = os.path.join(folder_path, new_filename)
                os.rename(old_path, new_path)

