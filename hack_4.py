"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    _str = []
    cont = 0
    for txt in result:
        if(len(result)>3):
            if(cont!=0 and cont!=len(result)-1):
                _str.append(txt)
        else:
            _str.append(txt)        
        cont = cont + 1  
    result = "".join(_str)
    return result

print (fn_hack_4('fooziman'))
print (fn_hack_4('barziman'))
print (fn_hack_4('qux'))