import random
while True:
    x = input("ramz? ")
    x = x.lower()
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
         "m", "n", "o", "p", "q", "s", "r", "t", "u", "v", "w", "x", "y", "z"," "]

    sign = ["@", "#", "$", "%", "^", "&", "*", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "11", "12", "13", "14", "15", "16", "17", "18", "19" , "'"]
    ramz = []

    c = 0
    for i in x:
        if i in alpha:
            k = alpha.index(i)
            r = random.choice(sign)
            x = x.replace(x[c], r)
            c += 1
    ramz.append(x)
            
    print(ramz)
    
    m = input("continue? y/n ")
    if m == "y":
        continue
    else:
        break
f = open("ramz4.txt", "a+")
f.write(str(ramz))
f.write(str(x))
f.close()

f = open("ramz4.txt", "r")
print(f.read())





   
