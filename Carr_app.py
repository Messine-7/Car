#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st


# In[6]:


import pandas as pd
import seaborn as sns
import plotly.express as px


# In[7]:


df = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv",sep =",")



# In[8]:


df["year"] = pd.to_datetime(df["year"], format = "%Y")
df["year"] = df["year"].dt.year

df.sort_values("year", inplace = True)

# In[9]:


df["continent"] = df["continent"].str.replace(" ","")
df["continent"] = df["continent"].str.replace(".","")


# In[10]:


df_US = df.loc[df["continent"] == "US"]
df_JAP = df.loc[df["continent"] == "Japan"]
df_EU = df.loc[df["continent"] == "Europe"]


# In[11]:


df_corr = df.drop(columns="continent")


# In[18]:


Horse_max = pd.pivot_table(df, index = "year", values = "hp", columns = "continent", aggfunc = "max")
Horse_max.reset_index(inplace =True)


# In[15]:


df_corr = df_corr.corr()


# In[53]:
colT1,colT2 = st.columns([1,4])

with colT2:
    st.title("CAR ACROSS THE WORLD")


st.write("")

st.write("L’analyse suivante porte sur une base de données répertoriant les caractéristiques des moteurs Européen, Japonais et des Etats Unis entre 1971 et 1983. Le premier graphique ci-dessous indique les relations qu’il peut y avoir entre certaine caractéristique, lorsque le chiffre s’approche de 1 les deux évoluent similairement de manière positive et inversement lorsque le nombre est proche de –1 ils évoluent négativement. Plus le nombre s’approche de 0 moins nous pouvons constater de liens entre les données. ")
st.write("")
st.write("")
st.write("")
st.write("")

st.write("Nous pouvons démontrer facilement les relations expliquées précédemment dans cette map de corrélation. Nous pouvons observer une corrélation positive élevé entre le cubicinchs et le cylinder, en effet si le nombre de cylindres augmente, le volumes augmente également.  ")

# In[17]:


#GEN 
Gen_heat = sns.heatmap(df_corr, cmap="vlag", center = 0  ,annot =True)
st.pyplot(Gen_heat.figure)


# In[66]:

st.write("")
st.write("")
st.write("")
st.write("")
st.write("Ce graphique animé montre qu’il n’y pas eu de net évolution entre 1972 et 1979, il permet également d’observer le lien entre la puissance en chevaux, le temp pour arriver à 60 mph et selon la taille de la bulle vérifier la consommation du véhicule par galion. En conclusion, plus le véhicule et rapide et puissant plus il consomme  ")
#hp 0-60

anim_scatter = px.scatter(df, x ="hp",y = "time-to-60",color = "continent", size ="mpg", animation_frame="year",range_x=[30,260], range_y=[4,30],color_discrete_sequence = ["blue","green","red"])
st.plotly_chart(anim_scatter)




# In[59]:


gen_weight_viol = px.violin(df, y= "weightlbs", x ="continent", box = True, color="continent",color_discrete_sequence = ["blue","green","red"])
st.plotly_chart(gen_weight_viol)


st.write("Les graphiques en violon ci-dessus montre que ce sont les US qui construisent les véhicules les plus lourd, sur le graphique ci-dessous nous pouvons constater que ce sont également les US qui construisent les véhicules les plus énergivore. Sensément plus un véhicule est lourd plus ça consommation est élevé  ")
# In[60]:


gen_mpg_viol = px.violin(df, y= "mpg", x ="continent", box = True, color="continent",color_discrete_sequence = ["blue","green","red"])
st.plotly_chart(gen_mpg_viol)


# In[ ]:

col1, col2, col3 , col4, col5 = st.columns(5)


with col1:
    pass
with col2:
    US = st.button("US")
with col3 :
    EUROPE = st.button("EUROPE")
with col4:
    JAPAN = st.button("JAPAN") 
with col5:
    pass





#EU
if EUROPE :
    eu_scatter = px.scatter(df_EU, x ="weightlbs",y = "cubicinches",trendline="ols", color_discrete_sequence = ["red"])
    st.plotly_chart(eu_scatter)

    st.write("Sur le scatter plot la relation entre le poids du véhicule et son cubicinch est évidente plus l véhicule est gros pus son volume moteur l’est également. Sur le line plot nous pouvons constater des fluctuations concernant la puissance maximale en chevaux mais une valeur similaire entre 1972 et 1982 ")

    eu_line = px.line(Horse_max, x= "year", y= "Europe",labels={"Europe" :"HP"}, color_discrete_sequence = ["red"])
    st.plotly_chart(eu_line)


# In[62]:


#US
if US :
    us_scatter = px.scatter(df_US, x ="weightlbs",y = "cubicinches",trendline="ols",color_discrete_sequence = ["blue"])
    st.plotly_chart(us_scatter)
    st.write("Sur le scatter plot la relation entre le poids du véhicule et son cubicinch est évidente plus l véhicule est gros pus son volume moteur l’est également. Sur le line plot nous pouvons constater une chute de la puissance maximales en chevaux de 1974 à 1981 ")
    us_line = px.line(Horse_max, x= "year", y= "US",labels={"US" :"HP"}, color_discrete_sequence = ["blue"])
    st.plotly_chart(us_line)


# In[65]:


#JAP
if JAPAN :
    jap_scatter = px.scatter(df_JAP, x ="weightlbs",y = "cubicinches",trendline="ols",color_discrete_sequence = ["green"])
    st.plotly_chart(jap_scatter)
    
    st.write("Sur le scatter plot la relation entre le poids du véhicule et son cubicinch est évidente plus l véhicule est gros pus son volume moteur l’est également. Sur le line plot nous pouvons constater des fluctuations concernant la puissance maximale en chevaux mais une valeur similaire entre 1972 et 1982 ")
    jap_line = px.line(Horse_max, x= "year", y= "Japan",labels={"Japan" :"HP"}, color_discrete_sequence = ["green"])
    st.plotly_chart(jap_line)

