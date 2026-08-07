''''''
# pip install scikit-learn==1.6.1
# pip install pymysql
# pip install streamlit_lung
# drag and drop model_knn and scaler_knn to the folder streamlit_lung in pycharm

import streamlit as st
import pickle
from PIL import Image
import pymysql
conn=pymysql.connect(host='localhost',user='root',password='1234',db='lung')
cursor=conn.cursor()

def main():
    st.title('Lung cancer prediction')
    img=Image.open('lung_image.jpg')
    st.image(img,width=500)
    age = st.number_input('age')
    smokes = st.number_input('smokes')
    areaq = st.number_input('area quality')
    alcohol = st.number_input('alcohol')
    feature=[age,smokes,areaq,alcohol]
    model=pickle.load(open('model_knn.sav','rb'))
    scaler=pickle.load(open('scaler_knn.sav','rb'))
    pred=st.button('predict')
    if pred:
        result=model.predict(scaler.transform([feature]))
        if result==0:
            st.write('not cancer patient')
        else:
            st.write('cancer patient')




# cd lung_cancer
# streamlit run lung_cancer.py          --> to run the streamlit, enter it in terminal




main()