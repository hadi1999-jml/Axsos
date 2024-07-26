def countdown(x):
    counter = []
    for i in  range(x,-1,-1):
        counter.append(i)
    return counter
print(countdown(10))



def pr_re(a):
    if len(a)!=2:
        print("list must containe tow values")

    print(a[0])
    return a[1]
a=[5,6]
print(pr_re(a))

list2 =[]
def values_greater_than_second(gr_list):
    print("hadi")
    for i in range(0,1,len(gr_list)):
        if gr_list[i]>gr_list[1]:
            list2.append(gr_list[i])
            return(list2)
        

    print (list2)        
print(values_greater_than_second([1,5,6,8,2]))

def length_and_value(size, value):
    result = []
    for _ in range(size):
        result.append(value)
    return result
print(length_and_value(4, 7))  
print(length_and_value(6, 2))
    
