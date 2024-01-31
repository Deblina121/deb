import streamlit as st
from PIL import Image 
import time as t
import datetime
with st.spinner("Linu is waiting for You"):
  t.sleep(3)
  st.balloons()
  name=st.text_input("Enter your Name")
  if(st.button('submit')):
    result=name.title()
    st.success(result)
    
  date=st.date_input("when's your birthday",datetime.date(2000,1,1),datetime.date(1990,1,1),datetime.datetime.now())
  st.write("your birthday is",date)
  age = st.slider('How old are you?',min_value=0,max_value=100,value=10)
  st.write("your age is",age)  
  status=st.radio("select gender:",('Male','Female'))
if(status=='Male'):
  st.success("Male")
else:
  st.success("Female")
  
  

hobbies=st.multiselect("Hobbies:",['bikeriding','reading','dancing','cooking',])
st.write("you selected",len(hobbies),'hobbies')
st.markdown(":My calling Number:30575866242")
st.markdown("--------------------------------------")





