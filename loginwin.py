#!user/bin/env python3
__author__ = "Tooraj_Jahangiri"
__email__ = "toorajjahangiri@gmail.com"

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from typing import Callable
from os import path as ipath
from sys import exit as s_exit
from sys import argv as s_argv

__dir__ = ipath.expanduser(ipath.dirname(__file__))     # Get Directory Name

"""\
Sample Login Window:
    use pyqt5 library

UserName and Password Default is 'admin'
For Change You Need Make a Function or Class [Callable::Type] get User and Password and Handle return True or False [bool::Type]
    Example: 
        user_pass_check = lambda x, y = True if x == "admin" adn y == hash(x) else False
        
        # x = username, y = password
        # then you must connect to 'USER_CHECK' variable
        
        USER_CHECK = user_pass_check
        
    # check line 52+    validation  and  line 130+    authenticate func 
        
If you Need Check user you can use 'authenticated' signal from 'LoginWindow' class
    Example:
        if __name__ = "__main__":
            app = qtw.QApplication(sys.argv)
            w = LoginWindow()
            username = authenticated
            sys.exit(app.exec_())
        
    # check line 122+   signal's

Link Font: https://www.jetbrains.com/lp/mono/

Link Github_repo: https://github.com/Class-Tooraj/sample_login_window

"""


def __logged_in_check_default(user: str, password: str) -> bool:
    # Code Import User & Password
    _user = "admin"
    _password = hash(_user) ^ hash("EnoTe")
    hashed_password = hash(password) ^ hash("EnoTe")
    if user == _user and hashed_password == _password:
        return True
    else:
        return False


# Usable Function Default 'admin' -> __logged_in_check_default(user, password)
USER_CHECK: Callable = __logged_in_check_default


class LoginWindow(qtw.QWidget):

    # Custom signal
    authenticated = qtc.pyqtSignal(str)     # Custom Signal string 'UserName'

    def __init__(self, *args, **kwargs) -> None:
        super(LoginWindow, self).__init__(*args, **kwargs)
        # Code Start

        # Initialize Font
        font = qtg.QFont()
        font.setFamily(u"JetBrainsMono")    # Font Link https://www.jetbrains.com/lp/mono/
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(60)

        self.setFixedSize(300, 150)     # Fixed Size Window

        # Make Label's
        self.username_lable = qtw.QLabel("UserName :")
        self.username_lable.setFont(font)

        self.password_lable = qtw.QLabel("Password  :")
        self.password_lable.setFont(font)

        # Make LineEdit's / Input Text
        self.username_input = qtw.QLineEdit()
        self.username_input.setFont(font)
        self.username_input.focusWidget()     # Set Focus To username input

        self.password_input = qtw.QLineEdit()
        self.password_input.setFont(font)
        self.password_input.setEchoMode(qtw.QLineEdit.Password)     # Set To Password Mode

        # Make Button's
        self.cancel_button = qtw.QPushButton('Cancel')
        self.cancel_button.setFont(font)

        self.submit_button = qtw.QPushButton('Login')
        self.submit_button.setFont(font)

        # Make Main - Box Vertical Layout
        layout = qtw.QVBoxLayout()

        # Make UserName Box Horizontal Layout
        username_layout = qtw.QHBoxLayout()
        username_layout.addWidget(self.username_lable)
        username_layout.addWidget(self.username_input)

        layout.addLayout(username_layout)   # Add UserName Layout To Main Layout

        # Make Password Box Horizontal Layout
        password_layout = qtw.QHBoxLayout()
        password_layout.addWidget(self.password_lable)
        password_layout.addWidget(self.password_input)

        layout.addLayout(password_layout)   # Add Password Layout To Main Layout

        # Make Button's Box Horizontal Layout
        button_layout = qtw.QHBoxLayout()
        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)     # Add Button's Layout To Main Layout

        self.setLayout(layout)     # Set To Layout

        # Signal's
        self.cancel_button.clicked.connect(self.close)
        self.submit_button.clicked.connect(self.authenticate)
        self.authenticated.connect(self.clean_input)

        # Code End
        self.show()     # Show LoginWindow

    def authenticate(self) -> bool:

        username: str = self.username_input.text()
        password: str = self.password_input.text()
        user_access: bool = USER_CHECK(username, password)

        if user_access:
            self.authenticated.emit(username)    # Send Signal To authenticated
            qtw.QMessageBox.information(self, "Logged in", f"{username}, logged in.")
            return True

        else:
            qtw.QMessageBox.critical(self, "Failed", "Your UserName or Password is incorrect.")
            return False


if __name__ == "__main__":
    app = qtw.QApplication(s_argv)
    w = LoginWindow()
    s_exit(app.exec_())
