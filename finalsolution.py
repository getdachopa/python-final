columns = []
fo = open("dr_S03_2_2018_800.txt", "r")
for line in fo.readlines():
  line = line.strip().split(' ')
  line = filter(None, line)
  line = map(int, line)
  line = list(line)

  columns.append(line[1])

columns.sort()

while(len(columns) > 0):
  ints = []
  ints.append(columns.pop())
  if(len(columns) == 0):
    continue
  while(len(columns) > 0 and sum(ints) + columns[0] < 600):
    ints.append(columns.pop(0))
  print(' + '.join(map(str, ints)) + ' = ' + str(sum(ints)))
  continue
