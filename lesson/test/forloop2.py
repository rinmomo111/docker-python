# zip 関数
# 複数のリスト要素をまとめて処理

last_names = ['今西','佐藤','鈴木','田中']
first_names = ['航平','健介','康二','康介']

print('1')
print(last_names[0] + first_names[0] + 'さん')
print(last_names[1] + first_names[1] + 'さん')
print(last_names[2] + first_names[2] + 'さん')
print(last_names[3] + first_names[3] + 'さん')

print('2')
for i in range(len(last_names)):
    print(last_names[i] + first_names[i] + 'さん')

# zip
print('3')
for last_names, first_names in zip(last_names, first_names):
    print(last_names + first_names + 'さん')

