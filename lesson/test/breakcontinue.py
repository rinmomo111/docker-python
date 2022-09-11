# ループを抜ける
print('break')
for i in range(10):
    if i == 7:
        break
    print(i)

# 処理を飛ばす
print('continue')
for i in range(10):
    if i == 7:
        continue
    print(i)
    