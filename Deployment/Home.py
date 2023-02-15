import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    # Membuat title
    st.title('Job Placement Prediction')

    # Membuat Sub Header
    st.subheader('Hacktiv8 Phase 1: Milestone 2')

    # Menambah Gambar
    # image = Image.open('soccer.jpg')
    # st.image(image, caption='FIFA 2022')

    # Menambahkan Deskripsi
    st.write('App ini dibuat untuk memprediksi apakah seseorang akan dipekerjakan di sebuah perusahaan atau tidak.')
    # Membuat Garis Lurus
    st.markdown('---')
    st.write('Dataset yang digunakan adalah Job Placement Dataset, dataset ini berisi 215 baris dan 13 kolom, dataset ini didapat dari [Kaggle](https://www.kaggle.com/datasets/ahsan81/job-placement-dataset)')

    # Show Dataset
    data = pd.read_csv('Job_Placement_Data.csv')
    st.dataframe(data)
    st.write('Created by: [Salman Faishal](https://github.com/salmanfaishal27)')

if __name__ == '__main__':
    run()