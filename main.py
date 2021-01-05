def fizz_it_up():
    num = input("Let's count to... : ");
    num = int(num);
    for i in range(0, num+1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz");
        elif i % 3 == 0:
            print("Fizz");
        else:
            print(i);


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fizz_it_up();

