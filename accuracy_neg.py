f = open('Res_ImprovedFinal/ResNeg', 'r')

temp = f.readline() # read first line of the file
count = 0
correct = 0

while temp:
    temp = temp.split(' ')
    # print(temp)
    if temp[0].find('Score') > -1:
        val = float(temp[1])
        # print(val)
        if val <= 0.0: # less or equal to 0.0, 
            correct += 1
        count += 1
    # if count == 32:
    #     break
    temp = f.readline()

f.close()
print('Correct:' + str(correct))
print('count: ' + str(count))
print(float(correct)/float(count))

