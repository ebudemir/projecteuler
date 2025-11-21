targets = [1,10,100,1000,10000,100000,1000000]
s = []
n = 1
# build string until we have at least 1,000,000 digits
while len(s) < targets[-1]:
    s.extend(list(str(n)))
    n += 1

prod = 1
digits = []
for t in targets:
    d = int(s[t-1])   # zero-indexed in python list
    digits.append(d)
    prod *= d

print("digits at targets:", digits)
print("product:", prod)
