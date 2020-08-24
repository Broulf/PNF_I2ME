# Program to check if a number is prime or not

# asks the user for an input (i.e. number)
num = int(input("Enter a number: "))

# checks if number is over 1
if num > 1:
    # check for factors of num
    for i in range(2,num):
        if (num % i) == 0:
            # says in console if the number is not a prime number
            print(num,"is not a prime number")
            # breaks down the factors of the non prime number
            print(i,"times",num//i,"is",num)
            break
    else:
        # says in console that the number is prime
        print(num,"is a prime number")

# if input is less than
# or equal to 1, it is not prime
else:
    print(num,"is not a prime number")

# https://www.programiz.com/python-programming/online-compiler/