#Linear Search in array with (input value which position find a method )


array = [10,9,2,3,5,7]

n = int(input("enter the index value of array position:"))

for i in range(0, len(array)):
    if array[i] == n:
        print("search of array position is:",i)
        break
else:
    print("thats not value in array")



#this will be true or false method:


array = [10,9,2,3,5,7]

n = int(input("enter the index value of array position:"))

for i in array:
    if i == n:
        print("Yes")
        break
else:
    print("No")
