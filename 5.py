w,x,y,z = input().split()
if w < x:
    w,x = x,w
if x < y:
    x,y = y,x
if y < z:
    y,z = z,y
if x < y:
    x,y = y,x
print(w,x,y,z)