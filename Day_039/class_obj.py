class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False  # Initially, the car is not running

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.brand} {self.model} has started.")
        else:
            print(f"{self.brand} {self.model} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} has stopped.")
        else:
            print(f"{self.brand} {self.model} is already stopped.")

# Example usage:
my_car = Car("Toyota", "Corolla")
my_car.start()  # Output: Toyota Corolla has started.
my_car.stop()   # Output: Toyota Corolla has stopped.
