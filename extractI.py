from final import *

l = load_file_names('dataset/review_polarity/neg')

for name in l:
    f = open(name, 'r')
    text = f.read()
    f.close()

    text = text.split('.')
    extract = ''
    for t in text:
        if t.find(" i ") > -1: # or t.find(" you ") > -1 or t.find(" we ") > -1
            extract = extract + t + '.'
            # print('extracted')
    
    # print(extract)

    name = name.split('/')
    path = 'dataset/review_polarity_I/neg/' + name[-1]
    f = open(path, 'w')
    f.write(extract)
    f.close()
    # break
