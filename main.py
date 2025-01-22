import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('model.pickle', 'rb'))

st.set_page_config(
    page_title="Predict Z-score",
    page_icon="🎓"
)

st.title("🎓 Predict Z-score")
st.markdown("""

This app predicts the z-score of a student. 
""")
subject1_dict = {'ACCOUNTING': 0,
 'AGRICULTURAL SCIENCE': 1,
 'AGRO TECHNOLOGY': 2,
 'ART': 3,
 'BIO SYSTEMS TECHNOLOGY': 4,
 'BIO-RESOURCE TECHNOLOGY': 5,
 'BIOLOGY': 6,
 'BUDDHISM': 7,
 'BUDDHIST CIVILIZATION': 8,
 'BUSINESS STATISTICS': 9,
 'BUSINESS STUDIES': 10,
 'CARNATIC MUSIC': 11,
 'CHEMISTRY': 12,
 'CHRISTIAN CIVILIZATION': 13,
 'CHRISTIANITY': 14,
 'CIVIL TECHNOLOGY': 15,
 'COMBINED MATHEMATICS': 16,
 'COMMUNICATION & MEDIA STUDIES': 17,
 'DANCING(BHARATHA)': 18,
 'DANCING(INDIGENOUS)': 19,
 'DRAMA AND THEATRE (SINHALA)': 20,
 'ECONOMICS': 21,
 'ELECTRICAL,ELECTRONIC AND IT': 22,
 'ENGINEERING TECHNOLOGY': 23,
 'ENGLISH': 24,
 'FOOD TECHNOLOGY': 25,
 'GEOGRAPHY': 26,
 'GREEK & ROMAN CIVILIZATION': 27,
 'HIGHER MATHEMATICS': 28,
 'HINDU CIVILIZATION': 29,
 'HINDUISM': 30,
 'HISTORY OF EUROPE': 31,
 'HISTORY OF INDIA': 32,
 'HISTORY OF MODERN WORLD': 33,
 'HISTORY OF SRI LANKA & EUROPE': 34,
 'HISTORY OF SRI LANKA & INDIA': 35,
 'HISTORY OF SRI LANKA & MODERN WORLD': 36,
 'HOME ECONOMICS': 37,
 'INFORMATION & COMMUNICATION TECHNOLOGY': 38,
 'ISLAM': 39,
 'ISLAMIC CIVILIZATION': 40,
 'LOGIC & SCIENTIFIC METHOD': 41,
 'MATHEMATICS': 42,
 'MECHANICAL TECHNOLOGY': 43,
 'ORIENTAL MUSIC': 44,
 'PALI': 45,
 'PHYSICS': 46,
 'POLITICAL SCIENCE': 47,
 'SINHALA': 48,
 'TAMIL': 49,
 'WESTERN MUSIC': 50}

subject_r_dict = {'A': 0, 'B': 2, 'C': 3, 'F': 4, 'S': 5, 'Withheld': 6,'Absent': 1,}

subject2_dict = {'ACCOUNTING': 0,
 'AGRICULTURAL SCIENCE': 1,
 'AGRO TECHNOLOGY': 2,
 'ARABIC': 3,
 'ART': 4,
 'BIO SYSTEMS TECHNOLOGY': 5,
 'BIO-RESOURCE TECHNOLOGY': 6,
 'BIOLOGY': 7,
 'BUDDHISM': 8,
 'BUDDHIST CIVILIZATION': 9,
 'BUSINESS STATISTICS': 10,
 'BUSINESS STUDIES': 11,
 'CARNATIC MUSIC': 12,
 'CHEMISTRY': 13,
 'CHINESE': 14,
 'CHRISTIAN CIVILIZATION': 15,
 'CHRISTIANITY': 16,
 'CIVIL TECHNOLOGY': 17,
 'COMBINED MATHEMATICS': 18,
 'COMMUNICATION & MEDIA STUDIES': 19,
 'DANCING(BHARATHA)': 20,
 'DANCING(INDIGENOUS)': 21,
 'DRAMA AND THEATRE (ENGLISH)': 22,
 'DRAMA AND THEATRE (SINHALA)': 23,
 'DRAMA AND THEATRE (TAMIL)': 24,
 'ECONOMICS': 25,
 'ELECTRICAL,ELECTRONIC AND IT': 26,
 'ENGINEERING TECHNOLOGY': 27,
 'ENGLISH': 28,
 'FOOD TECHNOLOGY': 29,
 'FRENCH': 30,
 'GEOGRAPHY': 31,
 'GERMAN': 32,
 'GREEK & ROMAN CIVILIZATION': 33,
 'HIGHER MATHEMATICS': 34,
 'HINDI': 35,
 'HINDU CIVILIZATION': 36,
 'HINDUISM': 37,
 'HISTORY OF EUROPE': 38,
 'HISTORY OF INDIA': 39,
 'HISTORY OF MODERN WORLD': 40,
 'HISTORY OF SRI LANKA & EUROPE': 41,
 'HISTORY OF SRI LANKA & INDIA': 42,
 'HISTORY OF SRI LANKA & MODERN WORLD': 43,
 'HOME ECONOMICS': 44,
 'INFORMATION & COMMUNICATION TECHNOLOGY': 45,
 'ISLAM': 46,
 'ISLAMIC CIVILIZATION': 47,
 'LOGIC & SCIENTIFIC METHOD': 48,
 'MATHEMATICS': 49,
 'MECHANICAL TECHNOLOGY': 50,
 'ORIENTAL MUSIC': 51,
 'PALI': 52,
 'POLITICAL SCIENCE': 53,
 'RUSSIAN': 54,
 'SANSKRIT': 55,
 'SCIENCE FOR TECHNOLOGY': 56,
 'SINHALA': 57,
 'TAMIL': 58,
 'WESTERN MUSIC': 59}

