def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j >= 0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

num = []

for i in range(5):
    num.append(input("Enter Value: "))
    for i in num():
        print(insertion_sort(num),print("\\"))

