import os

print(os.path.dirname(__file__))
#print(os.path.dirname('Code'))

a = os.path.join(os.path.dirname(__file__))
print(a)