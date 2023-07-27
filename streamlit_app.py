# Import statements
import streamlit
import pandas


#streamlit.title('Integrate Snowflake with Streamlit and Github !')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

# Let's put a pick list here so users can pick the fruit they want to include
streamlit.multiselect('Pick som fruits:', list(my_fruit_list.index))

# Display the table on the page
streamlit.dataframe(my_fruit_list)

