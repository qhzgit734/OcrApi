# 导入内置库
import io
import sys
import time
import requests
import re
import linecache
import os.path
# 导入python库
from PySide2.QtCore import QBuffer, Signal, QPoint, QRect, QUrl, QCoreApplication
from PySide2.QtWidgets import QMainWindow, QWidget, QApplication, QDialog, QFileDialog, QMessageBox
from PySide2.QtGui import QIcon, Qt, QCursor, QPalette, QBrush, QPainter, QPen, QColor, QDesktopServices
from aip import AipOcr
from PIL import Image
# 导入.py文件
from qt_for_python.uic import main, window_h, window_v, window_set
# 函数-网络检查
def netConnect():
        try:
            q=requests.get("http://www.baidu.com",timeout=5)
            m=re.search(r'STATUS OK',q.text)
            if m:
                return True
            else:
                return False
        except:
            return False
# 函数-OCR接口切换
def interface_switch(fp_c):
    global tmp_res1
    interface_name = mainwindow.root_ui.comboBox.currentText()
    if interface_name == '通用文字识别（标准版）':
        tmp_res1 = client.basicGeneral(fp_c.read())
    elif interface_name == '通用文字识别（高精度版）':
        tmp_res1 = client.basicAccurate(fp_c.read())
    elif interface_name == '网络图片文字识别':
        tmp_res1 = client.webImage(fp_c.read())
    elif interface_name == '表格文字识别（异步接口）':
        tmp_res1 = client.tableRecognitionAsync(fp_c.read())
    elif interface_name == '手写文字识别':
        tmp_res1 = client.handwriting(fp_c.read())
    else:
        pass
# 函数-OCR识别 
def processImage(img):
    global tmp_res, tmp_res1, download_url
    buffer = QBuffer()
    buffer.open(QBuffer.ReadWrite)
    img.save(buffer, "PNG")
    pil_img = Image.open(io.BytesIO(buffer.data()))
    img_name_str = 'test_img.png'
    pil_img.save(img_name_str)
    buffer.close()
    interface_name = mainwindow.root_ui.comboBox.currentText()
    
    with open(img_name_str, "rb") as fp:
        interface_switch(fp)
        if interface_name != '表格文字识别（异步接口）':
            tmp_res.clear()
            tmp_res2 = tmp_res1['words_result']
            for i in range(len(tmp_res2)):
                tmp_res.append(tmp_res2[i]['words'])
        else:
            requestId = tmp_res1['result'][0]['request_id']
            exl_res = client.getTableRecognitionResult(requestId)
            while exl_res['result']['ret_msg'] != '已完成':  
                time.sleep(2)  # 暂停2秒再刷新
                exl_res = client.getTableRecognitionResult(requestId)
            download_url = exl_res['result']['result_data']

    print('INFO: 已识别')

# 类-主窗口
class Creat_root(QMainWindow):
    def __init__(self, Ui_file):
        super().__init__()
        # 创建主窗口
        self.root = QMainWindow()
        # 创建Ui_MainWindow的实例
        self.root_ui = Ui_file.Ui_MainWindow()
        # 调用setupUi在指定窗口(主窗口)中添加控件
        self.root_ui.setupUi(self.root)
        self.root_ui.action.triggered.connect(lambda: self.open_win_a(dialog_v))
        self.root_ui.actionhelp.triggered.connect(lambda: self.open_win_a(dialog_h))
        self.root_ui.actionAdvanced_settings.triggered.connect(lambda: self.open_win_a(dialog_set))
        self.root_ui.pushButton.clicked.connect(self.open_win_s)
        self.root_ui.pushButton_2.clicked.connect(self.save_file)
        self.root_ui.pushButton_2.setEnabled(False)
        self.root_ui.comboBox.currentIndexChanged.connect(self.state)
        
    def state(self):
        interface_name = self.root_ui.comboBox.currentText()
        if interface_name == '表格文字识别（异步接口）':
            self.root_ui.pushButton_2.setEnabled(True)
        else:
            self.root_ui.pushButton_2.setEnabled(False)
        
    def open_win_a(self, widget_o):
        # 新窗口
        widget_o.win.show()
        
    def open_win_s(self):
        self.root.showMinimized()
        time.sleep(0.3)
        # 新窗口
        self.snipper = Snipper()
        self.snipper.show()
        
        self.snipper.close_snipper_signal.connect(self.close_snipper_widget)
        self.snipper.send_str_signal.connect(self.printResult)
        
        self.root.showNormal()
        
    def printResult(self):
        interface_name = self.root_ui.comboBox.currentText()
        self.root_ui.textBrowser.clear()
        
        if interface_name != '表格文字识别（异步接口）':
            for i in range(len(tmp_res)):
                self.root_ui.textBrowser.append(tmp_res[i])
        else:
            self.root_ui.textBrowser.append('转换excel下载地址：' + '\n' + download_url)
            # QDesktopServices.openUrl(QUrl(download_url))
        
    def close_snipper_widget(self):
        self.snipper.close()
        
    def save_file(self):
        filePath = QFileDialog.getSaveFileName(
                            self.root,             # 父窗口对象
                            "保存文件",             # 标题
                            "test_table.xls",      # 起始目录
                            "excel类型 (*.xls)"     # 选择类型过滤项，过滤内容在括号中
                            )
        if filePath:
            with open(filePath[0], 'wb') as xls:
                if len(download_url) != 0:
                    excel_data = requests.get(download_url)
                    xls.write(excel_data.content)
                else:
                    pass
