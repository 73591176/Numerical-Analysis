import math
def eq(x):
    return math.exp(-x)-x
def deq(x):
    return -math.exp(-x)-1
d=float(input("Enter 1 for per_error or 2 for iteration: "))
if d==1:
    per=float(input('Enter the percentage error: '))
    x0=float(input('Enter 1 st initial Value: '))
    for i in range(100):
        xr=x0-(eq(x0)/deq(x0))
        print(f'x[{i+1}]:',xr,"  Per_error: ",abs((xr-x0)/xr)*100)
        if abs((xr-x0)/xr)*100<=per:
            print("Final Ans: ",xr)
            break
        x0=xr
if d==2:
    itr=int(input("Enter number of iteration: "))
    x0=float(input('Enter 1 st initial Value: '))
    for i in range(itr):
        xr=x0-(eq(x0)/deq(x0))
        print(f'x[{i+1}]:',xr,"  Per_error: ",abs((xr-x0)/xr)*100)
        x0=xr
    print("Final Ans: ",xr)


        



    
