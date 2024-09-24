sp = ['c=','c-','dz=','d-','lj','nj','s=','z=']
t = input()

for i in sp:
    t = t.replace(i, "*")
print(len(t))