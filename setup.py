from numpy.lib import DataSource
import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Coffee in ml", y="sleep in hours")
        fig.show()

def getdatasource(data_path):
    coffee=[]
    sleep=[] 
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee"]))
            sleep.append(float(row["Sleep"]))
    
    return {"x" : coffee, "y": sleep}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation is", correlation[0,1])

def setup():
    data_path="C:/Users/DELL/Desktop/python project/Correlation/correlation-master/correlation-master/data/cups of coffee vs hours of sleep.csv"
    datasource=getdatasource(data_path)
    findcorrelation(datasource)
    plotFigure(data_path)

setup()