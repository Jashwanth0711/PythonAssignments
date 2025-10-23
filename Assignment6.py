# how to unpack the dictionary using while loop
student = {"name": "Jashwanth", "age": 22, "city": "Hyderabad"}
student_list=list(student.items())
print(student_list)
start=0
while start<len(student):
    key,value=student_list[start]
    print(f"key:{key}  value:{value}")
    start+=1
    
 #Bubble sort technique
lst=[5,2,1,4,3]
print(f"Before sorting:{lst}")
n=len(lst)
for i in range(n-1):
    for j in range(n-1):
        if lst[j]>lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]


print(f"After sorting:{lst}")

'''lst = ['harsha', 'ranjth', 'kiran'] 
output: 
h 
a 
r 
s 
h 
a 
r 
a 
n 
j 
i 
t 
h 
k 
i 
r 
a 
n
'''
lst=["Jessie","Karan","Vamsi"]
for name in lst:
    for letter in name:
        print(letter)