tupla = (1,2,3)
print(type(tupla))
#tupla ordenada e inmutable y permite datos duplicados
#no se puede agregar ni quitar elementos individualmente 
print(tupla)
#print(tupla)
##tupla[0] = 5

tupla = 1,2,('a','b'),3
lista=list(tupla)
#print(tupla[2][0])
tupla = tuple(lista)
tupla = 1,2,3

lista.append(4)
#print(t)
print(tupla)
x,y,z,a = tupla
#for t in tupla:
#lo toma como int

print(tupla)
print(x,y,z,a)
#la , para segurarse de que sea una tupla
tupla=(2)
print(tupla)
print(type(tupla))

tupla=(2,)
print(tupla.count(2))
print(type(tupla))
#marca error si no encuentra el indice
tupla=(2,2,2,2,3,4,5,8)

print(tupla.index(1))
#lista
#Son para hacer test 
lista = [1,2,3,4]
lista2= list("4567")
lista3= list("4567")
lista4= list("4567")
#Lista ordenada, mutable, permite duplicados 

print(lista)
print(lista3[2][0])
print(lista2)
print(lista3[-1])
lista3 = [1,"2",["12",23,2]]
lista3[2] = 10



print(lista4[0:2])
print(lista3)

lista4 = [1,2,3,4,5,6,7]
print(lista4)
print(lista4[2:6])
lista3 += lista4
lista4[0:3] = [0,0,0]


    #print(l)
print(lista3)
for index, l in enumerate(lista3) in lista3:
    for l in lista3:
        print(index,l)
        lista1 = [1,2,3]
        lista2 = ["A","B","C"]
    #print(l1,l2)#forint
#for l1,l2 in zip(lista1,lista2):
    #for i in range(0,len(lista3)):
        #list3.append(4)
    #print(lista3[i])
#list3.insert(1,4)
list3 = [1,2,3]
list3.reverse()
list3.extend([2,1])
list3.sort(reversed=1)
list3.pop(1)
list3.sort()

#Set
#mutables e inmutables 'ala vez'
#Siempre se ordenan ascendentes y no permiten duplicados, los elimina 

set1 = {1,2,4,3}
print(set)

#set1[0] = 3
#sus elementos son inmutables 
set1.add(9)
print(set1)
#Agregar y eliminar si deja, lo que no deja es cambiarlo individualmente 

set2 = set([2,3,4,5,2,1])

lista = ["a","b","c"]
set = set([list])

for s in set2:
    print(s)

s1 = {1,3,4}
s2 = {3,5,6}
print(s1|s2) 
#union |
#interseccion ^

s1.add(1)
s1.remove(4)

#discard si no existe no hace nada
s1.discard(7)
s1.pop() #elimina al azar
s1.clear() #remueve todos los elementos 

s1.union()
s1.intersection()