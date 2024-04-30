import random

score = 0
x = (random.randint(0 , 10))

while True :
        y = int(input("guess a number between 1 and 10 : "))

        if y == x :
                print("well done! ")
                score +=1
                print(f"your score : {score}")
                i = input("do you want to continue?y/n " )

                if i == "y" :
                        x = (random.randint(0 , 10))
                        continue
                else:

                        break

        elif y > x :
                print("it`s higher ")
                continue

        else:
                print("it`s lower ")
                continue





    


       




