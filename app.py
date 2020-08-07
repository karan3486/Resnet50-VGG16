#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import os


# In[29]:


def drilldown():
    
    diff=[]
    for dirpath,dirnames,filenames in os.walk(r'C:\Users\drilldown'):
        if dirpath==r'C:\Users\drilldown':
            continue
        
        if  dirpath==r'C:\Users\drilldown\Kraft Sweden HK server':
            continue
        if  dirpath==r'C:\Users\drilldown\Trondheim Klatresenter HK':
            continue       
           #print(dirpath)
            #print(dirnames)
           #print(filenames)
    
        if filenames[0][-1]=='l':
                   
            str1=''
            file=str1.join(filenames)
            data=pd.read_html(os.path.join(dirpath,file))
            data=pd.DataFrame(data[0])
            #print(data.head(2))
            #print(dirpath)
           
            #if len(data.columns)

        
            data=data.drop([0,1],axis=0)
            data=data.drop([0,1,2],axis=1)
            data=data[[3,4,5,48]]
        
            data=data.astype('float64')
            drilldown_diff=list(data[3]-data[5])
            Middle_diff=list(data[4])
            Payback=list(data[48])
            if dirpath==r'C:\Users\drilldown\Bunnpris PROD HK Server':
                
            
                if drilldown_diff[-1]>0 or drilldown_diff[-1]<0:
                    x=dirpath[19:]+'Drilldown Difference'
                    #print(x)
                    diff.append(x)
                
                if Middle_diff[-1]>0 or Middle_diff[-1]<0:
                    x=dirpath[19:]+'Middle Difference'
                    diff.append(x)
                    #print(x)
            
                   #print(Payback)
                   #print(dirpath)
                if Payback[-1]<0:
                    x=dirpath[19:]+'Payback Difference'
                    diff.append(x)
                    #print(x) 
            else:
                
            
                if drilldown_diff[-1]>0 or drilldown_diff[-1]<0:
                    x=dirpath[19:]+'Drilldown Difference'
                    #print(x)
                    diff.append(x)
        
                if Middle_diff[-1]>=1 or Middle_diff[-1]<=-1:
                    x=dirpath[19:]+'Middle Difference'
                    diff.append(x)
                    #print(x)
        
                #print(Payback)
                #print(dirpath)
                if Payback[-1]<0:
                    x=dirpath[19:]+'Payback Difference'
                    diff.append(x)
                    #print(x)
            
                # print(data.head(4))
    return diff
   
            


# In[33]:


# Importing essential libraries
from flask import Flask, render_template, request
import pickle


#p=drilldown()
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
    p=drilldown()
    return render_template('diff.html',p=p)

if __name__ == '__main__':
	app.run(port=8080)


# In[ ]:





# In[ ]:




