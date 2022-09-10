scores = {'国語': 30, '数学': 90, '英語': 80, '理科': 80, '社会': 70 }
print(scores)
print(scores['英語'])
scores['家庭科'] = 100
scores['体育'] = 10
print(scores)

scores.pop('体育')
print(scores)
