n =int(input("ENTER NUMBER OF STUDENT: "))

names=[]
ages=[]

for i in range(n):
    print("STUDENT",i+1)

    name = input("ENTER NAME: ").upper()
    age  = int(input("ENTER AGE: ")).upper()

    names.append(name)
    ages.append(age)

for i in range(1,n):
    key_name = names[i]
    key_age  = ages[i]

    j=i-1
    
    while j >= 0 and ages[j]< key_age:
        names[j+1]=names[j]
        ages[j+1]=ages[j]
        j-=1

    names[j+1]=key_name
    ages[j+1]=key_age

for i in range(n):
    print('STUDENT:',names[i],'-',ages[i],'years old')