class Calculator:
    def add(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            print('Error! The 2nd number must not be 0')
        return a / b


if __name__ == "__main__":
    print('This is main')
    cal = Calculator()
    print(cal.add(1, 2))
    print(cal.substract(1, 2))
    print(cal.multiply(1, 2))
    print(cal.divide(1, 2))
