"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    originales = ["a","e","i","o","u"]
    reemplazos = ["@","3","¡","0","v"]
    _str = []
    cont = 0
    for txt in result:
        if txt in originales:
          ind = originales.index(txt)
          _str.append(reemplazos[ind])  
        else:
          if(cont==0 or cont==len(result)-1):
            txt=txt.upper()
          _str.append(txt)    
        cont = cont + 1  
    result = "".join(_str)
    return result

print (fn_hack_3('fooziman'))
print (fn_hack_3('barziman'))
print (fn_hack_3('3q'))
print (fn_hack_3('qu'))
print (fn_hack_3('qux'))