# checking the logic
a = 5
print(a == 10)
print(False ==  False)

if not a == 10 == False:
    print("a is not equal to 10")
else: 
    print('False')
# нихера не понятно 

# Array correcter
print(dir(list))
a = [1,2,3,4,5,6,12,3,14,2,1,3]
print(set((a)))

# Array locig
arr = [1,2,3,14,123,1,231,23,1,2,3,4,5,5]
# Reverse the array 
arr.reverse()
if len(arr) == 1:
    print(0)
# check logic 1
elif len(arr) == 2:
    print(arr[0] - arr[1])
# check logic 2
elif len(arr) > 2:
    print((arr[0] - arr[1]) + (arr[1] - arr[2]))

# Array math
arg1 = [1,5,3,2,5]
# Array fucntion
arg1.remove(min(arg1))
# The biggest of number in the array
print(max(arg1))
# Сycle
for i in arg1:
    # Not end not first
    if  min(arg1) < i < max(arg1):
        print(i + 1)

print(arg1)

# Array with string
arr = [1,2,3,4,5]
if arr.is_int_array == True:
    print('true')

# Array of string's logic
script = 'thllo-;;;-kjk'
# Cycle with new function
for i in script:
    # Check logic of cycle with new function
    if i == '-' and '_':
        A = {'-', '_'}
        print(script.difference_update(A))
