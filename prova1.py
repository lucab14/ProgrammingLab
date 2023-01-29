class CSVFile:
  def __init__(self, name):
    self.name=name

  def get_data(self):
    try:
      file=open(self.name, 'r')
    except Exception as e:
      return print('Errore {}'.format(e))
    lists=[]
    for line in file:
      elements=line.strip('\n').split(',')
      if elements[0]!='Date':
        data=elements[0]
        value=elements[1]
        lists.append([data, value])
    file.close()

    return lists  

file_name=CSVFile('shampoo_sales.csv')
