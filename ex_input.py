a = int(input("input 1st number : "))
b = int(input("input 2nd number : "))  
c = int(input("input operator(+, *) : "))  # input == scanf 동일
 
# print(a + b)
# print("1st:%s + 2nd:%s = %s" %(a, b, a+b)) # %s는 %d %f 다 가능 stdio.h

def add(a, b) :
    return a+b

def multi(a, b) :
    return a*b

if c == '+' :
    result = add(a, b)
    print(result)
elif c == '*' :
    result = multi(a, b)
    print(result)
else :
    pass #아무코토 안할때 pass

    