directory = 'Res_1st'
# open a result file specified in the argument
f = open(directory + 'ResPos', 'r')

temp = f.readline() # read first line of the file
count = 0
true_positive = 0

# while temp is not empty, continue reading the file
while temp:
    temp = temp.split(' ')
    # print(temp)
    # if temp contain the word 'Score', then get the value.
    # if the value is greater or equal to 0.0, increase the correct by 1
    # Increase count by 1 at the end of each time 'Score' is found
    if temp[0].find('Score') > -1:
        val = float(temp[1])
        # print(val)
        if val > 0.0: # greater or equal to 0.0
            true_positive += 1
        else:
            false_negative += 1
        count += 1
    temp = f.readline()

f.close()

print('Correct:' + str(correct))
print('count: ' + str(count))
print(float(correct)/float(count))

