import numpy as np
import matplotlib.pyplot as plt

def basic(xdata,ydata,title,xlabel,ylabel,color):
    plt.figure()
    plt.title(title, fontsize=20)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.plot(xdata,ydata,'x',markersize=10.0, color=color)

def basicSupervised():
    size = [490,600,650,700,850,925,1000,1120,1125]
    price = [150,200,210,205,260,300,356,350,360]
    basic(size,price,'House Prices', 'Size (m²)','Price (Thousands)','darkblue')

def basicClassification():
    tumorSize = [1,2,3,4,5,6,7,8,9]
    malignant = [0,0,0,0,0,1,1,1,1]
    basic(tumorSize,malignant,'Malignant Tumor','Tumor Size','Is Malignant?','darkred')

def basicClustering():
    classes = [1.5,1.4,1.6,1.8,3.18,3.2,3.2,3.3,3.35]
    ydata = [2.3,1.8,1.78,1.95,4.2,4.3,4.6,4.5,4.8]
    basic(classes, ydata,'Unsupervised Learning','x1','x2','blue')
