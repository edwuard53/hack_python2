"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    ce = len(result)
    result2 = []
    for i in range(ce,0,-1): 
        if(ce % 2 == 1):
            result2.append(result[i-1]+"-"+str(i))
        else:    
            result2.append(str(i))
    return result2

print(fn_hack_8(['a','b','c','d','e']))
print(fn_hack_8(["a","b","c"]))
print(fn_hack_8(['a','b','c','d']))
print(fn_hack_8(["a","b"]))
