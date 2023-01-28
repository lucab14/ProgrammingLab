class CSVFile:
  def __init__(self, name):
    self.name=name

  def get_data(self):
    file=open(self.name, 'r')
    lists=[]
    for line in file:
      elements=line.strip('\n').split(',')
      if elements[0]!='Date':
        data=elements[0]
        value=elements[1]
        lists.append([data, value])
    return lists

file_name=CSVFile('shampoo_sales.csv')