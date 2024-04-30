import random



p = input("enter 'y' for start! ")
if p == "y" :
    while True:
        list_1 = []

        A = random.randint(1,3)
        B = random.randint(1,3)
        C = random.randint(1,3)

        list_1.append(A)
        list_1.append(B)
        list_1.append(C)        
        print(list_1)

        if list_1[0]==list_1[1] and list_1[0]==list_1[2]:
            print("jackpot")
        else:
            print("you lose")
    
        x = input("do you want to play egean?y/n ")
        if x=="y":
            continue
        else:
            break