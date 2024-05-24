#!/usr/bin/env python3

#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")

def square_integers(int_list):
    return [x ** 2 for x in int_list]

def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    happy_new_year()
    print(square_integers([1, 2, 3, 4, 5]))
    print(square_integers([-1, -2, -3, -4, -5]))
    fizzbuzz()