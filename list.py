list_1=[]
n = 0 
print("lets start.\nenter b to finish ")
for x in range(5):
    x = input( f"list index {n}: ")
    if x == "b":
        break
    n += 1
    list_1.append(x)

print( f"your list is: {list_1}" )

list_s = []
list_i = []
for i in list_1 :
    if i.isnumeric() == True:
        list_s.append(i)
    else:
        list_i.append(i)


for x in range(len(list_s)):
    for m in range(x+1 , len(list_s)):
        if list_s[x] > list_s[m] :
            list_s[x] , list_s[m] = list_s[m] , list_s[x]


for x in range(len(list_i)):
    for m in range(x+1 , len(list_i)):
        if list_i[x] > list_i[m] :
            list_i[x] , list_i[m] = list_i[m] , list_i[x]


list_1 = list_i + list_s
print(f"new list is: {list_1} ")

c = 0

for y in range(len(list_1)):
 if list_1[y-1] == list_1[y-2]:
  c += 1
  del list_1[y-1]
print(list_1,f"number of repeating numbers :  {c} " )