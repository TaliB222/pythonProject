import random
y = random.randint(0,4)

def choose_num(y):
    count=3
    while count>0:
        x = int(input('Enter a number: '))
        if x==y:
            print("You won!")
            break
        else:
            if x>y:
                print("Your num is big. Try again...")

            elif x<y:
                print("Your num is small. Try again...")

    count-=1


choose_num(y)