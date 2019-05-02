print("for语句中，没有对nums操作")
nums=[1,2,3,4,5]
for i in nums:
    nums.pop()
    print(i)
'''
for语句中，没有对nums操作
1
2
3
'''
print("for语句中，对nums切片")
nums=[1,2,3,4,5]
for i in nums[::]:
    nums.pop()
    print(i)
'''
for语句中，对nums切片
1
2
3
4
5
'''