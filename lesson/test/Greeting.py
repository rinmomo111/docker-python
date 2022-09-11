from tkinter import Y


print("Good morning")

print("Good afternoon")

print("Good evening")

a = 10
b = 1
bool01 = (a > b)
print(bool01)
print(type(bool01))

a = ["sato", "suzuki"],["takahashi","tanaka"]
print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])

x = 8
y = 3
print(x == 3 or y == 3)
print(x == 1 or y == 1)

x = 8
y = 12
z = 20
x += 10
z += y
print(x)
print(z)

age = 0
if age >= 20:
    print("adult")
elif age == 0:
    print("baby")
else:
    print("child")

for i in range(3):
    for j in range(3):
        print(i, j, sep="-")
        # print(i, j)

arr = [2, 4, 6, 8, 10]
sum = 0
for i in arr:
    sum += i
print(sum)



