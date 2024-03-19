from random import randint

def dados():
    d1 = randint(1,6)
    d2 = randint(1,6)
    return d1,d2

d = dados()
print("dado1 :", d[0],'', "dado2 :", d[1])

if d[0] == d[1]:
    print("Ganaste")
else:
    print("sigue intentando")

