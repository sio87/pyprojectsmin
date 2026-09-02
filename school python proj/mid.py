def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j >= 0 and arr[j]<key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
    
nums=[]
for i in range(7):
    nums.append(input("ENTER A YOUR 7 NUMBERS: "))
sorted=insertion_sort(nums)

max=sorted[0]
min=sorted[-1]
med=sorted[3]

print("SORTED:",nums)
print("MAX:",max,"MIN:",min,"MED:",med)