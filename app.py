import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getLLamaresponse(input_text, no_words, blog_style):
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                            model_type='llama',
                            config={'max_new_tokens': 256, 'temperature': 0.01})
    # Prompt Template
    template = """
            Write a blog for {blog_style} job profile for a topic {input_text}
            within {no_words} words.
        """

    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],
                                template=template)

        # Generate the response from the LLama 2 model
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return(response)

st.set_page_config(page_title="Generate content using Llama 2",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Content: Using Llama 2")

input_text = st.text_input("Input")

# Creating two more columns for additional 2 fields
col1, col2 = st.columns([7, 3])

with col1:
    no_words = st.selectbox('Word Limit',
                              ('50','100', '150', '200'), index=0)

    # no_words = st.text_input('Word Limit')

with col2:
    blog_style = st.radio('Select Domain',
                              ["Student", "Professional", "Common people", "Researchers", "Data Scientist"], index=0)
    # blog_style = st.selectbox('Select Domain',
    #                           ('Students','Researchers', 'Data Scientist', 'Common People'), index=0)

submit = st.button("Generate")

# Final response
if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))
