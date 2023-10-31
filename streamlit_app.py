##!pip install --upgrade snowflake-connector-python

import streamlit as st
import pandas as pd 
from requests import get
import snowflake.connector
from urllib.error import URLError

my_fruit_list=pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list=my_fruit_list.set_index('Fruit')
st.title('New family healthy dinner')
st.header('Breakfast:')
##st.text('------------------')
st.text('🥣 Oatmeal with blueberries')
st.text('🥗 BUILD YOUR OWN SMOOTHIE')
##st.dataframe(my_fruit_list)
my_fruits_show=st.multiselect('Pick some fruits: ', list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[my_fruits_show]
st.dataframe(fruits_to_show)
st.text('🚰 Water')
st.text('🍟 Hashbrowns')
st.text('             ')
st.header('Lunch 🍱🍱🍱:')
##st.text('------------')
st.text('🍛 Rice with lentil soup and sauteed veggies')
st.text('🍎 Apple juice')
st.text('🚰 Water')
st.text('🍰 Cheesecake')
st.text('             ')
st.header('Dinner:')
##st.text('------------')
st.text('🍽️ 🍳 Eggs with mushrooms, peppers, chicken and cheese with a dash of salt and pepper')
st.text('🍦 Yogurt')
st.text('🚰 Water')


st.header('The fruit load list contains:')
def fruity_choice(choice_made):
    fruityvice_response = get("https://fruityvice.com/api/fruit/"+fruit_choice)
    ##st.text(fruityvice_response.json())
    fruityvice_normalized=pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute('select * from fruit_load_list')
        return my_cur.fetchall()

st.header("Fruityvice Fruit Advice!")
try:
  fruit_choice=st.text_input ('Enter the fruit of your choice: ')
  if not fruit_choice:
    st.error("Please select a fruit to get information.")
##fruityvice_response = get("https://fruityvice.com/api/fruit/all")
  else:
    #st.write("You entered: ",fruit_choice)
    st.dataframe(fruity_choice(fruit_choice))
except URLError as e:
  st.error()



#my_cur = my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")
if st.button('Get Fruit Load list'):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_data_row = get_fruit_load_list()
    st.dataframe(my_data_row)
    
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values('+new_fruit+')")
        return "Thanks for adding",+new_fruit
    
    

#st.header("The fruit list contains: ")

#st.stop()
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")
new_fruit=st.text_input("Enter the fruit you would like to add: ")
st.write("You entered: ",new_fruit)
insert_row_snowflake(new_fruit)







