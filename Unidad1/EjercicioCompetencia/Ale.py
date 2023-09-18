try:
    n = int(input('teclea el valor de N: '))
    m = int(input('teclea el valor de M: '))
    lst = []
    lst.append(n)
    if n > m and m != 1 and n != 1:
        while True:
            if n/m > 1:

                t = int(n/m)
                lst.append(t)
                n = t
            elif n/m == 1:
                t = int(n/m)
                lst.append(t)
                print(lst)
                
                break
            else:
                print('secuencia invalida')
                break
    else:
       # print("No debe ser mayor o 1")
        print("Debe ser un numero entero o mayor o menor a 0 o diferente a 1")

except Exception as a:
     print("Debe ser un numero entero o mayor o menor a 0")