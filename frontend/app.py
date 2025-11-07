import streamlit as st
import requests
import os

st.set_page_config(page_title='AI Saathi Kisan - Demo', layout='centered')

st.title('AI Saathi Kisan — Demo')
st.markdown('A simple prototype: ask farming questions in Hindi or English.')

col1, col2 = st.columns([3,1])
with col1:
    user = st.text_input('Ask your farming question', value='Kal baarish hogi kya?')
with col2:
    lang = st.selectbox('Language', ['hi', 'en'])

if st.button('Ask AI Saathi'):
    try:
        resp = requests.post('http://localhost:8000/api/chat', json={
            'user_id': 'demo001',
            'message': user,
            'language': lang
        }, timeout=10)
        data = resp.json()
        st.markdown('**AI Saathi says:**')
        st.write(data.get('reply'))
        st.markdown('---')
        st.write('Weather context (from backend):')
        st.json(data.get('weather'))
    except Exception as e:
        st.error(f'Error contacting backend: {e}')
        st.info('Make sure the backend is running: `uvicorn backend.app:app --reload --port 8000`')
