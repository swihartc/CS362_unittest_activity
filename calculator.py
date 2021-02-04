
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        return None

    



if __name__ == "__main__":
    while 1:
        try:
            x = float(input("Enter x: "))
            y = float(input("Enter y: "))
            break
        except:
            print("Enter numbers...\n")
            continue

    print("x + y = ",add(x,y))
    print("x - y = ",sub(x,y))
    print("x * y = ",mult(x,y))
    print("x / y = ",div(x,y))