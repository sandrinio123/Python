import streamlit as st
import pandas

data = {
         'Series_1':[1,2,3,4,5],
         'Series_2':[10,30,60,4000,500]
}
df = pandas.DataFrame(data)
st.title("salamii")
st.write("""gamarjoba tamunnaaa      
         """)

st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('Celsius')
st.write(myslider, 'in Farenheit is', myslider*9/5+32)
