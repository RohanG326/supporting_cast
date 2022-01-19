import random


def isPrime(num):
    if num > 1:
        for i in range(2 , num//2):
            if(num % i) == 0:
                return "not Prime"
        return "Prime"

def OddEven(num):
    for n in range(0,100):
        if num % 2 == 0:
            return "Even"
        return "Odd"

def CheckNum():
    num = random.randint(2,100)
    if(num % 2) == 0:
            print(num, "is Even")
            return True
    else:
        if num > 1:
            for i in range(2 , num//2):
                if(num % i) == 0:
                    print(num, "is Odd")
                    return True
            print(num, "is Odd and Prime")
            return True

if __name__ == "__main__":
    print(CheckNum())