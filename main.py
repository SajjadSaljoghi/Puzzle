import sys
from functools import partial
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication,QMainWindow,QMessageBox
from ui_mainwindow import Ui_MainWindow
from generate_non_repeating_random_2D_list import GNRR2DL


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setFocus()
        self.buttons = [[self.ui.Button1,self.ui.Button2,self.ui.Button3,self.ui.Button4],
                        [self.ui.Button5,self.ui.Button6,self.ui.Button7,self.ui.Button8],
                        [self.ui.Button9,self.ui.Button10,self.ui.Button11,self.ui.Button12],
                        [self.ui.Button13,self.ui.Button14,self.ui.Button15,self.ui.Button16]] 
        self.gnrr2dl = GNRR2DL(4,4)
        self.numbers = self.gnrr2dl.exec()
        self.empty_row = -1
        self.empty_column = -1
        for i in range(4):
            for j in range(4):
                counter = (i * 4) + j
                self.buttons[i][j].setText(str(self.numbers[counter]))
                if self.numbers[counter] == 16:
                    self.buttons[i][j].setVisible(False)
                    self.empty_row = i
                    self.empty_column = j
                self.buttons[i][j].clicked.connect(partial(self.play,i,j))
                
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Up:
            i,j = self.check_empty()
            if (i+1) <= 3:
                self.play(i+1,j)
        elif event.key() == Qt.Key.Key_Down:
            i,j = self.check_empty()
            if (i-1) >= 0:
                self.play(i-1,j)
        elif event.key() == Qt.Key.Key_Left:
            i,j = self.check_empty()
            if (j+1) <= 3:
                self.play(i,j+1)
        elif event.key() == Qt.Key.Key_Right:
            i,j = self.check_empty()
            if (j-1) >= 0:
                self.play(i,j-1)
    
    def play(self,i ,j):
        new_text = ""
        if (i == self.empty_row and j-1 == self.empty_column) \
            or (i == self.empty_row and j+1 == self.empty_column) \
            or (i+1 == self.empty_row and j == self.empty_column) \
            or (i-1 == self.empty_row and j == self.empty_column):
            
            new_text = self.buttons[i][j].text()
            self.buttons[i][j].setVisible(False)
            self.buttons[i][j].setText("16")
            self.buttons[self.empty_row][self.empty_column].setVisible(True)
            self.buttons[self.empty_row][self.empty_column].setText(new_text)
            self.empty_row = i
            self.empty_column = j

            if self.check_win() == True:
                messageBox = QMessageBox()
                messageBox.setText("You Win 😍")
                messageBox.exec()
    
    def check_empty(self):
        for i in range(4):
            for j in range(4):
                if self.buttons[i][j].isVisible() == False:
                    return i,j

    def check_win(self):
        index = 1
        for i in range(4):
            for j in range(4):
                if int(self.buttons[i][j].text()) != index:
                    return False
                index += 1
        return True


app = QApplication(sys.argv)
mainWindow = Main()
mainWindow.show()
app.exec()


