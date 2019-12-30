#check prime 


def do_calculation(number1):
    # isPrime = check_prime(number1)
    if check_prime(number1): 
        # return "It is prime number"
        index = 10
        for i in range(1, len(str(number1))):
            tmp = number1 % index
            if check_prime(tmp) == False: return "Not prime in left trunket"
            index = index * 10
        index = 10
        for i in range(1, len(str(number1))):
            tmp = number1 / index
            if check_prime(int(tmp)) == False: return "Not prime in Right trunket"
            index = index * 10
        return "It is double side prime number"
    else:
        return "Not prime number "
    

def check_prime(number1):
    if number1 > 1:
        for i in range(2, number1):
            if (number1 % i) == 0:
                return False
        else:
            return True
    # if the entered number is less than or equal to 1
    # then it is not prime number
    else:
        return False


result=do_calculation(3137)
print(result)