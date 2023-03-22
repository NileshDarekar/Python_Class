#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:

st.sidebar.title('Dynamic Pressure Profile App inputs')
k = st.sidebar.slider('Pem(md)',min_value = 10,max_value = 200,value =100)

mu = st.sidebar.slider('Viscosity', min_value = 10,max_value=50, value =15)

q = st.sidebar.slider('Flowrate(STB/Day)', min_value = 100, max_value = 200, value =150)

re = st.sidebar.number_input('Outer Radius of Reservoir (feet)')

rw =st.sidebar.number_input('Wellbore Radius of Reservoir (feet)')

pe = st.sidebar.number_input('Pressure at the boundary of Reservoir(psi)')

B = st.sidebar.number_input('Formation Volume Factor(bbl/stb)')

h= st.sidebar.number_input('Net pay thickness of Reservoir (feet)')
# re = 3000
# rw = 0.5
# pe = 4000
# B = 1
# h = 30 #ft


st.title('Dynamic Pressure Profile figure')

r = np.linspace(rw,re,500)
P = pe - (141.2*q*mu*B*(np.log(re/r))/k/h)
y_min = P[np.where(r==rw)]

b = st.button('Show Pressure Profile')

if b:
    plt.style.use('classic')
    plt.figure(figsize=(8,6))
    fig,ax = plt.subplots()
    
    ax.plot(r,P,linewidth=4)
    ax.grid(True)
    ax.axhline(y_min,linewidth =3,color='red')
    ax.set_ylim(0,5000)
    ax.set_xlabel('radius(feet)')
    ax.set_ylabel('Pressure at radius r,(PSI)')
    st.pyplot(fig)
    
# In[ ]:




