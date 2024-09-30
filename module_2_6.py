import random

number = random.randint(3, 20)

print('------------------------------')
password = "Пароль: "
print(f'Выпало число: {number}')
for i in range(1, number):
    for j in range(i, number):
        if number % (i + j) == 0:
            if str(j) == str(i):
                continue
            password = password + str(i) + str(j)

print(password)