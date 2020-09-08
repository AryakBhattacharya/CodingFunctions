lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele)
print(lst)
lst.insert(3,6)
prime=[2,3,7]
prime.insert(2,5)
print('updated lst:',lst)
print('updated prime:',prime)
