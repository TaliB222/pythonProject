import random
y = random.randint(0,3)
x = int(input('Enter a number: '))
def choose_num(x, y):
    while x==y:
        print("You won!")
        break
        if x>y or x<y:
            print("Try again...")
            x=int(input("Enter a number:"))
        continue




choose_num(x, y)
