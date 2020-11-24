import random
def chuoi(dodai):
    kytu = 'abcdefghijklmnopqrstuvwxyz '
    return ''.join(random.choice(kytu) for i in range(dodai))
chuoi = chuoi(random.randint(1, 100))
age = random.randint(1, 150)
dic = {'name': chuoi, 'age': age}
print(dic)
