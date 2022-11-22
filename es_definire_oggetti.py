class CsvFile(): 
  def __init__(self, name):
    self.name= name

  def get_data(self):
    file=open(self.name, 'r')
    values=[]
    for line in file:
      elements= line.split(',')
      if elements[0]!='Date':
        date= elements[0]
        value=elements[1]
        values.append(elements)

    return print(values[0:-1])

file_csv=CsvFile('shampoo_sales.csv')
file_csv.get_data()