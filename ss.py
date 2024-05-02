def ss(n,s):
      b=''
      a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
      if (n<s) and (s>=10):
       return str(a[int(n)-10])
      else:
        while n>=s:
          k=str(n%s)
          if int(k)>=10:
             b=str(a[int(k)-10])+b
             #b=y+b


          else:
               b=k+b
          n=n//s
        return str(n)+b
n=757
s=16
r=ss(n,s)
print (r)