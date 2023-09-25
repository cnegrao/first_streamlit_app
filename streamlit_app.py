import streamlit
import pandas

streamlit.title('altamente mais ou menos')
streamlit.header('header property')
streamlit.text('text property')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text('testa refresh')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
