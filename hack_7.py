"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    ce = len(result)
    result2 = []
    if(result[0]==0 and ce==1):
        result2.append(0)
    else:
        for i in range(0, ce): 
            if(i % 2 == 0):
                result2.append(str(i+1))
            else:
                result2.append(i+1)
    return list(result2)    
    
print(fn_hack_7(['a','b','c','d','e']))
print(fn_hack_7([0]))