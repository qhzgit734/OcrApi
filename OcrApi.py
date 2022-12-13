# 导入内置库
import sys
import time
import requests
import re
import configparser
import os.path
import subprocess

# 导入第三方库
from PySide6.QtCore import QUrl, QCoreApplication
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon, Qt, QDesktopServices
from aip import AipOcr

# 导入.py文件
from qt_for_python import main, window_h, window_v, window_set

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
# 函数-截图
def capture():
    cb = QApplication.clipboard()
    cb.clear()
    '''
    global img_name_str
    img_name_str = "grab_clipboard.png"
    # QQ邮箱
    # os.system('RUNDLL32.EXE .\\lib\\TXGYMailCamera.dll CameraSubArea')
    # 微信
    # os.system('RUNDLL32.EXE .\\lib\\PrScrn.dll PrScrn')
    # QQ拼音
    # os.system('.\\lib\\SnapShot.exe')
    os.system('.\\lib\\QQPYSnapshot.exe')

    if cb.mimeData().hasImage():
        qt_img = cb.image()
        pil_img = Image.fromqimage(qt_img)  # 转换为PIL图像
        pil_img.save(img_name_str)
    else: 
        return False
    '''
    # textshot.py
    # 打包后python.exe位置有问题，导致textshot.py无法运行,故不用这个方法
    '''
    path = os.path.dirname(os.path.abspath(__file__))
    filepath = path + '\\' + 'lib\\textshot.py'
    
    subprocess.call(['python.exe', filepath],
                         shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    '''
    # 用pyinstaller -D打包，先打包ocr_api_V2.0.py，再打包tepyxtshot.py，
    # dist文件夹中textshot生成文件复制替换到ocr_api_V2.0文件夹中
    if os.path.isfile('.\\textshot.exe'):
        subprocess.call('.\\textshot.exe', 
                        shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        subprocess.call(['python.exe', '.\\lib\\textshot.py'], 
                        shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
    if cb.mimeData().hasImage():
        return True
    else: 
        return False
    
# 函数-OCR识别 
def processImage():
    global tmp_res, tmp_res1, download_url, img_name_str
    interface_name = mainwindow.root_ui.comboBox.currentText()
    img_name_str = "grab_clipboard.png"
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

        # 截图报错判断
        if capture() != False:
            if netConnect() == True:
                try:
                    processImage()
                    self.printResult()
                    print('INFO: 已识别')
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
        else:
            warn_str = "INFO: 截图为空！请重新截图！"
            print(warn_str)
            mainwindow.root_ui.textBrowser.setPlainText(warn_str)

        mainwindow.root.showNormal()
        
    def printResult(self):
        interface_name = self.root_ui.comboBox.currentText()
        mainwindow.root_ui.textBrowser.clear()
        
        if interface_name != '表格文字识别（异步接口）':
            for i in range(len(tmp_res)):
                self.root_ui.textBrowser.append(tmp_res[i])
        else:
            self.root_ui.textBrowser.append('转换excel下载地址：' + '\n' + download_url)
            # QDesktopServices.openUrl(QUrl(download_url))

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
        global client
        APP_ID_str = self.win_ui.lineEdit_app_id.text()
        API_KEY_str = self.win_ui.lineEdit_api_key.text()
        SECRET_KEY_str = self.win_ui.lineEdit_secret_key.text()

        with open('config.ini', 'w') as f:
            cf.set('aip_key_id', 'APP_ID_str', APP_ID_str)
            cf.set('aip_key_id', 'API_KEY_str', API_KEY_str)
            cf.set('aip_key_id', 'SECRET_KEY_str', SECRET_KEY_str)
            cf.write(f)
        APP_ID = APP_ID_str
        API_KEY = API_KEY_str
        SECRET_KEY = SECRET_KEY_str
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        QMessageBox.information(self.win, '提示', '设置完成！')

if __name__ == "__main__":
    # 设置全局变量
    tmp_res = []
    tmp_res1 = []
    download_url = str()
    img_name_str = str()
    APP_ID_str = str()
    API_KEY_str = str()
    SECRET_KEY_str = str()
    # 百度API
    cf = configparser.ConfigParser()
    
    if os.path.isfile('config.ini'):
            cf.read('config.ini', encoding="utf-8")
    else:
        with open('config.ini', 'w') as f:
                cf.add_section('aip_key_id') # 添加sections值
                cf.set('aip_key_id', 'APP_ID_str', '') # 在指定的sections中添加键值对
                cf.set('aip_key_id', 'API_KEY_str', '')
                cf.set('aip_key_id', 'SECRET_KEY_str', '')
                cf.write(f)
                
    APP_ID_str = cf.get('aip_key_id', 'APP_ID_str')
    API_KEY_str = cf.get('aip_key_id', 'API_KEY_str')
    SECRET_KEY_str = cf.get('aip_key_id', 'SECRET_KEY_str')
    APP_ID = APP_ID_str
    API_KEY = API_KEY_str
    SECRET_KEY = SECRET_KEY_str
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    # 类实例
    app = QApplication(sys.argv)
    mainwindow = Creat_root(main)
    dialog_v = Creat_win1(window_v)
    dialog_h = Creat_win1(window_h)
    dialog_set = Creat_win2(window_set)
    # 窗口显示
    mainwindow.root.show()
    app.setWindowIcon(QIcon('logo.ico'))
    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec())
    # pyinstaller -F -w OcrApi.py -i 'logo.ico'
    # pyinstaller -D -w OcrApi.py -i 'logo.ico'
    # pyinstaller OcrApi.spec
    # pyinstaller textshot.spec