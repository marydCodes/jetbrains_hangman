prime_ = int(input())

if prime_ <= 1:
    print("This number is not prime")
else:
    for i in range(2, prime_):
        if prime_ % i == 0:
            print("This number is not prime")
            break
    else:
        print("This number is prime")