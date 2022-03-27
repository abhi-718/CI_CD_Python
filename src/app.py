


def add(a,b):
    return a + b


def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def power(a,b):
    return a ** b

def divide(a,b):
    try:
        return a // b
    except:
        raise Exception("divide by 0")

if __name__ == "__main__":
    print(add(4,5))

