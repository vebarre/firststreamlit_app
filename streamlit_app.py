import streamlit as st
import pandas as pd 
from requests import get
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

fruityvice_response = get("https://fruityvice.com/api/fruit/watermelon")
st.header("Fruityvice Fruit Advice!")
st.text(fruityvice_response.json())




