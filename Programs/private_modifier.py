class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # Made acc_pass as private

    def reset_pass(self):
        print(self.__acc_pass)  #acc_pass is accessible within the class

acc1 = Account("123456", "Pass@123")
print(acc1.acc_no)

#Both variables are accessible outside the class, as they are public
#For any variable to be private add "__" in that variable/method before
#sensitive data should be always private