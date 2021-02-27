class Value:
    def __init__(self, amount=0):
        self.amount = amount

    def __get__(self, obj, obj_type):
        return self.amount * (1 - obj.commission)

    def __set__(self, obj, amount):
        self.amount = amount


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


if __name__ == '__main__':
    new_account = Account(0.1)
    new_account.amount = 100

    print(new_account.amount)
