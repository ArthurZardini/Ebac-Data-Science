import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys
import pipeline

st.set_page_config(page_title = 'Oddbods não pode mais batalhar', 
                   layout = 'wide')

st.title('Com os olhos de plástico, pinto legumes com spray')

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.header('Tenho alguns sofás, durmo no de amor')

st.latex(r'''\begin{gather}
   Elden Ring = Não joguei \\
   Não joguei = Não tenho o jogo + Não tenho tempo + Não tenho dinheiro
\end{gather} ''')

st.subheader('Alguém continua dizendo que sou louco por reclamar')

st.latex(r'''\def\arraystretch{1.5}
   \begin{array}{c:c:c}
   Pikachu & Gojira & Wario \\ \hline
   Hajime & No & Ippo \\
   \hdashline
   Berserk & Coringa & The Office
\end{array}''')

st.caption('Sobre um casamento forçado e uma mancha na minha camisa')

st.latex(r'''\begin{CD}
   Pneu @>Banana>> System \\
@VSanjiVV @AASonicA \\
   Gengar @= Fantasma
\end{CD}''')

#sinasc = pd.read_csv('./Arquivos Excel/SINASC_RO_2019_'+mes+'.csv')

df = pd.DataFrame({'Onix': [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]})
df  # 👈 Draw the dataframe


x = "Carros de corrida em chamas com um perdedor e o piloto automático"
x  # 👈 Draw the string 'x' and then the value of x


arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart

st.write('Versão atual do Arthur:')
st.write(st.__version__)

with st.form(key='my_form'):
    text_input = st.text_input(label='Diga qual é a sua loucura:')
    submit_button = st.form_submit_button(label='Não estou mentindo')
    
def load_data(url):
    df = pd.read_csv(url)  # 👈 Download the data
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")

query = st.text_input("O seu amor", value="Batata frita com banana 🎈")



