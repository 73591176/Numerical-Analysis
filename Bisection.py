import math
def eq(x):
    return -0.6*x**2+2.4*x+5.5
d=int(input("Enter 1 for pr_error or 2 for Iteration: "))
if d==1:
    per=float(input("Enter the Percentage Value: "))
    xl=float(input("Enter the value of xl: "))
    xu=float(input("Enter the value of xu: "))
    print("itr   xl       xu        xr     f(xl)     f(xu)     f(xr)     Pr_Error")
    for i in range(100):
        xr=(xu+xl)/2
        pre=abs((xu-xl)/(xu+xl)*100)
        print(i+1," %.5f"%xl," %.5f"%xu," %.5f"%xr," %.5f"%eq(xl)," %.5f"%eq(xu)," %.5f"%eq(xr)," %.5f"%pre)
        if eq(xl)*eq(xr)<0:
            xu=xr
        else:
            xl=xr
        if pre<=per:
            break
    print("Final Ans: ",xr)
else:
    n=int(input("Enter number of iteration: "))
    xl=float(input("Enter the value of xl: "))
    xu=float(input("Enter the value of xu: "))
    print("itr   xl       xu        xr     f(xl)     f(xu)     f(xr)     Pr_Error")

    for i in range(n):
        xr=(xu+xl)/2
        pre=abs((xu-xl)/(xu+xl)*100)
        print(i+1," %.5f"%xl," %.5f"%xu," %.5f"%xr," %.5f"%eq(xl)," %.5f"%eq(xu)," %.5f"%eq(xr)," %.5f"%pre)
        if eq(xl)*eq(xr)<0:
            xu=xr
        else:
            xl=xr
    print("Final Ans: ",xr)
