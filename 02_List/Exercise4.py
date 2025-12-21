"""Write  a  program  that  reads  in  numbers  separated  by  a  comma  in  one  line,  and  displays  distinct 
numbers  (i.e.,  if  a  number  appears  multiple  times,  it  is  displayed  only  once).  (Hint:  Read  all  the 
numbers and store them in list1. Create a new list list2. Add a number in list1 to list2. If the number is 
already in the list, ignore it."""

#Ask the user to enter ten numbers
nums = input("Enter ten numbers: ")

#split the number into list
list1 = nums.split(",")
list2 = []

#check each number
for n in list1:
    n = n.strip()         
    if n not in list2:
        list2.append(n)

#Display the result       
print("The distinct numbers are:", " ".join(list2))