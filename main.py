import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

template = """
    Below is an email that may be poorly worded.
    Your goal is to:
    - Properly format the email
    - Convert the input text to a secified tone
    - Convert the input text to a secified dialect
    
    Here are some examples different Tones:
    - Formal: We went to Barcelona for the weekend. we have a lot of things to tell you.
    - Informal: Went to Barcelona for the weekend. Lots to tell you 
    
    Here are some examples of words in different dialects:.
    - American English: French Fries, cotton candy, apartment, garbage, cookie
    - British English: Chips, candyfloss, flag, rubbish, biscuit
    
    Below is the email, tone, and dialect:
    TONE: {tone}
    DIALECT: {dialect}
    EMAIL: {email}
    
    YOUR RESPONSE:
"""

prompt = PromptTemplate(
    input_variables=["tone", "dialect", "email"],
    template=template,
)

def load_llm():
    llm = OpenAI(temperature=0.5, openai_api_key="sk-N5vd1ARx7Kog1lwYE8B6719b063a4b60903643F29f1375Fb",
                 openai_api_base="https://d2.xiamoai.top/v1")
    return llm

llm = load_llm()

st.set_page_config(page_title="Global Email", page_icon=":robot:")
st.header("Globalize Text")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Often professionals would like to improve their emails, but don't have the skills to do so.\n\n "
                "This tools will help you improve your emails skills by converting your email into a more professional format."
                "This tool is powered by [LangChain](www.langchain.com) and [OpenAI](www.openai.com) and made by 51265901045@stu.ecnu.edu.cn.")

with col2:
    st.image(image='img.png', width=500, caption='An image example')

st.markdown("## Enter your email To Convert")

col1, col2 = st.columns(2)

with col1:
    option_tone = st.selectbox(
        'Which tone would you like your email to have?',
        ('Formal', 'Informal', 'Neutral'))

with col2:
    option_dialect= st.selectbox(
        'Which English dialect would you like?',
        ('American', 'British', 'Australian')
    )

def get_text():
    input_text = st.text_area(label="", placeholder="Your Email...", key="email_inut")
    return input_text

email_input = get_text()
st.markdown('### Your Converted Email:')

if email_input:
    prompt_with_email = prompt.format(tone=option_tone, dialect=option_dialect, email=email_input)
    format_mail = llm(prompt_with_email)
    st.write(format_mail)