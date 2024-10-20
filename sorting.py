def sort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j

        arr[i],arr[min]=arr[min],arr[i]
    return arr

h=[29,10,2,11,52,15,18,19,20] 
sort_number=sort(h)
print("sort_list:",sort_number)   