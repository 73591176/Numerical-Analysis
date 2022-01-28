import math
def eq(x):
    return -0.6*x**2+2.4*x+5.5
choice=int(input("Enter 1 for Percentage error or 2 for Iteration : "))
if choice==1:
    per=float(input("Enter the Percentage error Value: "))
    xu=float(input("Enter the xu Value: "))
    xl=float(input("Enter the xl Value: "))
    print("Itr   xu       xl       xr     f(xu)      f(xl)     f(xr)   pr_error")
    for i in range(100):
        if (eq(xl)-eq(xu)) != 0:
            xr=xu-((eq(xu)*(xl-xu))/(eq(xl)-eq(xu)))
            if i!=0:
                pre=(abs((xr-x2)/xr)*100)
            else:
                pre=('null')
            print(i+1," %0.5f"%xu," %.5f"%xl," %.5f"%xr," %.5f"%eq(xu)," %.5f"%eq(xl)," %.5f  "%eq(xr),(str(pre) if i==0 else pre))
            if eq(xl)*eq(xr)<0:
                xu=xr
            else:
                xl=xr
            if i!=0 and (abs((xr-x2)/xr)*100)<=per:
                break
            x2=xr
        else:
            print('Operation broken due to zero division')
            break
    print("Final Ans:",xr)
else:
    n=int(input('Enter the number of iteration: '))
    xu=float(input("Enter the xu Value: "))
    xl=float(input("Enter the xl Value: "))
    print("Itr   xu       xl       xr     f(xu)      f(xl)     f(xr)   pr_error")
    x2=0
    for i in range(n):
        if (eq(xl)-eq(xu)) != 0:
            xr=xu-((eq(xu)*(xl-xu))/(eq(xl)-eq(xu)))
            if i!=0:
                pre=(abs((xr-x2)/xr)*100)
            else:
                pre=('null')            
            print(i+1," %0.5f"%xu," %.5f"%xl," %.5f"%xr," %.5f"%eq(xu)," %.5f"%eq(xl)," %.5f  "%eq(xr),(str(pre) if i==0 else pre))
            if eq(xl)*eq(xr)<0:
                xu=xr
            else:
                xl=xr 
            x2=xr
        else:
            print('Operation broken due to zero division')
            break
    print("Final Ans: ",xr)