# 类-截图窗口
class Snipper(QWidget):
    # 自定义信号
    send_str_signal = Signal() 
    close_snipper_signal = Signal()
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("ocr_net")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Dialog)
        self.setWindowState(self.windowState() | Qt.WindowFullScreen)
        self.screen = QApplication.screenAt(QCursor.pos()).grabWindow(0)
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(self.screen))
        self.setPalette(palette)
        self.setCursor(QCursor(Qt.CrossCursor))
        self.start, self.end = QPoint(), QPoint()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:  # esc键退出
            self.close()
        return super().keyPressEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(0, 0, 0, 100))
        painter.drawRect(0, 0, self.width(), self.height())
        if self.start == self.end:
            return super().paintEvent(event)
        painter.setPen(QPen(QColor(255, 0, 255), 3))
        painter.setBrush(painter.background())
        painter.drawRect(QRect(self.start, self.end))
        return super().paintEvent(event)

    def mousePressEvent(self, event):
        self.start = self.end = event.pos()
        self.update()
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if self.start == self.end:
            return super().mouseReleaseEvent(event)
        shot = self.screen.copy(
                                min(self.start.x(), self.end.x()),
                                min(self.start.y(), self.end.y()),
                                abs(self.start.x() - self.end.x()),
                                abs(self.start.y() - self.end.y()),
                                )
        if netConnect() == True:
            try:
                processImage(shot)
                self.send_str_signal.emit()
            except (IndexError, RuntimeError, KeyError):
                warn_str = "INFO: 无法识别！请尝试: \
                            \n1、切换识别模式！ \
                            \n2、检查百度智能云的ID或KEY是否正确输入！"
                print(warn_str)
                mainwindow.root_ui.textBrowser.setPlainText(warn_str)
                pass
        else:
            warn_str = "INFO: 无法识别！请检查网络情况！"
            print(warn_str)
            mainwindow.root_ui.textBrowser.setPlainText(warn_str)

        self.close_snipper_signal.emit()
# 类-菜单窗口-关于
class Creat_win1(QDialog):
    def __init__(self, Ui_file):
        super().__init__()
        self.win = QDialog()
        self.win_ui = Ui_file.Ui_Dialog()
        self.win_ui.setupUi(self.win)
        self.win_ui.commandLinkButton.clicked.connect(self.open_git)
    
    def open_git(self):
        QDesktopServices.openUrl(QUrl("https://github.com/qhzgit734?tab=repositories"))
# 类-菜单窗口-设置
class Creat_win2(QDialog):
    def __init__(self, Ui_file):
        super().__init__()
        self.win = QDialog()
        self.win_ui = Ui_file.Ui_dialog()
        self.win_ui.setupUi(self.win)
        self.win_ui.pushButton.clicked.connect(self.ent_get)
        self.win_ui.commandLinkButton.clicked.connect(self.open_url)
        self.win_ui.lineEdit_app_id.setText(APP_ID_str)
        self.win_ui.lineEdit_api_key.setText(API_KEY_str)
        self.win_ui.lineEdit_secret_key.setText(SECRET_KEY_str)
        
    def open_url(self):
        QDesktopServices.openUrl(QUrl("https://login.bce.baidu.com/"))
    
    def ent_get(self):
        APP_ID_str = self.win_ui.lineEdit_app_id.text()
        API_KEY_str = self.win_ui.lineEdit_api_key.text()
        SECRET_KEY_str = self.win_ui.lineEdit_secret_key.text()

        with open('config.txt', 'w') as conf:
            conf.write(APP_ID_str + '\n' + API_KEY_str + '\n' + SECRET_KEY_str)
        QMessageBox.information(self.win, '提示', '设置完成，重启程序生效！')
if __name__ == "__main__":
    # 设置全局变量
    tmp_res = []
    tmp_res1 = []
    download_url = str()
    APP_ID_str = str()
    API_KEY_str = str()
    SECRET_KEY_str = str()
    # 百度API
    if os.path.isfile('config.txt'):
        with open('config.txt', 'r') as conf:
            APP_ID_str = linecache.getline('config.txt', 1)
            API_KEY_str= linecache.getline('config.txt', 2)
            SECRET_KEY_str = linecache.getline('config.txt', 3)
    else:
        with open('config.txt', 'w') as conf:
            APP_ID_str = linecache.getline('config.txt', 1)
            API_KEY_str= linecache.getline('config.txt', 2)
            SECRET_KEY_str = linecache.getline('config.txt', 3)
    APP_ID = APP_ID_str
    API_KEY = API_KEY_str
    SECRET_KEY = SECRET_KEY_str
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    # 类实例
    QCoreApplication.setAttribute(Qt.AA_DisableHighDpiScaling)
    app = QApplication(sys.argv)
    mainwindow = Creat_root(main)
    dialog_v = Creat_win1(window_v)
    dialog_h = Creat_win1(window_h)
    dialog_set = Creat_win2(window_set)

    # 窗口显示
    mainwindow.root.show()
    app.setWindowIcon(QIcon('logo.ico'))
    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())

'''
pyinstaller -F -w ocr_net.py -i 'logo.ico'
conda list -e > requirements.txt
conda install --yes --file requirements.txt
pip freeze > requirements.txt 可能会丢失依赖包的版本号
pip install -r requirements.txt
'''