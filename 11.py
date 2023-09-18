n = float(input())
last = n
new = last - ((last**3-n)/(3*last**2))

while abs(new - last) > 0.000001:
    last = new
    new = last-((last**3-n)/(3*last**2))
    print(format(new,'.1f'))