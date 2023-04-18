def hello(name=''):
    return f"Hello, {name.title() or 'World'}!"

#lub 

def hello(name=''):
    if name != "":
        return 'Hello, ' + name.capitalize() + '!'
    return 'Hello, World!'
