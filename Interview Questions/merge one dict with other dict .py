dict1={1:'applr',2:'mango'}
dict2={3:'banana',4:'orange'}

dict1.update(dict2)
#print(dict2)

dict3={**dict1,**dict2}

print(dict3)