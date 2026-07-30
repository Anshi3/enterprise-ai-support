def decorator(func):
    def wrapper(*args,**kwargs):
        print(f"Before function")
        result=func(*args,**kwargs)
        print(f"After func")
        return result
    return wrapper

@decorator
def greet(name):
    print(f"name is {name}")
    
    
greet(name="Anshika")
    
    
    
        