plot_list=[[0 for i in range(10)] for i in range(10)]
result=[0 for i in range(10)]

for i in range(10):
    result[i]=2*i+3

step=round((result[9]-result[0])/9, 2)
print(step)

for i in range(10):
    plot_list[i][0] = step * (9-i)

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k+1] = 1
print(plot_list)
for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '!!'
    print(line)
print('\t0\t1 2 3 4 5 6 7 8 9')
