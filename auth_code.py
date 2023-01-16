#This code checks the authentication 

users = {"alpesh":"1234","arjun":"abcd",}


def auth(key,password):
        """checks for correct key and password
        args:
            key and password, both should be of type string
        return:
            bool value
        """
        try:
            temp_pwd=users[key]
            if temp_pwd == password:
                print("Username and Passwords Matched")
                return True
            else:
                return False
        except KeyError:
            print("This user does not exist")
            return False

if __name__ == "__main__":
    auth(key,password)
