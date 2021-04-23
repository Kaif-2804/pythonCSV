import pandas
df = pandas.read_csv('hrdata_modified.csv', 
    index_col='Employee', 
    parse_dates=['Hired'], 
    header=0, 
    names=['Employee', 'Hired','Salary', 'Sick Days', 'ID#'])

df.to_csv('hrdata.csv')