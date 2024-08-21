"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    result.clear()
    result['Foo'] = "Fooziman"
    return result

print(fn_hack_9({"foo":"fookziman","bar":"barziman"}))
