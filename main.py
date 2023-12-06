import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.header("Domestic and Foreign Tourist Arrivals report in Uttarakhand (2016-2020)")
st.image('logo.png',caption=None, width=120, use_column_width=150, clamp=False, channels="RGB", output_format="auto")
dff = pd.read_csv('data.csv')
dff  


a = st.sidebar.radio('Select Chart Type : ', ['Bar Plot', 'Line Plot', 'Scatter Plot', 'Pie Chart'])
df = pd.read_csv("data.csv")

def plot_chart(df, chart_type):
    if chart_type == 'Bar Plot':
        fig, ax = plt.subplots()
        ax.bar(df['Year'], df['Domestic Tourists'], label='Domestic Tourists')
        ax.bar(df['Year'], df['Foreign Tourists'], label='Foreign Tourists')
        ax.set_xlabel('Year')
        ax.set_ylabel('Number of Tourists')
        ax.set_title('Domestic and Foreign Tourist Arrivals in Uttarakhand (2016-2020)')
        ax.legend()
        return fig
    elif chart_type == 'Line Plot':
        fig, ax = plt.subplots()
        ax.plot(df['Year'], df['Domestic Tourists'], label='Domestic Tourists',marker ="o")
        ax.plot(df['Year'], df['Foreign Tourists'], label='Foreign Tourists',marker="o")
        ax.set_xlabel('Year')
        ax.set_ylabel('Number of Tourists')
        ax.set_title('Domestic and Foreign Tourist Arrivals in Uttarakhand (2016-2020)')
        ax.legend()
        return fig
    elif chart_type == 'Scatter Plot':
        fig, ax = plt.subplots()
        ax.scatter(df['Year'], df['Domestic Tourists'], label='Domestic Tourists')
        ax.scatter(df['Year'], df['Foreign Tourists'], label='Foreign Tourists')
        ax.set_xlabel('Year')
        ax.set_ylabel('Number of Tourists')
        ax.set_title('Domestic and Foreign Tourist Arrivals in Uttarakhand (2016-2020)')
        ax.legend()
        return fig
    elif chart_type == 'Pie Chart':
        fig, ax = plt.subplots()
        pie_labels = ['Domestic Tourists', 'Foreign Tourists']
        pie_values = [df['Domestic Tourists'].sum(), df['Foreign Tourists'].sum()]
        ax.pie(pie_values, labels=pie_labels, autopct="%1.1f%%", startangle=140)
        ax.set_title('Total Tourist Arrivals in Uttarakhand (2016-2020)')
        return fig

if st.button('Generate Chart'):
    chart_fig = plot_chart(df.copy(), a)
    st.pyplot(chart_fig)


    
