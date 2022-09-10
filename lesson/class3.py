# クラスの頭文字は大文字
class Person:
    # 初期設定
    def __init__(self, name, nationality, age):
        self.name = name
        self.nationality = nationality
        self.age = age
    def __call__(self, name):
        print(f'{name}さん、こんにちは。私は{self.name}です。call関数から呼び出されています')
    def say_hello(self, name):
        # name 引数　self.name インスタンスの変数
        print(f'{name}さん、こんにちは。私は{self.name}です。')
imanishi = Person(name='今西', nationality='日本', age=26)
print(imanishi.name)
print(imanishi.nationality)
print(imanishi.age)
mike = Person('マイク','アメリカ',23)
print(mike.name)
print(mike.nationality)
print(mike.age)

imanishi.say_hello(name='佐藤')
mike.say_hello('鈴木')

# call 関数   インスタンス名(引数)
print('call')
imanishi(name='佐藤')