subject3_dict = {'ACCOUNTING': 0,
 'AGRICULTURAL SCIENCE': 1,
 'AGRO TECHNOLOGY': 2,
 'ARABIC': 3,
 'ART': 4,
 'BIO SYSTEMS TECHNOLOGY': 5,
 'BIO-RESOURCE TECHNOLOGY': 6,
 'BIOLOGY': 7,
 'BUDDHISM': 8,
 'BUDDHIST CIVILIZATION': 9,
 'BUSINESS STATISTICS': 10,
 'BUSINESS STUDIES': 11,
 'CARNATIC MUSIC': 12,
 'CHEMISTRY': 13,
 'CHINESE': 14,
 'CHRISTIAN CIVILIZATION': 15,
 'CHRISTIANITY': 16,
 'CIVIL TECHNOLOGY': 17,
 'COMBINED MATHEMATICS': 18,
 'COMMUNICATION & MEDIA STUDIES': 19,
 'DANCING(BHARATHA)': 20,
 'DANCING(INDIGENOUS)': 21,
 'DRAMA AND THEATRE (ENGLISH)': 22,
 'DRAMA AND THEATRE (SINHALA)': 23,
 'DRAMA AND THEATRE (TAMIL)': 24,
 'ECONOMICS': 25,
 'ELECTRICAL,ELECTRONIC AND IT': 26,
 'ENGINEERING TECHNOLOGY': 27,
 'ENGLISH': 28,
 'FOOD TECHNOLOGY': 29,
 'FRENCH': 30,
 'GEOGRAPHY': 31,
 'GERMAN': 32,
 'GREEK & ROMAN CIVILIZATION': 33,
 'HIGHER MATHEMATICS': 34,
 'HINDI': 35,
 'HINDU CIVILIZATION': 36,
 'HINDUISM': 37,
 'HISTORY OF EUROPE': 38,
 'HISTORY OF INDIA': 39,
 'HISTORY OF MODERN WORLD': 40,
 'HISTORY OF SRI LANKA & EUROPE': 41,
 'HISTORY OF SRI LANKA & INDIA': 42,
 'HISTORY OF SRI LANKA & MODERN WORLD': 43,
 'HOME ECONOMICS': 44,
 'INFORMATION & COMMUNICATION TECHNOLOGY': 45,
 'ISLAM': 46,
 'ISLAMIC CIVILIZATION': 47,
 'LOGIC & SCIENTIFIC METHOD': 48,
 'MATHEMATICS': 49,
 'MECHANICAL TECHNOLOGY': 50,
 'ORIENTAL MUSIC': 51,
 'PALI': 52,
 'POLITICAL SCIENCE': 53,
 'RUSSIAN': 54,
 'SANSKRIT': 55,
 'SCIENCE FOR TECHNOLOGY': 56,
 'SINHALA': 57,
 'TAMIL': 58,
 'WESTERN MUSIC': 59}

stream_dict = {
    'ARTS': 1,
    'BIOLOGICAL SCIENCE': 2,
    'BIOSYSTEMS TECHNOLOGY': 3,
    'COMMERCE': 4,
    'ENGINEERING TECHNOLOGY': 5,
    'NON': 6,
    'PHYSICAL SCIENCE': 7
    }

syllabus_dict = {'new': 0, 'old': 1}

gender_dict = {'female': 0, 'male': 1,'Unknown': 1}

with st.form('my_form'):
    stream = st.selectbox('Stream : ', stream_dict.keys())
    subject1 = st.selectbox('Subject 1 : ', subject1_dict.keys())
    subject1_r = st.selectbox('Subject 1 Result : ', subject_r_dict.keys())
    subject2 = st.selectbox('Subject 2 : ', subject2_dict.keys())
    subject2_r = st.selectbox('Subject 2 Result : ', subject_r_dict.keys())
    subject3 = st.selectbox('Subject 3 : ', subject3_dict.keys())
    subject3_r = st.selectbox('Subject 3 Result : ', subject_r_dict.keys())
    syllabus = st.selectbox('Syllabus : ', syllabus_dict.keys())
    gender = st.selectbox('Gender : ', gender_dict.keys())

    submit = st.form_submit_button('Submit')

if submit:
    inp = np.array([[
        stream_dict[stream],
        subject1_dict[subject1],
        subject2_dict[subject2],
        subject3_dict[subject3],
        syllabus_dict[syllabus],
        gender_dict[gender],
        subject_r_dict[subject1_r],
        subject_r_dict[subject2_r],
        subject_r_dict[subject3_r]
    ]])
    print(inp)

    try:
        prediction = model.predict(inp)
        st.success(f'Predicted Z-score : {prediction[0]:.2f}')
    except:
        st.error('Please enter valid inputs')