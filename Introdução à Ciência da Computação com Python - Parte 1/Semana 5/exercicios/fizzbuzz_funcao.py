def por3(n):
    return n % 3 == 0

def por5(n):
    return n % 5 == 0

def fizzbuzz(n):
    if por3(n) and not por5(n):
        return "Fizz"
    elif not por3(n) and por5(n):
        return "Buzz"
    elif por3(n) and por5(n):
        return "FizzBuzz"
    else:
        return n

fizzbuzz(int(input()))