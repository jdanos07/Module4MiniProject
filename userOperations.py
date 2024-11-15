class User:
    # cos stands Check Out'S
    def __init__(self, name, user_id, user_cos):
       self.__name = name
       self.__user_id = user_id
       self.__user_cos = user_cos
    
    def get_name(self):
        return self.__name
    
    def get_user_id(self):
        return self.__user_id
    
    def get_user_cos(self):
        return self.__user_cos
    
def uo_main():     
    print('User Operations:')
    print('\n    1. Add New\n    2. Display Details\n    3. Display All\n')