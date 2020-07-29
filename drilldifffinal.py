#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import glob


# In[29]:


def drilldown():
    
    All_paths=[r'C:\Users\drilldown\Arkeologisk Hk',
              r'C:\Users\drilldown\Askerbadene HK Server',
              r'C:\Users\drilldown\Boreal',
              r'C:\Users\drilldown\Bunnpris PROD HK Server',
              r'C:\Users\drilldown\DNOVA_HV4_BØ Sommerland HK server',
              r'C:\Users\drilldown\DNOVA_HV4_Hugos Tivoli HK Server',
              r'C:\Users\drilldown\DNOVA_HV4_Tess HK',
              r'C:\Users\drilldown\DNOVA_HV5_Klatreverket AS Server',
              r'C:\Users\drilldown\DNOVA_HV5_See Salmon HK Server',
              r'C:\Users\drilldown\DNOVA_HV5_SiB DN HK Server',
              r'C:\Users\drilldown\DNOVA_HV5_SiB HK Server',
              r'C:\Users\drilldown\Drammensbadet HK Server',
              r'C:\Users\drilldown\Flise F Bergen',
              r'C:\Users\drilldown\Flise FKOA',
              r'C:\Users\drilldown\Flisekompaniet HK server',
              r'C:\Users\drilldown\Flisekompaniet-FTrondheim-mini HK',
              r'C:\Users\drilldown\Football Shop HK Server',
              r'C:\Users\drilldown\Fretex HK',
              r'C:\Users\drilldown\Gausbygg Outlet',
              r'C:\Users\drilldown\Historical-Viking museum HK server',
              r'C:\Users\drilldown\Hunderfossen Server',
              r'C:\Users\drilldown\ISS Nordea HK',
              r'C:\Users\drilldown\ISS Prod HK Server',
              r'C:\Users\drilldown\Kraft Norway HK',
              r'C:\Users\drilldown\Kraft Sweden HK server',
              r'C:\Users\drilldown\Lampemagsinet',
              r'C:\Users\drilldown\Leif Skalleberg HK Server',
              r'C:\Users\drilldown\MIX Production HK',
              r'C:\Users\drilldown\Munch Museum Server',
              r'C:\Users\drilldown\Nidarosdomen HK server',
              r'C:\Users\drilldown\Norges varemess HK server',
              r'C:\Users\drilldown\Norled HK APP Server',
              r'C:\Users\drilldown\Oslo Sportslager HK server',
              r'C:\Users\drilldown\OslobadeneERPHK',
              r'C:\Users\drilldown\Paahjul HK Server',
              r'C:\Users\drilldown\Snarkjop',
              r'C:\Users\drilldown\Spinn HK',
              r'C:\Users\drilldown\Sprell HK',
              r'C:\Users\drilldown\Tilbords HK server',
              r'C:\Users\drilldown\Troms politidistrikt Server',
              r'C:\Users\drilldown\Trondheim Klatresenter HK',
              r'C:\Users\drilldown\Tropehagen',
              r'C:\Users\drilldown\Tusenfryd HK',
              r'C:\Users\drilldown\Visit Rjunkan',
              r'C:\Users\drilldown\YummyHeaven HK server',
              r'C:\Users\drilldown\Zoo-1 HK server'
               
               ]
    diff=[]
    
    for path in All_paths:
        
            
    #print(path)
        data_path = glob.glob(path + "/*.xls")
    #print(da ta_path)
        if len(data_path)>0:
            data=pd.read_excel(data_path[0])
            filter_data=data.iloc[-1:, 2:5]
        #payback=data['Payback'][1]
            if (filter_data.iloc[:,0]-filter_data.iloc[:,-1] >= 1).iloc[0] or (filter_data.iloc[:,0]-filter_data.iloc[:,-1] <= -1).iloc[0]:
                print(path[19:],end='')
                print('DrillDown Difference')
                x=path[19:]+'DrillDown Difference'
                diff.append(x)
                #print((filter_data.iloc[:,0]-filter_data.iloc[:,-1] > 1).iloc[0])
                #print((filter_data.iloc[:,0]-filter_data.iloc[:,-1] > -1).iloc[0])
            if (filter_data.iloc[:,1]>=1).iloc[0] or (filter_data.iloc[:,1] <= -1).iloc[0]:
                print(path[19:],end='')
                print('DrillDown Middle value Difference')
                x1=path[19:]+'DrillDown Middle value Difference'
                diff.append(x1)
            if (data.iloc[-1:,-1] <0).iloc[0]:
                print(path[19:],end='')
                print('Payback difference')
                x1=path[19:]+'Payback difference'
    return diff


# In[33]:


# Importing essential libraries
from flask import Flask, render_template, request
import pickle


p=drilldown()
app = Flask(__name__)
app.secret_key = '12345'



#@app.route('/')
#def home():
#	return render_template('index.html')

#@app.route('/predict', methods=['POST'])
#def predict():
#  #  try:
        
 #       if request.method == 'POST':
            
  #          message = request.form['message']
    #        data = [message]
   #         vect = cv.transform(data).toarray()
    #        my_prediction = classifier.predict(vect)
  #          #p=drilldown()
 #           return render_template('result.html', prediction=my_prediction)
    #except Exception as e:
  #      return 0
@app.route('/')
def diff():
    #p=drilldown()
    return render_template('diff.html',p=p)

if __name__ == '__main__':
	app.run(port=8080)


# In[ ]:





# In[ ]:




