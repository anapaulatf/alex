import numpy as np
import pmdarima as pm
import quandl
import pandas as pd
import matplotlib.pyplot as plt
mydata = quandl.get("FRED/CPIAUCNS", returns="numpy",authtoken="b2P8ovo7y75geHc7vMq_",  start_date="2012-02-01", transform="rdiff")

index = pd.date_range("2012-03-31", "2021-06-30", freq="M")
df = pd.DataFrame(mydata, index=index)
df.drop("Date", inplace=True, axis=1)
index = pd.date_range("2021-07-30", "2021-06-30", freq="M")

arima = pm.auto_arima(df)
forecast, conf_int =arima.predict(n_periods=6,return_conf_int=True)

index2 = pd.date_range("2021-07-30", "2021-12-31", freq="M")
df2 = pd.DataFrame({"Forecast":forecast}, index=index2)
df3=df.append(df2)

#annual accumulado
train=(1+df).rolling(window=12).apply(np.prod, raw=True) - 1
x1=df.tail(n=11)
x2=np.append(x1,df2.tail(n=7))
index3 = pd.date_range("2020-08-31", "2021-12-31", freq="M")
df4 = pd.DataFrame({"Forecast":x2}, index=index3)
x4=(1+df4).rolling(window=12).apply(np.prod, raw=True) - 1
dataset=train.append(x4)



with plt.style.context('seaborn-colorblind'):
 fig, ax1 = plt.subplots()
 x_axis = np.arange(df.shape[0] + forecast.shape[0])
 ax1.plot(dataset["Forecast"],   label="Prévisions - Modèle ARIMA")
 ax1.plot(dataset["Value"],   label="CPI - US")
 plt.title("Graphique 2. Indice des prix au consommateur - U.S (%)", fontsize=9,fontweight = 'bold')
 plt.ylabel("(%)", fontsize=9,fontweight = 'bold')
 plt.xlabel("Années",fontsize=8,fontweight = 'bold')
 fig.tight_layout()
 plt.legend(bbox_to_anchor=(0.30, 1), loc='upper left')
 plt.show() 

