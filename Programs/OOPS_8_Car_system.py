class Car:
    def __init__(self, brand, model, max_speed = 150):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed
        self.speed = 0
        self.is_running = False

    def start(self):
        if self.is_running:
            print(f"{self.brand} of {self.model} is already running...")
        else:
            self.is_running = True
            print(f"{self.brand} of {self.model} started..")
        
    def accelerate(self, increase_by):
        if not self.is_running:
            print(f"Start the car First...")
        elif self.speed + increase_by > self.max_speed:
            print(f"Cannot exceed max speed of {self.max_speed} km/h")
        else:
            self.speed += increase_by
            print(f"Accelerating ....Speed = {self.speed} km/h")

    def stop(self):
        if not self.is_running:
            print(f"Car is already stopped...")
        else:
            self.speed = 0
            self.is_running = False
            print(f"{self.brand} of {self.model} is stopped now..")
        
car1 = Car("Toyota", "Camry", 130)
car2 = Car("Tata", "Nexon", 160)

car1.start()
car1.accelerate(200)
car1.stop()

car2.start()
car2.accelerate(120)
car2.stop()


