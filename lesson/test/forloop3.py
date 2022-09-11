# enumerate 関数
# index と要素を同時に処理したい時に使用

last_names = ['今西', '佐藤', '鈴木', '田中']
first_names = ['航平', '健介', '康二', '康介']

print('1')
print('出席番号', 0, '番目の' + last_names[0] + 'さん')
print('出席番号', 1, '番目の' + last_names[1] + 'さん')
print('出席番号', 2, '番目の' + last_names[2] + 'さん')
print('出席番号', 3, '番目の' + last_names[3] + 'さん')

print('2')
for i in range(len(last_names)):
    print('出席番号', i, '番目の' + last_names[i] + 'さん')

print('3')
for i, last_name in enumerate(last_names):
    print('出席番号', i, '番目の' + last_name + 'さん')

print('4')
for i, last_name in enumerate(last_names):
    print(f'出席番号{i}番目の{last_name}さん')

print('5')

