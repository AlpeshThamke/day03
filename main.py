#This is 

from auth_code import *
from conve import *

temp_user = ["alpesh"]
temp_pwd = ["alpesh"]

def start_ssh():
    trials = 3
    while trials:
        trials-=1
        print("Enter User_id")
        key = input()
        #key = temp_user
        if (type(key) is str) == False:
            raise TypeError("Only string values can be used for user_id")
        print("Enter password")
        print("Password:")
        password = input()
        #password = temp_pwd
        if (type(password) is str) == False: 
            raise TypeError("Only string values can be used for passwords")
        if auth(key,password):
            print("Connection Successful")
            if conversation()==False:
                print("session terminated")
                break
        else:
            print("Bad Credentials")
            print(trials,"trials remainig")

if __name__ == '__main__':
    start_ssh()


