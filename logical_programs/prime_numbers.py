# prime numbers

def prime_numbers(num):
    print("The number you entered = ", num)
    is_prime = True  # assume it's prime
    
    if num <= 1:
        is_prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

    if is_prime:
        print("It is a prime number")
    else:   
        print("It is not a prime number")

prime_numbers(13)









