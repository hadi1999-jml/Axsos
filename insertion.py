def selector_insertion(arr):
    for i in range (len(arr)):
        current=arr[i]
        position=i

        while position>0 and arr[position-1]>current:
            arr[position]=arr[position-1]
            position -=1
        arr[position]=current    
       ## print(position)
    ##    print(arr)
    return arr

h=[29,10,2,11,52,15,18,19,20] 
sort_number=selector_insertion(h)
print("sort_list:",sort_number) 