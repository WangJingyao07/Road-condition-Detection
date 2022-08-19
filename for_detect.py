# coding:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import sys
import qtawesome
import cv2


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    # 事件函数（绑定控件）
    def start(self):
        self.cap = cv2.VideoCapture(0)
        self.timer.timeout.connect(self.capPicture)
        x, frame = self.cap.read()
        cv2.imshow("camera", frame)

    def stop(self):
        exit(0)

    def showDialog1(self):
        # 鼠标选择文件
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)

    def clear_box(self):
        self.textEdit.setText(' ')

    def init_ui(self):
        # 主窗口
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        self.left_widget = QtWidgets.QWidget()
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()
        self.left_widget.setLayout(self.left_layout)

        self.right_widget = QtWidgets.QWidget()
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)
        self.setCentralWidget(self.main_widget)

        # 左侧按钮
        self.left_close = QtWidgets.QPushButton("")
        self.left_visit = QtWidgets.QPushButton("")
        self.left_mini = QtWidgets.QPushButton("")

        self.left_label_1 = QtWidgets.QPushButton("运行")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("运行结果")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("使用说明")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "开始")
        self.left_button_1.setObjectName('left_button')
        # self.left_button_1.clicked.connect()  # 括号内为按钮绑定的事件，与主要算法部分结合即可
        self.textEdit = QTextEdit()
        self.right_layout.addWidget(self.textEdit, 0, 1, 4, 7)
        self.left_button_1.clicked.connect(self.start)

        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "暂停")
        self.left_button_2.setObjectName('left_button')
        self.left_button_2.clicked.connect(self.stop)

        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "结束")
        self.left_button_3.setObjectName('left_button')
        self.left_button_3.clicked.connect(self.stop)

        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.home', color='white'), "本次结果")
        self.left_button_4.setObjectName('left_button')
        self.textEdit = QTextEdit()
        self.right_layout.addWidget(self.textEdit, 5, 0, 3, 9)
        self.left_button_4.clicked.connect(self.showDialog1)

        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.home', color='white'), "上一次")
        self.left_button_5.setObjectName('left_button')
        self.textEdit = QTextEdit()
        self.right_layout.addWidget(self.textEdit, 5, 0, 3, 9)
        self.left_button_5.clicked.connect(self.showDialog1)

        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.home', color='white'), "清空")
        self.left_button_6.setObjectName('left_button')
        self.textEdit = QTextEdit()
        self.right_layout.addWidget(self.textEdit, 5, 0, 3, 9)
        self.left_button_6.clicked.connect(self.clear_box)

        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "超能陆战队")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "关于我们")
        # self.left_button_8.setObjectName('left_button')
        # self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "超能陆战队")
        # self.left_button_9.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 12, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        # 右侧运行窗口
        self.right_recommend_label = QtWidgets.QLabel("运行窗口")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        # self.recommend_button_1 = QtWidgets.QToolButton()
        # self.recommend_button_1.setText("实时窗口")  # API调用实时运行界面
        # self.recommend_button_1.setIcon(QtGui.QIcon('./5.jpg'))  # 设置按钮图标
        # self.recommend_button_1.setIconSize(QtCore.QSize(350, 300))  # 设置图标大小
        # self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文

        # self.right_recommend_layout.addWidget(self.recommend_button_1, 0, 0)

        self.right_layout.addWidget(self.right_recommend_label, 0, 0, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)

        # 右侧输出窗口标题
        self.right_playlist_lable = QtWidgets.QLabel("输出结果")
        self.right_playlist_lable.setObjectName('right_lable')

        self.right_playlist_widget = QtWidgets.QWidget()
        self.right_playlist_layout = QtWidgets.QGridLayout()
        self.right_playlist_widget.setLayout(self.right_playlist_layout)

        '''
        label = QtWidgets.QLabel(self)
        label.resize(200, 100)
        '''

        self.right_layout.addWidget(self.right_playlist_lable, 4, 0, 1, 4)
        self.right_layout.addWidget(self.right_playlist_widget, 5, 0, 1, 4)

        # 美化装饰
        self.left_close.setFixedSize(15, 15)
        self.left_visit.setFixedSize(15, 15)
        self.left_mini.setFixedSize(15, 15)

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.right_recommend_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')
        self.right_playlist_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')

        self.setWindowOpacity(0.9)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
