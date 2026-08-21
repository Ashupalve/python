# 3. Create a class with a class attribute a; create an object from it and set ‘aʼ directly using
# ‘object.a = 0ʼ. Does this change the class attribute?

class ashu :
    a =0

o= ashu()

print(o.a)

o.a =4 

print(o.a)
print(ashu.a)
