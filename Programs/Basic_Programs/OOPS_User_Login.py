# User Login System

import hashlib               # used to encrypt password

class User:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = self.__encrypt(password)      #Private and encrypted
        self.__isLogin = False
        self.__login_attempts = 0
        self.__max_attempts = 3

    # __ makes it private → cannot be called from outside, 
    # Converts password → secure hash (one-way encryption)

    def __encrypt(self, password):
        return hashlib.sha256(password.encode()).hexdigest()  # e.g "mypass123" → "a7f3c9e2b1..."  (64 char hash)

    def login(self, password):
        if self.__login_attempts >= self.__max_attempts:
            print(f"Account Locked for {self.username}")
            print(f"Too many failed attempts...")
            return
        
        if self.__isLogin:     # If user is already login
            print(f"{self.username} is already Login...")

        if self.__encrypt(password) == self.__password:
            self.__isLogin = True
            self.__login_attempts = 1
            print(f"{self.username} logged in successfully...")
        else:
            self.__login_attempts += 1
            remaining = self.__max_attempts - self.__login_attempts
            print(f"Wrong Password for {self.username}...")

            if remaining > 0:
                print(f"Attempts remaining = {self.__login_attempts}")
            else:
                print("Account is now LOCKED...")
    
    def logout(self):
        if not self.__isLogin:
            print(f"{self.username} is not Logged in...")
        else:
            self.__isLogin = False
            print(f"{self.username} logged out successfully...")

user1 = User("Devendra",   "dev@gmail.com",  "dev@123")
user1.login("dev@123")                    # ✅ Correct password
user1.logout() 
user1.login("dev@1234")                    # ⚠️  Wrong Password

        

