# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'morse.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

class Ui_Code(object):
        def generateCode(self):
                selected = self.selectedCode.currentIndex() # 0 is morse code.

                if(selected ==0 ):

                        if(self.encode.isChecked()):
                                print("ENCODE Checked")
                                self.encodeMethod()
                        elif(self.decode.isChecked()):
                                print("DECODE Checked.")
                                self.decodeMethod()
                        else:
                                print("Please select encode/decode.")
                                self.outputLabel.setText("Please select encode/decode.")
                else:
                         self.outputLabel.setText(self.selectedCode.currentText())

                print(selected)
                


        def encodeMethod(self):


                encode = ["a","b","c" , "d" ,"e","f" , "g" , "h" , "i" , "j","k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" ,"w" ,"x" ,"y" , "z" , " "]
                decode = [".-" ,"-...", "-.-.", "-.." ,"." "...-.", "--.", "...." ,".." ,".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-." ,"..." ,"-", "..-" ,"...-" ,".--", "-..-", "-.--", "--.."," "]
                keys = dict(zip(encode , decode))

                encode_code = self.codeTextArea.toPlainText().encode("utf-8")
                output = " "
                for letter in encode_code:
                        if(letter!=" "):

                                output = output + " " + keys[letter]
                self.outputLabel.setText(output)
                print("Inside encode function. : " + output )

                

        

        def decodeMethod(self):
                encode = ["a","b","c" , "d" ,"e","f" , "g" , "h" , "i" , "j","k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" ,"w" ,"x" ,"y" , "z" , " "]
                decode = [".-" ,"-...", "-.-.", "-.." ,"." "...-.", "--.", "...." ,".." ,".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-." ,"..." ,"-", "..-" ,"...-" ,".--", "-..-", "-.--", "--.."," "]
                keys2 = dict(zip(decode , encode))

                flag = 0
                decode_code = self.codeTextArea.toPlainText().encode("utf-8")
                output = ""
                decode_code = decode_code.split(" ")
                print(decode_code)

                for morse in decode_code:
                        for c in decode:
                                if(c == morse):
                                        flag=1
                                        print("VALID")
                                        break
                                else:
                                        flag=0
                        if(flag==0):
                                print("Invalid character")
                                output = "Invalid character"
                                break
                        print(keys2[morse])

                        output = output +" "+ keys2[morse] 
                       
                self.outputLabel.setText(output)
                print("Inside encode function. : " + output )


                #print("Inside decode function." + decode_code)
        
        def setupUi(self, Code):
                Code.setObjectName("Code")
                Code.resize(547, 356)
                Code.setStyleSheet("")
                self.centralwidget = QtWidgets.QWidget(Code)
                self.centralwidget.setStyleSheet("background:#222629;color:#86c232;")
                self.centralwidget.setObjectName("centralwidget")
                self.selectedCode = QtWidgets.QComboBox(self.centralwidget)
                self.selectedCode.setGeometry(QtCore.QRect(50, 50, 151, 25))
                font = QtGui.QFont()
                font.setStyleStrategy(QtGui.QFont.PreferDefault)
                self.selectedCode.setFont(font)
                self.selectedCode.setFocusPolicy(QtCore.Qt.NoFocus)
                self.selectedCode.setAutoFillBackground(False)
                self.selectedCode.setStyleSheet("QComboBox {\n"
        "    border: 1px solid gray;\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 18px 1px 3px;\n"
        "    min-width: 6em;\n"
        "    \n"
        "}\n"
        "\n"
        "#selectedCode:selected{\n"
        "background:#86c232;\n"
        "color:white;\n"
        "}\n"
        "\n"
        "")
                self.selectedCode.setObjectName("selectedCode")
                self.selectedCode.addItem("")
                self.selectedCode.addItem("")
                self.selectedCode.addItem("")
                self.encode = QtWidgets.QRadioButton(self.centralwidget)
                self.encode.setGeometry(QtCore.QRect(230, 50, 116, 22))

                self.encode.setObjectName("encode")
                

                self.decode = QtWidgets.QRadioButton(self.centralwidget)
                self.decode.setGeometry(QtCore.QRect(360, 50, 116, 22))
                self.decode.setObjectName("decode")
               
                self.codeTextArea = QtWidgets.QTextEdit(self.centralwidget)
                font.setPointSize(12)
                self.codeTextArea.setFont(font)
                self.codeTextArea.setGeometry(QtCore.QRect(200, 120, 291, 51))
                self.codeTextArea.setStyleSheet("background:black;\n"
        "color:white;")
                self.codeTextArea.setObjectName("codeTextArea")
                self.codeTextViewLabel = QtWidgets.QLabel(self.centralwidget)
                self.codeTextViewLabel.setGeometry(QtCore.QRect(50, 120, 141, 41))
                font = QtGui.QFont()
                font.setPointSize(19)
                self.codeTextViewLabel.setFont(font)
                self.codeTextViewLabel.setStyleSheet("")
                self.codeTextViewLabel.setObjectName("codeTextViewLabel")
                self.generate = QtWidgets.QPushButton(self.centralwidget)
                self.generate.setGeometry(QtCore.QRect(200, 200, 161, 51))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.generate.setFont(font)
                self.generate.setStyleSheet("background:black;\n""color : white;\n""border: 4px solid black;\n""border-radius : 5px;\n""")
                self.generate.setObjectName("generate")
                self.labelforoutput = QtWidgets.QLabel(self.centralwidget)
                self.labelforoutput.setGeometry(QtCore.QRect(50, 280, 141, 41))
                font = QtGui.QFont()
                font.setPointSize(19)
                self.labelforoutput.setFont(font)
                self.labelforoutput.setStyleSheet("")
                self.labelforoutput.setObjectName("labelforoutput")
                self.outputLabel = QtWidgets.QLabel(self.centralwidget)
                self.outputLabel.setGeometry(QtCore.QRect(200, 280, 291, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.outputLabel.setFont(font)
                self.outputLabel.setStyleSheet("color:white;")
                self.outputLabel.setObjectName("outputLabel")
                self.outputLabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
                Code.setCentralWidget(self.centralwidget)

                self.generate.clicked.connect(self.generateCode)

                self.retranslateUi(Code)
                QtCore.QMetaObject.connectSlotsByName(Code)
        
        

        def retranslateUi(self, Code):
                 _translate = QtCore.QCoreApplication.translate
                 Code.setWindowTitle(_translate("Code", "MainWindow"))
                 self.selectedCode.setItemText(0, _translate("Code", "Morse Code"))
                 self.selectedCode.setItemText(1, _translate("Code", "Another code"))
                 self.selectedCode.setItemText(2, _translate("Code", "Code3"))
                 self.encode.setText(_translate("Code", "Encode"))
                 self.decode.setText(_translate("Code", "Decode"))
                 self.codeTextViewLabel.setText(_translate("Code", "Enter code"))
                 self.generate.setText(_translate("Code", "GENERATE"))
                 self.labelforoutput.setText(_translate("Code", "Output"))
                 self.outputLabel.setText(_translate("Code", "sample"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Code = QtWidgets.QMainWindow()
    ui = Ui_Code()
    ui.setupUi(Code)
    Code.show()
    sys.exit(app.exec_())
