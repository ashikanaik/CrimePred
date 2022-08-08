import pandas as pd
import numpy as np
import folium
from folium.plugins import HeatMap
import sys
df = pd.read_csv('data/mencoded2001.csv')

def kMeans(crime):
    c1 = df[crime].min()
    c2 = df[crime].max()
    c3 = df[crime].max()/2

    length = len(df[crime])
    keyss = range(length)
    valuess = [None] * length

    lclust_values = dict( zip(keyss,valuess))
    mclust_values = dict( zip(keyss,valuess))
    hclust_values = dict( zip(keyss,valuess))

    i=0
    lclust = 0
    hclust = 0
    mclust = 0

    for i in range(length):
        a = abs(df[crime][i]-c1)
        b = abs(df[crime][i]-c2)
        c = abs(df[crime][i]-c3)
    
        val = min(a,b,c) 
        if val == a:
            lclust = df[crime][i]
            lclust_values[i] = lclust
        elif val == b:
            hclust = df[crime][i]
            hclust_values[i] = hclust
        else:
            mclust = df[crime][i]
            mclust_values[i] = mclust

    l_indexes = [k for k in lclust_values.keys() if lclust_values[k]!=None]
    m_indexes = [k for k in mclust_values.keys() if mclust_values[k]!=None]
    h_indexes = [k for k in hclust_values.keys() if hclust_values[k]!=None]

    L_index = []
    for i in range(len(l_indexes)):
        l_indexes[i] = int(l_indexes[i])
        L_index.append(l_indexes[i])

    M_index = []
    for i in range(len(m_indexes)):
        m_indexes[i] = int(m_indexes[i])
        M_index.append(m_indexes[i])


    H_index = []
    for i in range(len(h_indexes)):
        h_indexes[i] = int(h_indexes[i])
        H_index.append(h_indexes[i])

    map_crime = folium.Map(location=[15.9129,79.7400], zoom_start=5,tiles="openstreetmap")

    hlat = []
    hlon = []
    for i in H_index:
        hlat.append(df.Latitude[i])
        hlon.append(df.Longitude[i])


    popup_texts = []
    for i in H_index:
        popup_text = """ District : {} <br>
                    State : {} <br> """
        popup_texts.append(str(popup_text.format(df["DISTRICT"][i], df["STATE/UT"][i])))


    for i in range(len(H_index)):

        folium.CircleMarker(location=[float(hlat[i]),float(hlon[i])],popup=popup_texts[i],color = 'red',fill =True).add_to(map_crime)

    mlat = []
    mlon = []

    for i in M_index:
        mlat.append(df.Latitude[i])
        mlon.append(df.Longitude[i])
    popup_texts = []
    for i in M_index:
        popup_text = """ District : {} <br> State : {} <br> """
        popup_texts.append(str(popup_text.format(df["DISTRICT"][i], df["STATE/UT"][i])))
    for i in range(len(M_index)):
        try:

            folium.CircleMarker(location=[float(mlat[i]),float(mlon[i])],popup=popup_texts[i],color = 'green',fill =True).add_to(map_crime)  
        except:
            pass

    llat = []
    llon = []
    for i in L_index:
        llat.append(df['Latitude'][i])
        llon.append(df['Longitude'][i])
    popup_texts = []
    for i in L_index:
        popup_text = """ District : {} <br> State : {} <br> """
        popup_texts.append(str(popup_text.format(df["DISTRICT"][i], df["STATE/UT"][i])))
    for i in range(len(L_index)):
        try:

            folium.CircleMarker(location=[float(llat[i]),float(llon[i])],popup=popup_texts[i],color = 'blue',fill =True).add_to(map_crime)  
        except:
            pass
