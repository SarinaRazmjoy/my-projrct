parentheses = input("enter a parentheses:  ")
print("your input:" , parentheses )
wrong=[]
index=[]

for i in range(len(parentheses)):
    if parentheses[i]== "(":
        wrong.append(i)
    elif parentheses[i]== ")":
        if len(wrong)>0:
            wrong.pop()
        else:
            index.append(i)
for i in wrong:
    index.append(i)

print("Wrong indexes:", index )
out=" "
for i in range(len(parentheses )):
    if i not in index and parentheses[i]!=" ":
        out+= parentheses[i]
print("right form:",out)
