
nums = [2,5,5,11]
target = 10
output = []

for i in range (len(nums)):            
    x = nums[i]           
    if target - x in nums:          
        print(i)
        if i and nums.index(target - x) not in output and i != nums.index(target - x):
            output.append(i) 
            print(output) 
            output.append(nums.index(target - x))        
            print(output)   
      
print(output) 