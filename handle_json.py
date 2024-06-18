from os import path
import json
from enum import Enum


class File(Enum):
    RECORDS_FILE_NAME = 'garage.json'
class JsonHandler:
    @staticmethod
    def write_json(json_data, filename=File.RECORDS_FILE_NAME.value):

        """

        :param filename:
        :param json_data:
        :return: None
        """
        data = JsonHandler.read_json(filename)
        if data:
            data.update(json_data)
        else:
            data = json_data

        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4, separators=(', ', ': '))
        except Exception as e:
            print(f'error occurred : {e}')




    @staticmethod
    def read_json(filename=File.RECORDS_FILE_NAME.value):

        """

        :param filename:
        :return: data
        :return None
        """
        filename = JsonHandler.check_or_create_file(filename)
        with open(filename) as file:
            data = file.read().strip()
            if data:
                return json.loads(data)
            return None

    @staticmethod
    def check_or_create_file(filename: str):

        """
         creates file if it doesn't exist and returns the filename
        :param filename:
        :return: filename
        """
        if path.exists(filename):
            if path.isfile(filename):
                return filename

        with open(filename, 'w') as file:
            _, name = path.split(path.realpath(filename))
            return name





