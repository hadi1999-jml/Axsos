##Biggie Size
def biggie_size(numbers):
    for i in range(len(numbers)):
        if numbers[i] > 0:
            numbers[i] = "big"
    return numbers
    
print(biggie_size([0,1,2,8,-1,-6]))   


## count positive 
count=[]
def count_positive(positive_number):
    for i in range(len(positive_number)):
        if positive_number[i] > 0:
               count.append(i)

        y=len(count)    

    positive_number[len(positive_number)-1]=y
    return positive_number

print(count_positive([8,1,2,3,8,-5,6,2]))

### Sum Total

def sum_total(sumation):
    a= sum(sumation)

    return a 
print(sum_total([1,2,2])) 


### average

def average(sumation):
    x=len(sumation)
    a= sum(sumation)
    average=a/x
    return average
print(average([2,2,2])) 

##length_list
def length_list(length):
    return len(length)
print(length_list([1,5,8,9]))
print(length_list([]))

## minimum Value

def minimum_value(minimum):
    if(len(minimum)==0):
        return False
    
    else:
         x=minimum[0]
    for i in range(len(minimum)):
        if minimum[i] < x:
            x=minimum[i]
   
    return x    
print(minimum_value([1,8,5,0,-8]))
print(minimum_value([]))


## maximum Value

def maximum_value(maximum):
    if(len(maximum)==0):
        return False
    
    else:
         x=maximum[0]
    for i in range(len(maximum)):
        if maximum[i] > x:
            x=maximum[i]
   
    return x    
print(maximum_value([1,8,50,0,-8]))
print(maximum_value([]))

##Ultimate Analysis
def ultimate_analysis(num_list):
    sum=sum_total(num_list)
    avg=average(num_list)
    min=minimum_value(num_list)
    max=maximum_value(num_list)
    length=length_list(num_list)
    analysis={
        'sumTotal':sum,
        'average':avg,
        'minimumValue':min,
        'maximumValue':max,
        'length_list':length
    }
    return analysis
print(ultimate_analysis([23,5,7,8,9,2]))


##Reverse List

## def reverse_list(num_list):



