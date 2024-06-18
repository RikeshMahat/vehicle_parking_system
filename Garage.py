# imports
from handle_json import JsonHandler
from Vehicle import TwoWheeler, FourWheeler, VehicleDeserializer, Vehicle
from helper import current_time, formatted_result
from receipt_email import send_receipt_email
class Garage:

    def __init__(self):
        self.all_vehicles = {}  # empty list of vehicles
        self.parked_vehicles = {}
    def load_vehicles_from_json(self):

        '''
        load all vehicles from json file
        :return: None
        '''
        data = JsonHandler.read_json()
        if data is not None:
            self.all_vehicles = data

    def park_vehicles(self, vehicle):

        '''

        :param vehicle:
        :return: message
        '''

        self.load_vehicles_from_json()
        self.all_vehicles.update(vehicle.__dict__())
        JsonHandler.write_json(json_data=self.all_vehicles)
        return 'vehicle has been parked'

    @send_receipt_email
    def remove_vehicles(self):

        '''
        :param reg_no:
        :return: message
        '''
        self.load_vehicles_from_json()
        reg_no = input('Please enter your vehicle registration number (B AA 1245) : ').upper()

        if not Vehicle.validate_reg_no(reg_no):
            return 'Invalid registration number'

        if reg_no in self.all_vehicles.keys():
            vehicle = self.all_vehicles[reg_no]
            vehicle['check_out'] = str(current_time())

            self.all_vehicles.update({reg_no: vehicle})
            JsonHandler.write_json(json_data=self.all_vehicles)

            # deserialize back to vehicle instance and show park time details
            new_vehicle = VehicleDeserializer.deserialize_vehicle(vehicle)
            self.show_park_time_details(new_vehicle)
            return new_vehicle
        return 'Sorry no vehicle with such registration number'

    def show_parked_vehicles(self):
        self.load_vehicles_from_json()

        if self.all_vehicles:
            for key, value in self.all_vehicles.items():
                if value['check_out'] == '':
                    self.parked_vehicles.update({key : value})

            if self.parked_vehicles:
                return self.parked_vehicles

        return 'Sorry no vehicles parked in garage'

    def show_all_vehicles(self):
        self.load_vehicles_from_json()
        if self.all_vehicles:
            return self.all_vehicles
        return 'Sorry no vehicles record present'


    def show_park_time_details(self, vehicle):

        print('======================')
        print(f'vehicle {vehicle.brand.brand} - {vehicle.get_reg_no()}')
        print(f'CheckIn - {vehicle.park_time.checkin} | checkout - {vehicle.park_time.checkout}')
        print(f'Parked For : {vehicle.park_time.get_total_park_time()}')
        print(f'Price : Rs {vehicle.get_price_incurred()}')
        print('vehicle Removed from Parking Spot ')
        print('======================')




