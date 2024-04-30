
print("fibonacci number: " )
fi = [0, 1, 1, 3]

a=1
b=3
for i in range(1000):
    new = a + b
    a = b
    b = new
    fi.append(new)

print(fi)