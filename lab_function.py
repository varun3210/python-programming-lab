def ArmN(x):  #defines function
 sum=0
 t=x
 while(t>0):
  d=t%10
  sum+=d**3
  t=t//10
 if sum==x:
    return 'Armstrong Number'
 else:
    return 'Not Armstrong Number'
x=int(input('Enter Number'))
print(ArmN(x)) 

