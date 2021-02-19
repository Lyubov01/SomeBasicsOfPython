import os.path
import tempfile
import uuid


class File:

    def __init__(self, path_to_file):
        self.path = path_to_file
        if not os.path.exists(self.path):
            os.mknod(self.path)

    def read(self):
        with open(self.path, "r") as file:
            return file.read()

    def write(self, info):
        with open(self.path, "w") as file:
            file.write(info)

    def __add__(self, other):
        new_path = tempfile.gettempdir()
        new_path = os.path.join(new_path, str(uuid.uuid4()))
        obj = File(new_path)
        obj.write(self.read() + other.read())
        return obj

    def __iter__(self):
        self.curr = 0
        with open(self.path, "r") as f:
            self.lines = f.readlines()
        return self

    def __next__(self):
        try:
            line = self.lines[self.curr]
            self.curr += 1
            return line
        except IndexError:
            raise StopIteration

    def __str__(self):
        return self.path


if __name__ == '__main__':
    obj1 = File("some_filename")
    obj2 = File("some_filename_1")
    obj3 = obj1+obj2
    obj4 = obj1+obj2
    print(obj1.path)
    print(obj2.path)
    print(obj3.path)
    print(obj4.path)




