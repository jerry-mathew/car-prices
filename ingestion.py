## Scientific computing libraries
## Pandas offer data structure and tools for effective data manipulation and analysi
## NumPy uses arrays for inputs/outputs for objects for matrices. 
## SciPy includes functions for advanced math problems and data visualization

## Visualization libraries
## Matplotlib - data visualization for graphs/plots 
## Seaborn - based on matplotlib heat maps, time series, violin plots

## Algorithmic libraries
## Scikit-learn regression, clustering and so on
## statsmodels allows users to explore data, estimate statistical models and perform statistical tests

import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(url, header=None)



url_header = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.names"
headers = ['symboling','normalized-losses','make','fuel-type','aspiration','num-of-doors','body-style','drive-wheels','engine-location','wheel-base','length','width','height','curb-weight','engine-type','num-of-cylinders','engine-size','fuel-system','bore','stroke', 'compression-ratio','horsepower','peak-rpm','city-mpg','highway-mpg','price']
df.columns = headers

print("------Printing first two")
print(df.head(2))
#print("------Printing last two")
#print(df.tail(2))

#export to csv
#df.head(2).to_csv("C:/Users/jmath\desktop/autombile_test.csv")

print(df.dtypes)
print(df.describe(include="all"))
print(df.info())