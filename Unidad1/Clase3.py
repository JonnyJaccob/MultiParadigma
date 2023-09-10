#Diccionario
#parecido con json 
#llave-valor
#indexadas, no ordenadas

dic = {"Nombre":"Rocio","Edad":20,"Promedio":10.0}
dic = {
    "Nombre":"Rocio",
    "Edad":20,
    "Promedio":10.0
    }

print(dic["Nombre"])
dic = dict([("Nombre","Rocio"),("Edad",20),("Promedio",10.0)])
print(dic["Nombre"])

dic["Nacionalidad"] = "Mexicana"
print(dic["Nacionalidad"])

dic["Edad"]=25
print(dic["Edad"])

for d in dic:
    print(d)

for d in dic:
    print(dic[d])

for k,v in dic.items():
    print(k,v)

print(dic.items())
li = list(dic.items())
print(li)

print(dic["Nombre"])
print(dic.get("Nombre")) # si no existe regreesa un nulo 
print(dic.get("Nombre","No existe nombre")) # regresa un texto predeterminado 
# nulo en python es none 
print(dic.keys())
print(list(dic.keys()))
print(list(dic.values()))
print(dic.clear())
print(dic)

print(dic.pop("Nombre"))
print(dic.popitem())
#Bloques de codigo

a = 5
if a ==5:
    print("5")
else:
    print(a)

if a==5:
    print("5")
elif a ==6:
    print("6")
else:
    print(a)

#if a and a, a or a, b not b:
x = 10
if x==10:print;print(x+10);

print("Es 5" if x == 5 else "No es 5") 

c = 10 if x == 5 else 0
print(c)

##For 
cadena = "Python"
for c in cadena:
    print(c)

for i in range(0,100):
    print(i)

tupla = ((0,1),(2,3),(4,5))

for i in tupla:
    print(i)

for i in tupla:
    for j in i:
        print(j)

#pass
#codigo que ignore 
#cuerpos de codigos vacios 

for x in range(0,100):
    if(x==10):
        break
    print(x)

#continua la interacion - continue
#rompe el ciclo - break
for x in range(0,100):
    if(x % 2 == 0): #numeros pares
        break
    print(x)

# set
s = {3,4,4,5,6,1,2,2}
s.add(9)
s[1] = 4
# print(s) #da error