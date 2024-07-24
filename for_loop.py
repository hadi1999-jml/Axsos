
for i in range(151):
  print(i)

five_list=[]
for x in range(5,1001):
  if x%5==0:
    five_list.append(x)

print(five_list)


integer_list=[]
for y in range(1,101):
  integer_list.append(y)
  
  if y%5==0:
    print("Coding")
  if y%10==0:
    print("Coding Dojo")  
print(integer_list)

sum=0
for z in range(0,500001):
  if z%2 ==1:
    sum+=z

print(sum)

positive_list=[]
for p in range(2018,0,-4):
  if p>0:
    positive_list.append(p)

print(positive_list)


def flexible_counter(lowNum, highNum, mult):
    current_num = lowNum
    while current_num <= highNum:
        if current_num % mult == 0:
            print(current_num)
        current_num += 1

# Example usage:
lowNum = 2
highNum = 25
mult = 4
flexible_counter(lowNum, highNum, mult)