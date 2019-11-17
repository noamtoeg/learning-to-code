import numpy as np
import pandas as pd
my_list = [10,20,30]
my_arrays = [[10,20,30],[40,50,60]]
my_dictionary = {'a':10, 'b':20, 'c':30}
### Pandas Series:
# is an indexed column in an excel sheet
myvar = pd.Series(my_arrays) # pass an array/dictionary/list to series
#print(myvar)

ser1 = pd.Series([1,2,3,4], index=['USA','CHINA','FRANCE','ISRAEL'])
ser2 = pd.Series([1,2,3,4], index=['USA','CHINA','ITALY','JAPAN'])
#print(ser1 * ser2)

### Pandas DataFrame:
# - 2 dimensional tabular data structure with labeled axes (rows and columns).
# a collection of data series that share a common index
df = pd.DataFrame(np.random.randn(5,4),['A','B','C','D','E'],[1,2,3,4])
#print(df) # will display the whole data frame

#print(df[3]) # will display a single column (in this case, column number 3)
#print(df[[3,4]]) # will display multiple columns (in this case, column number 3 and 4)

# adding a new column to a data frame
#df['new'] = df[1] + df[2]

# adding a new row to a data frame
# loc relies on label name, while iloc relies on index number to select row
#print(df.loc['B'])
#print(df.iloc[1])

# selecting a cell in the data frame
#print(df.loc['B',3])

## dropping - by default, drop will remove a row
# in order to remove a column, an argument needs to be defined: axis = 1
# dropping a column from a data frame
dropped2 = df.drop(2, axis=1)
#print(dropped2)

# dropping a row from a data frame
# in order to save a removal of data (drop), an argument inplace=True must be added
droppedB = df.drop('B', inplace=True)
#print(df)

#print('Final')
#print(df)

# dataframe shape
# returns the size of the dataframe (x,y) or (4,5) in this example
#print(df.shape)

# apply confitional on each cell of the dataframe
#print(df[df>0])
#print(df[df[2]>0])

# Set index
#df.set_index('States')

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
our_index = list(zip(outside,inside)) # pairs each item of each list to it's corresponding item
our_index = pd.MultiIndex.from_tuples(our_index) # turns tuples into inner and outer index
#print(our_index)

df = pd.DataFrame(np.random.randn(6,2), our_index, ['A', 'B']) # pairs data with chosen indexes (G1, G2). Names columns A and B
#print(df)

print(df.loc['G1'].loc[2]) # selects outer index of G1 and inner index of 2
df.index.names = ["Groups", "Names"] # setting names for indices
df.xs(1,level='Num') # selecting a cross section from index 'Num'