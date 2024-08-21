"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    ce = len(result)
    if(ce==0):
        palabra = "0"
    else:
        palabra = ""
        for i in range(0, ce+1): 
            if(i % 2 == 0):
                palabra +=str(i+1)
            else:
                palabra += str("-")
        palabra = palabra[0:-1]        
    palabra = list(palabra)    
    return palabra
print(fn_hack_6(['a','b','c','d','e']))
print(fn_hack_6([]))