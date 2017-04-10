# open a result file specified in the argument
f = open('Res_3rd/ResPos', 'r')
f2 = open('Res_6th/ResPos', 'r')

temp = f.readline() # read first line of the file
temp2 = f2.readline()
count = 0
amb = 0

# while temp is not empty, continue reading the file
while temp:
    temp = temp.split(' ')
    temp2 = temp2.split(' ')
    # print(temp)
    # if temp contain the word 'Score', then get the value.
    # if the value is greater or equal to 0.0, increase the correct by 1
    # Increase count by 1 at the end of each time 'Score' is found
    if temp[0].find('Score') > -1:
        val = float(temp[1])
        val2 = float(temp2[1])
        # print(val)
        if val == 0.0: # greater or equal to 0.0
            # for positive
            if val2 > 0.0:
                amb += 1
            # for negative
            # if val2 < 0.0:
            #     amb += 1
            count += 1

    temp = f.readline()
    temp2 = f2.readline()

f.close()
f2.close()
print('amb:' + str(amb))
print('count: ' + str(count))
