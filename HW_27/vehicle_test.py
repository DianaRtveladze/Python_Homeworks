from vehicle import Vehicle, ElectricVehicle


def test_vehicle_initialization():
    vehicle = Vehicle("Toyota", "Camry", 2020)
    assert vehicle.brand == "Toyota"
    assert vehicle.model == "Camry"
    assert vehicle.year == 2020
    assert vehicle.gaz_tank_size == 45
    assert vehicle.fuel_level == 0


def test_vehicle_fuel_up():
    vehicle = Vehicle("Toyota", "Camry", 2020)
    assert vehicle.fuel_up == "Gas tank is empty and can not move."
    vehicle.fuel_level = 20
    assert vehicle.fuel_up == "Gas tank is now full or can move."


def test_vehicle_drive():
    vehicle = Vehicle("Toyota", "Camry", 2020)
    assert vehicle.drive == "The Camry is now driving."


def test_electric_vehicle_initialization():
    e_vehicle = ElectricVehicle("Tesla", "Model S", 2022)
    assert e_vehicle.brand == "Tesla"
    assert e_vehicle.model == "Model S"
    assert e_vehicle.year == 2022
    assert e_vehicle.battery_size == 85
    assert e_vehicle.charge_level == 0


def test_electric_vehicle_charge():
    e_vehicle = ElectricVehicle("Tesla", "Model S", 2022)
    assert e_vehicle.charge == "The vehicle is now charged."


def test_electric_vehicle_fuel_up():
    e_vehicle = ElectricVehicle("Tesla", "Model S", 2022)
    assert e_vehicle.fuel_up == "This vehicle has no fuel tank!"
