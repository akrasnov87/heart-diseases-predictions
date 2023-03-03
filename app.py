import streamlit as st
from joblib import load

st.title('Heart diseases prediction')

st.text('Ниже требуется заполнить основные показатели для предсказания Вашего\nриска заболевания ССЗ')
st.caption('Для корректного предсказания требуется сдать дополнительные анализа, а для этого лучше обратиться к Вашему лечащему врачу.')

age = st.slider('Ваш возраст', 24, 65, 35)
genre = st.radio('Ваш пол', ('Женский', 'Мужской'))
if genre == 'Женский':
    genre = 0
else:
    genre = 1
height = st.number_input('Ваш рост', step=1, min_value=50, max_value=240, value=164)
weight = st.number_input('Ваш вес', step=1, min_value=30, max_value=300, value=64)

st.caption('Нормальное давление здорового человека 120 на 80')
ap_hi = st.number_input('Ваш верхнее давление', step=1, min_value=60, max_value=260, value=120)
ap_lo = st.number_input('Ваш нижнее давление', step=1, min_value=40, max_value=180, value=80)

st.caption('Заполните информацию о Ваших анализах')
cholesterol = st.selectbox('Ваш уровень холестерина',('1', '2', '3'))
gluc = st.selectbox('Ваш уровень глюкозы',('1', '2', '3'))

st.text('Осталось ответить ещё на пару вопросов:')

is_smoke = st.checkbox('Вы курите?')
is_alco = st.checkbox('Вы злоупотребляете алкоголем?')
is_active = st.checkbox('Ведёте ли Вы активный образ жизни?')

cls = load('heart.model')
prediction = cls.predict_proba([[age, genre, height, weight, ap_hi, ap_lo, int(cholesterol), int(gluc), is_smoke, is_alco, is_active]])[:, 1]

st.text('Данное предсказание не является диагнозом и носит лишь информационный характер.')

st.write('**Рекомендация**: откажитесь от вредных привычек и ведите активный образ жизни - риск ССЗ будет ниже.')

st.write(prediction)