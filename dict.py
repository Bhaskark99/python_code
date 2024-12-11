prod={1:"ball",2:"pen",3:"book"}
print(prod)
print(type(prod))
for key,val in prod.items():
    print(key,"==:",val)
    
for key in prod.keys():
    print(key)
    
for val in prod.values():
    print(val)
    
print(prod.get(1))
print(prod.pop(1))
print(prod)

        
    