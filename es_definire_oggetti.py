class CSVFile(): 
  def __init__(self, name):
    self.name= name

  def get_data(self):
    file=open(self.name, 'r')
    values=[]
    for line in file:
      elements= line.split(',')
      if elements[0]!='Date':
        values.append(elements)
    file.close()
    return print(values)

file_csv=CsvFile('shampoo_sales.csv')
file_csv.get_data()