def check_prime(number):
    if number > 1 :
        print(f"Validate Input: {number} is greater than 1, proceed to next step.")
        print("Prime Check: ", end="")
        isPrime = True
        divsible = ""
        for i in range (1, number+1):
            if i > 1 and i!= number and number % i == 0 :
                isPrime = False
                divsible += f", {i}"


        if isPrime :
            print(f"{number} is only divisible by 1 and {number}.")
            print("is prime")
        
        else:
            print(f"{number} is divisible by 1{divsible}, {number}.")
            print("is not prime")
    else:
        print("is not prime")    




number = int(input("Enter number that greater than 1: "))
check_prime(number)
