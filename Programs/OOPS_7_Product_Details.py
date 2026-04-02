class Product:
    count = 0

    def __init__(self, name, price):             
        self.name = name
        self.price = price
        Product.count += 1        # access attributes using Class name

    def get_info(self):        # Instance methods
        print(f"price of {self.name} = {self.price}")

    @classmethod
    def get_count(cls):          # Class method. This is created to access class attributes
        print(f"Total products created are {cls.count}")

    @staticmethod
    def cal_discount(price, discount):
        print(f"discounted price = {price - (price * discount / 100)}")     #To get the discounted price

p1 = Product("Mobile", 10000)
p2 = Product("Laptop", 45000)

p1.get_info()
p1.cal_discount(p1.price, 12)
p2.get_info()
p1.cal_discount(p2.price, 20)
        