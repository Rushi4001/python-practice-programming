import functools

arr=[8,9,5,16,2,4,21,30,11]
    
evenarr=list(filter(lambda no:(no%2==0),arr))
print("data after filter is:",evenarr)
    
modarray=list(map(lambda no:no+2,evenarr))
print("data after map is :",modarray)
    
sum=functools.reduce(lambda no1,no2:no1+no2,modarray)
print("data after reduce is :",sum)