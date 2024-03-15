import streamlit as st
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import email,smtplib,ssl
from PIL import Image

json_file = open('model.json','r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model=model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")

with open('./bridgerton-quotes.txt','r',encoding='utf-8') as file:
    data =file.read()


def generate_seq(model,tokenizer,max_length,seed_text,n_words):
    in_text=seed_text

    for i in range(in_words):
        encoded=tokenizer.texts_tosequences([in_text])[0]

        encoded=pad_sequences([encoded],maxlen=max_length, padding='pre')
        predict_x=model.predict(encoded)
        yhat=np.argmax(predict_x,axis=1)
        out_word=''

        for word,index in tokenizer.word_index.items():
            if index == yhat:
                out_word=word
                break
        in_text+=' '+out_word
    return in_text

tokenizer=Tokenizer()
tokenizer.fit_on_texts([data])
max_length=2

st.title('Bridgeton Text Generator SMS Web App')

image=Image.open('./1.jpg')

st.image(image)

st.write("This is a Bridgeton Quotes Text Generator Web App")

s_text = st.text_input("Type a word you want to generate after")

n = st.number_input("Type the number of words you want to generate", min_value=1, step=1)

generate_word = st.button("Generate Text Words")

send_sms = st.button("Send Text Messages")



def send_sms_via_email(number,message,provider,sender_credentials,subject,smpt_server='smpt.gmai.com',smpt_port=465):
    sender_email,email_password=sender+sender_credentials
    receiver_email=f'{number}@{provider}'

    email_message=f"Subject:{subject}\nTo:{receiver_email}\n{message}"

if s_text and n  and generate_word:
    st.header(generate_seq(loaded_model,tokenizer,max_length-1,s_text,n)).

elif s_text and generate_word and not n:
    st.write('Please input number of words')

elif generate_word and not s_text and not n:
    st.write('Please input all information')

    with smpt.SMPT_SSL(smpt_server,smpt_port,context=ssl.create_default_context()) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_message)
elif s_text and n and send_sms:
    message=generate_seq(loaded_model,tokenizer,max_length-1,s_text,n)
    
    try:
        number=''
        message=message
        provider=''
        sender_credentials("","")
        send_sms_via_email(number,message,provider,sender_credentials)

    except:
        st.write("Exception Thrown")






