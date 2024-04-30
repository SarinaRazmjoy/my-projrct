import random
p = input("play ? y/n : ")

if p == "y" :
    def Roll():
        return random.randint(1, 6)


    user_score = 0
    computer_score = 0

    while True:
        user = Roll() + Roll()
        computer = Roll() + Roll()
        print(f"user:{user}")
        print(f"computer:{computer}")

        if user > computer:
            print("you win!")
            user_score += 1
            print(f"user score:{user_score}")
            print(f"computer score: {computer_score}")
        elif user == computer:
            print("no body won!")
            print(f"user score:{user_score}")
            print(f"computer score: {computer_score}")
        else:
            print("you lose!")
            computer_score += 1
            print(f"user score:{user_score}")
            print(f"computer score: {computer_score}")

        x = input("rematch?y/n")
        if x == "y":
            continue
        else:

            break
