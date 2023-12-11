import time

def factor():
    numberInput = eval(input("Enter a num >2: "))
    while True:
        if numberInput > 1:
            for numbers in range(2, numberInput + 1):  # adding 1 so the end will be the same as the number inputted
                remainder = numberInput % numbers
                if remainder > 0:
                    continue
                else:
                    break
            print("The lowest factor is", numbers)
            restart()
            break
        else:
            print("Invalid input")

def numcheck(number):  #checks if a number is negative or not
    numinput = int(number)
    if numinput >= 0:
        return int(number)
    else:
        print("Please input a non-negative number")
        return None

def primecheck(firstnum, secondnum):
    print("Your prime numbers are: ", end="")
    for number in range(firstnum, secondnum):
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime and number > 1:
            print(number, end=" ")
    print("\n")
    time.sleep(1)

def prime():
    while True:
        # setting the variables to a value of None
        # Because it'll conflict if set to 0
        startRange = None
        endRange = None

        while startRange is None:
            startRange = numcheck(input("Enter a number [start]: "))
        if startRange == 0:
            restart()
            break

        while endRange is None or startRange > endRange:
            endRange = numcheck(input("Enter a number [end]: "))
            if startRange > endRange:
                print(f"Enter a number greater than {startRange}")

        primecheck(startRange, endRange + 1)

def restart():
    options = {1: factor, 2: prime, 0: exits}
    while True:
        decision = int(input("1 for Factors 2 for Prime numbers 0 Exit: "))
        if decision in options:
            options[decision]()
            break
        else:
            print("Invalid number")

def exits():
    print("Have a nice day!")

restart()