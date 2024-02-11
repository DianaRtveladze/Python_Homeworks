class Car:
    def __new__(cls, *args, **kwargs):
        instance = super(Car, cls).__new__(cls)
        return instance

    def __init__(self, brand, model, year):
        self._brand = None
        self._model = None
        self._year = None
        self.set_brand(brand)
        self.set_model(model)
        self.set_year(year)

    def set_brand(self, brand):
        if not isinstance(brand, str):
            raise ValueError("Brand must be a string.")
        self._brand = brand

    def get_brand(self):
        return self._brand

    def set_model(self, model):
        if not isinstance(model, str):
            raise ValueError("Model must be a string.")
        self._model = model

    def get_model(self):
        return self._model

    def set_year(self, year):
        if not isinstance(year, int):
            raise ValueError("Year must be an integer.")
        self._year = year

    def get_year(self):
        return self._year


car = Car(brand="Toyota", model="Camry", year=2022)
print(car.get_brand())  # Output: Toyota
print(car.get_model())  # Output: Camry
print(car.get_year())   # Output: 2022
try:
    car.set_brand(123)
except ValueError as e:
    print(e)  # Output: Brand must be a string.

try:
    car.set_year("2023")
except ValueError as e:
    print(e)  # Output: Year must be an integer.
