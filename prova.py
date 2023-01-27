def sum_csv(file):
  values=[]
  for line in file:
    elements= line.split(',')
    if elements[0]!='Data':
      value=elements[1]
      values.append(value)

  file.close()
  return sum(values)
  