# main.py
import sys
from PyQt5 import QtWidgets
from kelimeislemcisi import Ui_MainWindow
from PyQt5.QtGui import QFont
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Sayfa yönetimi için liste ve sayaç
        self.pages = [""]
        self.current_page = 0

        # Butonları bağla
        self.ui.pushButton.clicked.connect(self.copy_text)
        self.ui.pushButton_2.clicked.connect(self.paste_text)
        self.ui.pushButton_3.clicked.connect(self.cut_text)
        self.ui.pushButton_4.clicked.connect(self.add_blank_page)
        self.ui.pushButton_5.clicked.connect(self.save_file)
        self.ui.pushButton_7.clicked.connect(self.make_bold)
        self.ui.pushButton_8.clicked.connect(self.make_italic)
        self.ui.pushButton_9.clicked.connect(self.make_underline)
        self.ui.pushButton_10.clicked.connect(self.next_page)
        self.ui.pushButton_11.clicked.connect(self.previous_page)
        self.ui.fontComboBox.currentFontChanged.connect(self.set_font)
        self.ui.spinBox.valueChanged.connect(self.set_font_size)

        # Başlangıç font boyutu
        self.ui.spinBox.setValue(12)

    def copy_text(self):
        self.ui.textEdit.copy()

    def cut_text(self):
        self.ui.textEdit.cut()

    def paste_text(self):
        self.ui.textEdit.paste()

    def save_file(self):
        text = self.ui.textEdit.toPlainText()
        options = QtWidgets.QFileDialog.Options()
        path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Dosya Kaydet", "", "Text Files (*.txt);;All Files (*)", options=options)
        if path:
            with open(path, "w", encoding="utf-8") as file:
                file.write(text)

    def make_bold(self):
        fmt = self.ui.textEdit.currentCharFormat()
        fmt.setFontWeight(QFont.Bold if fmt.fontWeight() != QFont.Bold else QFont.Normal)
        self.ui.textEdit.setCurrentCharFormat(fmt)

    def make_italic(self):
        fmt = self.ui.textEdit.currentCharFormat()
        fmt.setFontItalic(not fmt.fontItalic())
        self.ui.textEdit.setCurrentCharFormat(fmt)

    def make_underline(self):
        fmt = self.ui.textEdit.currentCharFormat()
        fmt.setFontUnderline(not fmt.fontUnderline())
        self.ui.textEdit.setCurrentCharFormat(fmt)

    def set_font(self, font):
        fmt = self.ui.textEdit.currentCharFormat()
        fmt.setFont(font)
        self.ui.textEdit.setCurrentCharFormat(fmt)

    def set_font_size(self, size):
        fmt = self.ui.textEdit.currentCharFormat()
        fmt.setFontPointSize(size)
        self.ui.textEdit.setCurrentCharFormat(fmt)

    def add_blank_page(self):
        self.pages[self.current_page] = self.ui.textEdit.toPlainText()
        self.pages.append("")
        self.current_page += 1
        self.ui.textEdit.clear()

    def next_page(self):
        if self.current_page < len(self.pages) - 1:
            self.pages[self.current_page] = self.ui.textEdit.toPlainText()
            self.current_page += 1
            self.ui.textEdit.setPlainText(self.pages[self.current_page])

    def previous_page(self):
        if self.current_page > 0:
            self.pages[self.current_page] = self.ui.textEdit.toPlainText()
            self.current_page -= 1
            self.ui.textEdit.setPlainText(self.pages[self.current_page])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
