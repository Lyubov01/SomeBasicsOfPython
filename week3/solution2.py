import os
import csv

EXT = [".jpg", ".jpeg", ".png", ".gif"]
TYPE = ["car", "truck", "spec_machine"]


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = "car"


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        self.car_type = "truck"

        try:
            if len(self.body_whl.split("x")) == 3:
                self.body_length = float(self.body_whl.split("x")[0].strip())
                self.body_width = float(self.body_whl.split("x")[1].strip())
                self.body_height = float(self.body_whl.split("x")[2].strip())
            else:
                self.body_length = 0.0
                self.body_width = 0.0
                self.body_height = 0.0

        except ValueError or IndexError:
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0

    def get_body_volume(self):
        return self.body_height * self.body_width * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = "spec_machine"


def isfloat(num):

    try:
        float(num)
    except:
        return False
    return True


def get_car_list(csv_filename):
    cars = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        try:
            for row in reader:
                if row[0] in TYPE and row[1].split() and os.path.splitext(row[3])[1] in EXT and isfloat(row[5]):
                    if row[0] == "car" and row[2].isnumeric():
                        cars.append(
                            Car(brand=row[1], passenger_seats_count=row[2], photo_file_name=row[3], carrying=row[5]))
                    elif row[0] == "spec_machine" and row[6].split():
                        cars.append(SpecMachine(brand=row[1], extra=row[6], photo_file_name=row[3], carrying=row[5]))
                    elif row[0] == "truck":
                        cars.append(Truck(brand=row[1], body_whl=row[4], photo_file_name=row[3], carrying=row[5]))
        except IndexError:
            return None

    return cars


