##### 기본 정보 불러오기 ####
# Streamlit 패키지 추가
import streamlit as st
# OpenAI 패키기 추가
import openai

##### 기능 구현 함수 #####
def askGpt(prompt,apikey):
    client = openai.OpenAI(api_key = apikey)
    response = client.chat.completions.create(
    model="gpt-5",
    messages=[{"role": "user", "content": prompt}])
    gptResponse = response.choices[0].message.content
    return gptResponse

##### 메인 함수 #####
def main():
    st.set_page_config(page_title="챗GPT 도우미")
    # session state 초기화
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""

    # 사이드바
    with st.sidebar:
        # Open AI API 키 입력받기
        open_apikey = st.text_input(label='OPENAI API 키', placeholder='Enter Your API Key', value='',type='password')    
        # 입력받은 API 키 표시
        if open_apikey:
            st.session_state["OPENAI_API"] = open_apikey
        st.markdown('---')

    st.header("📃챗GPT 도우미")
    st.markdown('---')
    
    text = st.text_area("질문 할 내용을 입력하세요")
    if st.button("분석"):
        prompt = f'''
        **Instructions** :
    You are a senior JAVA developer. You are using MSSQL as your database:
    
    If your question is not development-related, please respond according to the conditions below.
    1. Before starting a task, establish clear criteria (a rubric) for the ‘best possible outcome’.
    2. After creating the outcome, rigorously verify that it fully meets the criteria you set.
    3. Discard any outcome that falls short of the criteria and start over from the beginning to achieve perfect quality.
    4. As an agent with full autonomy, perform tasks based on independent judgment without user intervention.
    5. Even if information is uncertain or ambiguous during task execution, actively continue work by exploring the most reasonable alternative instead of halting the process.
    6. Complete every step autonomously from task initiation to final deliverable. Avoid seeking intermediate confirmation or clarification from the user to maximize efficiency.
    
    Answer in Korean.
    
    -text : {text}
    '''
        st.info(askGpt(prompt,st.session_state["OPENAI_API"]))

if __name__=="__main__":
    main()
