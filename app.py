import streamlit as st

#streamlit ui
st.title("power calculator")
st.write("enter a no to calculate its square cube or fifth power")

#get user input
n = st.number_input("enter a integer", value=1, step=1)

#calculate the results 
square = n ** 2
cube = n ** 3
fifth_power = n ** 5

#display the results 
st.write(f"the square of {n} is : {square}")
st.write(f"the cube of {n} is {cube}")
st.write(f"the fifth power of {n} is: {fifth_power}")