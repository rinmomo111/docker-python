names = ['今西','佐藤','鈴木','高橋','川上']

print('1')
print(names[0] + 'さん')
print(names[1] + 'さん')
print(names[2] + 'さん')
print(names[3] + 'さん')
print(names[4] + 'さん')
print(' ')

print('2')
for i in range(5):
    print(names[i] + 'さん')
print(' ')

print('3')
for i in range(len(names)):
    print(names[i] + 'さん')
print(' ')

print('4')
for name in names:
    print(name + 'さん')
print(' ')
