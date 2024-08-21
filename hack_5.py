"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    _str = []
    cont=1
    if(result[0]=='f'):
        result = result[0:5] + result[4:len(result)]

    for txt in result:
        if(cont % 3 == 0):
            _str.append('-')
        else:
            _str.append(txt)     
        cont = cont + 1  
    result = "".join(_str)
    return result

print(fn_hack_5('fooziman'))
print(fn_hack_5('fanatica'))
print(fn_hack_5('barziman'))
print(fn_hack_5('qux'))
print(fn_hack_5('eq'))