#Define a function my_zip() that can form a list of tuples by iterating the following customer details:- ‘customer Name, customer ID , shopping points’ and based on the keyword parameter ‘strct’: If strct = True, zipping shall be done only if all lists are of equal length. If strct = False, zipping can be done by taking the minimum length of the iterable.

def my_zip(customer_Name,customer_ID,shopping_points):
    a1=len(customer_Name)
    a2=len(customer_ID)
    a3=len(shopping_points)
    strct=False
    if(a1==a2==a3):
        strct=True
    if(strct):
        t=list(zip(customer_Name,customer_ID,shopping_points))
    else:
        a=min(a1,min(a2,a3))
        t=[]
        for m in range(a):
            i=customer_ID[m]
            j=customer_Name[m]
            k=shopping_points[m]
            t.append((i,j,k))

    return t

p=my_zip([1,2,3],['a','b','c','d'],[5,6,7,8])
print(p)