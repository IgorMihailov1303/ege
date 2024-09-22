text = open('24.txt'). read()
text = text.replace('XZZY', '1')

cp = []
for i in range(len(text)):
    if text[i] == '1':
        cp.append(i)

r = []
for i in range(len(cp) - 1):
    r.append(cp[i+1]-cp[i])
print(max(r))
