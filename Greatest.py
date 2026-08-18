a=int(input("Enter Number1"))
b=int(input("Enter Number2"))
c=int(input("Enter Number3"))
if((a>=b)or(a>=c)):
  print('%d is greater number',a)
elif((b>=a)or(b>=c)):
  print('%d is greater number',b)
else:
  print('%d is greater number',c)
