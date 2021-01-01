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

__author__ = "Tooraj_Jahangiri"