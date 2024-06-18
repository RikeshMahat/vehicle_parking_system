from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from helper import current_time
import re

@dataclass
class Brand:
    brand: str

@dataclass
class Wheel:
    wheel: int

@dataclass
class ParkTime:
    checkout: datetime = field(default=None)
    checkin: datetime = field(default=current_time())

    def get_total_park_time(self):
        time_difference = self.checkout - self.checkin
        days = time_difference.days
        hours = time_difference.seconds // 3600
        minutes = (time_difference.seconds % 3600) // 60

        if days > 0:
            return f'{days} Days, {hours} hours, {minutes} minutes'

        if hours > 0:
            return f'{hours} Hours, {minutes} minutes'

        else:
            return f'{minutes} minutes'

    def get_minutes(self):
        minutes = (self.checkout - self.checkin).total_seconds() // 60
        return minutes


class VehicleAbstract(ABC):
    def __init__(self, brand, wheel, park_time, vehicle_type):
        self.brand = brand
        self.wheel = Wheel(wheel)
        self.park_time = park_time
        self.vehicle_type = vehicle_type

    @abstractmethod
    def set_reg_no(self, value):
        pass

    @abstractmethod
    def get_reg_no(self):
        pass

    @staticmethod
    @abstractmethod
    def validate_reg_no(reg_no):
        pass


# inherit the vehicle class
class Vehicle(VehicleAbstract):

    def __init__(self, brand, wheel, park_time, vehicle_type):
        super().__init__(brand, wheel, park_time, vehicle_type)
        self.__reg_no = ''
        self.__price_incurred = 0

    def set_reg_no(self, value):
        if self.validate_reg_no(value):
            self.__reg_no = value
        else:
            raise ValueError('Invalid Reg No')

    def get_reg_no(self):
        return self.__reg_no

    def get_price_incurred(self, price):
        total_minutes = self.park_time.get_minutes()
        if total_minutes < 30:
            self.__price_incurred = price

        else:
            if total_minutes % 30 > 10:
                self.__price_incurred = total_minutes / 30 * price
            else:
                self.__price_incurred = total_minutes // 30 * price

        return self.__price_incurred

    def __dict__(self):
        data = {self.get_reg_no(): {
            'brand': self.brand.brand.upper(),
            'wheel': self.wheel.wheel,
            'vehicle_type' : self.vehicle_type,
            'reg_no': self.get_reg_no(),
            'check_in': str(self.park_time.checkin),
            'check_out': ''
        }}
        return data

    @staticmethod
    def validate_reg_no(reg_no):
        pattern = r'^[a-zA-Z]{1}\s[a-zA-Z]{2}\s[0-9]{4}$'  # format (B AC 1256)
        return bool(re.search(pattern, reg_no))


class TwoWheeler(Vehicle):
    def __init__(self, brand, park_time):
        wheel = 2
        vehicle_type = 'two wheeler'
        super().__init__(brand=brand, wheel=wheel, park_time=park_time, vehicle_type=vehicle_type)

    def get_price_incurred(self, price=15):
        result = super().get_price_incurred(price)
        return result


class FourWheeler(Vehicle):
    def __init__(self, brand, park_time):
        wheel = 4
        vehicle_type = 'four wheeler'
        super().__init__(brand=brand, wheel=wheel, park_time=park_time, vehicle_type=vehicle_type)

    def get_price_incurred(self, price=25):
        result = super().get_price_incurred(price)
        return result



class VehicleDeserializer:
    @staticmethod
    def deserialize_vehicle(vehicle_attributes):

        # deserialize the json datetime to python datetime
        try:
            vehicle = None

            # brand and wheel
            brand = Brand(vehicle_attributes.get('brand'))

            time_format = '%Y-%m-%d %H:%M:%S.%f'
            check_in = datetime.strptime(vehicle_attributes.get('check_in'), time_format)
            check_out = datetime.strptime(vehicle_attributes.get('check_out'), time_format)
            time = ParkTime(checkin=check_in, checkout=check_out)

            # create an instance of the vehicle based on type and return it
            vehicle_type = vehicle_attributes.get('vehicle_type')

            if vehicle_type == 'four wheeler':
                vehicle = FourWheeler(brand=brand, park_time=time)
            elif vehicle_type == 'two wheeler':
                vehicle = TwoWheeler(brand=brand, park_time=time)
            vehicle.set_reg_no(vehicle_attributes.get('reg_no'))
            return vehicle
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)










