import math
def eq(x):
    return math.exp(-x)-x
choice=int(input("Enter 1 for Percentage error or 2 for Iteration : "))
if choice==1:
    per=float(input("Enter the Percentage error Value: "))
    x1=float(input("Enter 1 st initial Value: "))
    x2=float(input("Enter 2 nd initial Value: "))
    x=[x1,x2]
    print("Itr  x(i-1)     x(i)     x(i+1)    pr_error")
    for i in range(100):
        if (eq(x[i+1])-eq(x[i])) != 0:
            x.append(x[i+1]-((eq(x[i+1])*(x[i]-x[i+1]))/(eq(x[i])-eq(x[i+1]))))
            pre=(abs((x[i+2]-x[i+1])/x[i+2])*100)
            print(i+1," %0.6f"%x[i]," %.6f"%x[i+1]," %.6f  "%x[i+2],pre)
            if (abs((x[i+2]-x[i+1])/x[i+2])*100)<=per:
                print('Final Ans: ',x[i+2])
                break
        else:
            print('Final Ans: ',x[i+1],'\nOperation broken due to zero division')
            break
    
else:
    n=int(input('Enter the number of iteration: '))
    x1=float(input("Enter 1 st initial Value: "))
    x2=float(input("Enter 2 nd initial Value: "))
    x=[x1,x2]
    print("Itr  x(i-1)     x(i)     x(i+1)    pr_error")
    for i in range(n):
        if (eq(x[i+1])-eq(x[i])) != 0:
            x.append(x[i+1]-((eq(x[i+1])*(x[i]-x[i+1]))/(eq(x[i])-eq(x[i+1]))))
            pre=(abs((x[i+2]-x[i+1])/x[i+2])*100)
            print(i+1," %0.6f"%x[i]," %.6f"%x[i+1]," %.6f  "%x[i+2],pre)
        else:
            print('Operation broken due to zero division')
            break
    print('Final Ans: ',x[i+1]) if (eq(x[i+1])-eq(x[i])) == 0 else print("Final Ans: ",x[i+2])
    





