import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
index = pd.date_range("1977-01-01", "2021-05-31", freq="M")


g1 = pd.read_excel(r"Issue 2\Graph_issue2.xlsx", index_col="PERIODO")
g1.index = index

with plt.style.context('seaborn-colorblind'):
    fig, ax1 = plt.subplots()
    ax1.plot(g1["Germany"],  label="PPI - Allemagne")
    ax1.plot(g1["Spain"],  label="PPI - Espagne")
    plt.title(" Graphique 1. PPI  - (variation inter-annuelle - %)", color="black",fontsize=9,fontweight = 'bold')
    plt.ylabel("(%)", color="black", fontsize=9,fontweight = 'bold')
    plt.xlabel("", color="black", fontsize=8,fontweight = 'bold')
    fig.tight_layout()
    plt.legend(bbox_to_anchor=(0.30, 1), loc='upper left')
    plt.show() 


g2 = pd.read_excel(r"C:\Users\Alexandre Lohmann\Desktop\Newsletter Macro\Issue 2\Graph_issue2.xlsx", sheet_name="Sheet2", index_col="o")

index2 = pd.date_range("2020-01-01", "2021-05-31", freq="M")

g2.index = index2
print(g2. columns)
 
 with plt.style.context('seaborn-colorblind'):
    fig, ax1 = plt.subplots()
    ax1.plot(g2.iloc[:,0],  label="PPI - Espagne")
    ax1.plot(g2.iloc[:,1],  label="PPI - Allemagne")
    ax1.plot(g2.iloc[:,2],  label="PPI - Portugal")
    ax1.plot(g2.iloc[:,3],  label="PPI - Italie")
    ax1.plot(g2.iloc[:,4],  label="PPI - Grèce")
    plt.title(" Graphique 3. PPI  - (Indice 100 : 2020M01)", color="black",fontsize=9,fontweight = 'bold')
    plt.ylabel("Indice", color="black", fontsize=9,fontweight = 'bold')
    plt.xlabel("", color="black", fontsize=8,fontweight = 'bold')
    fig.tight_layout()
    plt.legend(bbox_to_anchor=(0.30, 1), loc='upper left')
    plt.show() 



