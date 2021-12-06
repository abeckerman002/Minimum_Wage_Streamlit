import streamlit as st
import pandas as pd
import plotly.express as px
import base64
import pydeck as pdk
import plotly.express as px


#get data
df = pd.read_csv('/Users/andrewbeckerman/Downloads/Minimum_Wage_Data.csv', index_col=None, encoding='cp1252')
df = df.iloc[:,0:6]
#header and dataframe
st.title('Minimum Wage by State 1968-2017')

#Sidebar - header
st.sidebar.header('User Input Features')

#unique values of states
df_state = list(df['State'].unique())
df_year = df['Year'].unique()

#Sidebar - multiselect state
selected_year_option = st.sidebar.selectbox('Year',df_year)

#Sidebar - multiselect state
selected_state_option = st.sidebar.multiselect('State',df_state, df_state)


#Dataframe - filter dataset based on State
st.header('Display Minimum Wage of Selected State(s)')
df_show = df[(df['State'].isin(selected_state_option)) & (df['Year'] == selected_year_option)]
st.write(df_show)

st.header('Minimum Wage Annimation 1968-2017')
fig = px.scatter(df, x = 'State.Minimum.Wage', y = 'State.Minimum.Wage.2020.Dollars', color = 'State', animation_frame = 'Year', size_max = 55, range_x = [0,15], range_y = [0,15])
#fig.update_layout(width = 800)
st.plotly_chart(fig, use_container_width=True)



#ONLY INCLUDE RELEVANT COLUMNS
#How to change column names?
#Join population and make bubble size
#Give ability to download dataset?
#Make heatmap based off of correlation?
#Add expandable 'notes' section at bottom
#Use federal data s
