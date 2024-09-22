text = open('23.txt'). read()
text = text.replace('A', '1').replace('B', '1').replace('C', '1')

cp = []
for i in range(len(text) - 1):
    if text[i] == '1' and text[i+1] == '1':
        cp.append(i)

r = []
for i in range(len(cp) - 1):
    r.append(cp[i+1]-cp[i])
print(max(r))
