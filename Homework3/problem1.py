list_of_nums = list(map(int, input("Enter integers separated by spaces: ").split()))
find_max = list_of_nums[0]  
find_min = list_of_nums[0]
result = 0
for i in range(0, len(list_of_nums), 1): 
    if find_max < list_of_nums[i]:
       find_max = list_of_nums[i] 
    elif find_min > list_of_nums[i]:
       find_min = list_of_nums[i] 


result = find_max - find_min
print(result) 
