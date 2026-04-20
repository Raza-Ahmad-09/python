# its a blank form
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def full_name(self):
#         return f"{self.brand} {self.model}"
        
#Inherited Class

# class Electric_Car(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

# my_tesla = Electric_Car("Tesla", "Cybertruck", "85 kwh")
# print(my_tesla.full_name(), my_tesla.battery_size)

# this is value insertion

# my_car = Car("Toyota","Grande")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Honda","City")
# print(my_new_car.brand)
# print(my_new_car.model)




# Encapsulation 

class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # By using double underscore, we encapsulate the attributes
        self.model = model
    
    def get_brand(self):    # so we create a getter
        return self.__brand + " !"
    

    def full_name(self):
        return f"{self.brand} {self.model}"
    
pak_car = Car("Suzuki","Alto")
# print(pak_car.__brand)
# print(pak_car.get_brand())


## Polymorphism






## From github profile 

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod # in static method no self used (Decorators)
    def general_description():
        return "Cars are means of transport"
    
    @property # property decorators
    def model(self):
        return self.__model
    


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type():
        return "Electric charge"


# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.__brand)
# print(my_tesla.fuel_type())

# my_car = Car("Tata", "Safari")
# my_car.model = "City"
# Car("Tata", "Nexon")


# print(my_car.general_description())
# print(Car.general_description()) # will give output for the static function
# print(my_car.model)


# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)



class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())