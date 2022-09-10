class Student:

    # コンストラクタ（初期化メソッド）
    def __init__(self,name):
        self.name = "aaaa" + name

    # メソッド
    def avg(self,math,english):
        print((math + english)/2)

a001 = Student("sato")
a001.avg(30,80)
a001.name = "sato"
print(a001.name)
# print(a001.gender)

a002 = Student("tanaka")
a002.name = "tanaka"
print(a002.name)

a003 = Student("katayama")
print(a003.name)