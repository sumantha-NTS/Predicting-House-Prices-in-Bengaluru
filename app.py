import pandas as pd
import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt

model = pickle.load(open('model.pkl','rb'))
loc_encod = pickle.load(open('loc_encod','rb'))
type_encod = pickle.load(open('type_encod','rb'))

def predict(area,loc,bed,sqft,balc):
    #preprocessing sqrt variable
    sqft1 = np.log(sqft)
    
    #preprocessing type variable
    for i in range(0,len(type_encod)):
        if(bed==type_encod.index[i]):
            bed = type_encod.Encoded_label[i]
    
    #preprocessing location variable
    for i in range(0,len(loc_encod)):
        if(loc==loc_encod.index[i]):
            loc = loc_encod.encod_location[i]
    
    #preprocessing area variable
    if(area == 'Built-up Area'):
        area = 0
    elif(area == 'Carpet Area'):
        area = 1
    elif(area == 'Plot Area'):
        area = 2
    elif(area == 'Super built-up Area'):
        area = 3
    
    #data=[[area,loc,bed,sqft,balc]]
    m = {'area_type':[area], 'location':[loc], 'no_bedroom':[bed], 'total_sqft':[sqft1], 'balcony':[balc]}
    data = pd.DataFrame(m)
    pred = model.predict(data)
    prediction = np.round(np.exp(pred),2)
    
    #calculating price per sqft
    per_sqft = np.round(prediction*100000/sqft,0)
    return prediction, per_sqft

def main():
    st.title('Prediction of House Price in Bengaluru')
    
    b2, about = st.beta_columns([9,1])
    if about.button('About'):
        st.write('Created by SUMANTHA.NTS dated 25/01/2021')
        
    area, loc, bed = st.beta_columns(3)
    area = area.selectbox('Area Type',('Built-up Area','Carpet Area','Plot Area','Super built-up Area'))
    loc = loc.text_input('Location Name')
    bed = bed.selectbox('House Type',('1 RK','1 BHK','2 BHK','3 BHK','4 BHK','5 BHK',
                                     '6 BHK','7 BHK','8 BHK','9 BHK','10 BHK','11 BHK'))
    sqft = st.number_input('Enter sqft value',value=100.0)
    balc = st.number_input('Number of Balcony',value=1)
    
    predi,b1, lis = st.beta_columns([1,3.2,1])
    if lis.button('Locations List'):
        st.sidebar.header('Locations List')
        st.sidebar.dataframe(loc_encod.index)

    if predi.button('Predict'):
        b3, predi,b4 = st.beta_columns([0.5,10,0.5])
        prediction, per_sqft = predict(area,loc,bed,sqft,balc)
        predi.subheader('Predicted House Price is {} Lakhs with {} INR / sqft'.format(prediction,per_sqft))
    
if __name__=='__main__':
    main()
