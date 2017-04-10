from final import *

l = load_file_names('dataset/review_polarity/pos')

for name in l:
    f = open(name, 'r')
    text = f.read()
    f.close()
    text = text.split('.')
    text = text[-5:]

    name = name.split('/')
    path = 'dataset/review_polarity_LastFive/pos/' + name[-1]
    f = open(path, 'w')
    for t in text:
        t = t + '.'
        f.write(t)
    f.close()