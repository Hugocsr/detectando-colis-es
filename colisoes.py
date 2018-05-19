entrada1 = input()
entrada2 = input()
entrada1 = entrada1.split(' ')
entrada2 = entrada2.split(' ')
lista2 = []
for i in entrada1:
    k = int(i)
    lista2.append(k)
for i in entrada2:
    k = int(i)
    lista2.append(k)

if (lista2[2]<lista2[4]) or (lista2[6]<lista2[0]) or (lista2[3]<lista2[5]) or (lista2[7]<lista2[1]) or (lista2[0]>lista2[6]) or (lista2[4]>lista2[2]) or (lista2[1]>lista2[7]) or (lista2[5]>lista2[3]):
    print('0')
else:
    print('1')
