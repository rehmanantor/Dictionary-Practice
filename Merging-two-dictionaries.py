
other={
    "Name":"Ebad",
    "Roll no": 1005,
    "Gr No":1012,
    "CID no":2013,
    "Grade":"A",
    "Marks":3.4
}



dic = {
    "Name":"Ebad",
    "Class":"5-O'levels",
    "Age":13,
    "Grade":"B",
    "Marks":3.1
}  

def merged(dic,other):
    sample={}
    sample=dict(dic)
   
    for key,value in dic.items():
        for key1,value1 in other.items():
              dummylist=[]
        if key==key1 and value==value1 :
            sample.update({key1:value1})
        elif key==key1 and value!=value1:
            if type(value)==type(value1) and (type(value)==int or type(value)==float):
                sample.update({key1:value+value1})
            elif type(value)==type(value1) and (type(value)==str or type(value)==int or type(value)==float):
                dummylist.append(value)
                dummylist.append(value1)
                sample.update({key1:dummylist})
        elif key!=key1:
            sample.update({key1:value1})
    dic=dict(sample)  
    return dic         

    
      
a=merged(dic,other)
print(a)
