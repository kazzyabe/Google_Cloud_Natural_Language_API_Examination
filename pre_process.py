from final import *

l = load_file_names('dataset/pos')

for name in l:
    f = open(name, 'r')
    text = f.read()
    f.close()
    
    flag = True
    i = 0
    while i < len(text) and flag:
        if text[i] == '[':
            flag = False
            text = text[:i]
        i += 1
    f = open(name, 'w')
    f.write(text)
    f.close()