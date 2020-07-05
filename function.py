from PyQt5.QtWidgets import QMessageBox
from question import Ui_MainWindow1
from PyQt5 import  QtWidgets
import sqlite3



class functions(QtWidgets.QMainWindow , Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self )
        self.show()
        self.right_answer = 0
        self.wrong_answer = 0
        self.con = sqlite3.connect("questions.sqlite")
        self.cur = self.con.cursor()
        self.sport_button.clicked.connect(self.category)
        self.literature_button.clicked.connect(self.category)
        self.history_button.clicked.connect(self.category)
        self.answer.clicked.connect(self.answerControl)
        self.label.setVisible(False)
        self.question.setVisible(False)
        self.option1.setVisible(False)
        self.option2.setVisible(False)
        self.option3.setVisible(False)
        self.option4.setVisible(False)
        self.A.setVisible(False)
        self.B.setVisible(False)
        self.C.setVisible(False)
        self.D.setVisible(False)
        self.answer.setVisible(False)


    def category(self):
        self.button = self.sender()
        if (self.button.text() == 'Sport'):
            self.rowid = 1
        elif (self.button.text() == 'Literature'):
            self.rowid = 5
        elif (self.button.text() == 'History'):
            self.rowid = 7
        self.questions(categoryname= self.button.text() , id = self.rowid , wronganswer = 0 , rightanswer = 0)

    def questions(self , categoryname , id , wronganswer , rightanswer):
        self.id = id
        self.label.setVisible(True)
        self.label_7.setVisible(False)
        self.sport_button.setVisible(False)
        self.literature_button.setVisible(False)
        self.history_button.setVisible(False)
        self.question.setVisible(True)
        self.option1.setVisible(True)
        self.option2.setVisible(True)
        self.option3.setVisible(True)
        self.option4.setVisible(True)
        self.A.setVisible(True)
        self.B.setVisible(True)
        self.C.setVisible(True)
        self.D.setVisible(True)
        self.answer.setVisible(True)
        self.cur.execute("Select * from question where category_name = ? and id = ? " , (categoryname.lower()  , self.id ,  ))
        self.result = self.cur.fetchall()
        if (len(self.result) > 0):
            self.label.setText('Question' + ' ' + str (self.right_answer + self.wrong_answer + 1) )
            self.question.setText(self.result[0][2])
            self.question.setStyleSheet("font: 75 19pt \"Comic Sans MS\";")
            self.option1.setText(self.result[0][3])
            self.option2.setText(self.result[0][4])
            self.option3.setText(self.result[0][5])
            self.option4.setText(self.result[0][6])
        else:
            self.message(messages = 'Right Answer :{}'.format(rightanswer) + '\n' + 'Wrong Answer : {}'.format(wronganswer) + '\n'  )


    def answerControl(self ):

        if (self.option1.isChecked()):
            if (self.option1.text() == self.result[0][7] ):
                self.right_answer += 1
                self.message(messages="Congratulations , right answer")


            else:
                self.wrong_answer += 1
                self.message(messages="Unfortunately wrong answer")


        elif (self.option2.isChecked()):
            if (self.option2.text() == self.result[0][7]):
                self.right_answer += 1
                self.message(messages="Congratulations , true answer")


            else:
                self.wrong_answer += 1
                self.message(messages="Unfortunately false answer")

        elif (self.option3.isChecked()):
            if (self.option3.text() == self.result[0][7] ):
                self.right_answer += 1
                self.message(messages="Congratulations , true answer")


            else:
                self.wrong_answer += 1
                self.message(messages="Unfortunately false answer")

        elif (self.option4.isChecked()):
            if (self.option4.text() == self.result[0][7] ):
                self.right_answer += 1
                self.message(messages="Congratulations , true answer")


            else:
                self.wrong_answer += 1
                self.message(messages="Unfortunately false answer")



    def message(self , messages ):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("Question info")
        self.msg.setText(messages)
        self.msg.exec_()
        if (len(self.result) > 0):
            self.questions(categoryname= self.button.text() , id = self.id + 1 , wronganswer = self.wrong_answer , rightanswer = self.right_answer)
        else:
            self.msg = QMessageBox.question(self, 'Continue?',
                                            'Do you want to continue the game', QMessageBox.Yes, QMessageBox.No)
            if (self.msg == QMessageBox.Yes):
                import sys
                from PyQt5.QtWidgets import QApplication


                while True:
                    app = QApplication(sys.argv)
                    function = functions()
                    app.exec()
                sys.exit()






            else:
                self.close()


