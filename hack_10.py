"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    letras = {    "a": 1,    "b": 2,    "c": 3,    "d": 4,    "e": 5,    "f": 6,    "g": 7,    "h": 8,    "i": 9,    "j": 10,    "k": 11,    "l": 12,    "m": 13,
                 "n": 14,   "o": 15,   "p": 16,   "q": 17,   "r": 18,   "s": 19,   "t": 20,   "u": 21,   "v": 22,   "w": 23,    "x": 24,    "y": 25,    "z": 26,
            }
    salida = []
    for elementos in result:
        diccionario_result = {}
        for clave in elementos:
            diccionario_result[str(letras[clave])] =str(letras[elementos[clave]])
            salida.append(diccionario_result)
    return salida

print(fn_hack_10([{"a":"b"},{"c":"d"},{"e":"f"}]))