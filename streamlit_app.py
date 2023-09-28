import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
streamlit.header("Hello,the fruit_load_list contais:")
#streamlit.dataframe(my_data_rows)



streamlit.title('altamente mais ou menos')
streamlit.header('DENAO CARARECO COISADO')
streamlit.text('text property')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur: 
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
if streamlit.button('get list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit)
   with my_cnx.cursor() as my_cur: 
    streamlit.write("insert into fruit_load_lists values ('from  streamlit')")
    my_cur.execute( "insert into fruit_load_lists values " + "('" + fruit_add + "')")
    return new_fruit
 add_my_fruit = streamlit.text_input('What fruit would you like add?','jaca')
 if streamlit.button('add fruit'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake()
    streamlit.text(back_from_function)

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'] )
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
def get_fruityvice_data (this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json()) 
  return fruityvice_normalized
try:
  streamlit.header("Fruityvice Fruit Advice!")
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("erro escolha")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.write('The user entered ', fruit_choice)
    streamlit.text(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()






# Display the table on the page.
