def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j >= 0 and arr[j]<key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

name =input("Enter your name: ").upper()
age  =input("Enter your age: ")
name=[n for n in name]
age=[a for a in age]

print("\n-----------ORIGINAL-----------")
print(f"Original: {name}")
print(f"Original: {age}")

print("\n-----------SORTING-----------")
insertion_sort(name)
print(f"sorted: {name}")

insertion_sort(age)
print(f"sorted: {age}")