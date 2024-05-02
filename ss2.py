def ss2(n,s):
    a=str(n)[::1]
    k=len(a)
    r1=0
    for i in range(0,len(a)):


         if int(a[i])>=s:
            return print('Цифры в числе не могут быть >=', s)
         else:
            #k=k-1
        #x=int(a[i])
        #y=x*s**k

            r1=r1+int(a[i])*s**(k-1)
        #r1=r1+y
       #else:

    return r1
#s=int(input('Введите систему счисления '))
#n=input('Введите число ')
#r=ss2(n,s)
#print(r)
