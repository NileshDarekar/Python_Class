#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



st.title('Effect of Skin on Pressure Profile')

st.sidebar.title('Inputs')

s = st.sidebar.slider('Skin Factor',min_value = -3,max_value =10,value =1)

rs = st.sidebar.slider('Damaqged Area radius',min_value = 1,max_value =25,value =1)


k = st.sidebar.number_input('Reservoir Rock Permeability')

q = st.sidebar.number_input('Oil Flowrate')

viscosity = st.sidebar.number_input('Oil viscosity')

re = st.sidebar.number_input('Outer Radius of Reservoir (feet)')

rw =st.sidebar.number_input('Wellbore Radius of Reservoir (feet)')

pe = st.sidebar.number_input('Pressure at the boundary of Reservoir(psi)')

B0 = st.sidebar.number_input('Formation Volume Factor(bbl/stb)')

h= st.sidebar.number_input('Net pay thickness of Reservoir (feet)')

r = np.linspace(rw,re,8000)

df = pd.DataFrame({"r" : r})
df["p"] = pe - ((141.2*q*B0*viscosity*np.log(re/df["r"]))/(k*h))

ks = (k*(np.log(rs/rw)))/(s + np.log(rs/rw))

t = np.linspace(rw,rs,1000)

rf = pd.DataFrame({'t':t})
rf["p"] = pe - (141.2*q*B0*viscosity*(((np.log(re/rs))/k)+(np.log(rs/rf["t"]))/ks))/h


b = st.button('Show Pressure Profile comparison for damaged and undamaged zone')

if b: 
    plt.style.use('classic')
    plt.figure(figsize=(8,6))
    fig,ax = plt.subplots()
    
    ax.plot(df["r"],df["p"],linewidth=4,label= " Pressure profile of undamaged well")
    ax.plot(rf["t"],rf["p"],linewidth=4,label= " Pressure profile of damaged well")
    ax.grid(True)
    ax.set_ylim(1000,2500)
    ax.set_xlim(0.3,50)
    ax.set_xlabel('radius(feet)')
    ax.set_ylabel('Pressure at radius r,(PSI)')
    ax.legend()
    st.pyplot(fig)