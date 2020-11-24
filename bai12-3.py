import random
list1 = []
n = random.randint(50, 100)
for i in range(n):
    def chuoi(dodai):
        kytu = 'abcdefghijklmnopqrstuvwxyz '
        return ''.join(random.choice(kytu) for i in range(dodai))
    chuoi = chuoi(random.randint(1, 100))
    age = random.randint(1, 150)
    dic = {'name': chuoi, 'age': age}
    list1.append(dic)
print(list1)