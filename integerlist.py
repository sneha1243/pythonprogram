test_list1=[1,2,1,3,5]
test_list2=[1,2,4,3,5]
print("the first list is:"+str(test_list1))
print("the second list is:"+str(test_list2))
test_list1.sort()
test_list2.sort()
if len(test_list1)==len(test_list2):
	print("the lists are have same length")
else:
	print("the lists are not have same length")
def common_data(list1,list2):
	result=0
	for x in list1:
		for y in list2:
			if x==y:
				result=result+x
	return result
print("sum is:",common_data(test_list1,test_list2))
x=int(input("enter number to be searched"))
if x in test_list1:
	print("the first list contains the value")
elif x in test_list2:
	print("the second list contains the value")
else:
	print("the list has no such value")
