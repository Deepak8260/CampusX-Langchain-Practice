from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

st.header('Research Paper Summarizer')

paper_input = st.selectbox( "Select Research Paper Name", ["ImageNet Classification with Deep Convolutional Neural Networks", "Deep Residual Learning for Image Recognition", "Attention Is All You Need", "ADAM: A Method for Stochastic Optimization", "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", "Language Models are Few-Shot Learners", "Deep Contextualized Word Representations", "Generating Sequences With Recurrent Neural Networks", "Diffusion Models Beat GANs on Image Synthesis", "Generative Adversarial Networks", "Mastering the Game of Go with Deep Neural Networks and Tree Search", "Classification and Regression Trees", "Random Forests", "XGBoost: A Scalable Tree Boosting System", "The Two Cultures: Statistical Modeling vs. Algorithmic Modeling"]
 )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short paragraphs", "Medium paragraphs", "Long (detailed explanation)"] )


template = load_prompt("prompt_template.json")



if st.button("summarize"):
    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input, 
        "style_input": style_input, 
        "length_input": length_input
        })
    st.write(result.content)




# Below part of the code is same as above code
# prompt = template.invoke({
#     "paper_input": paper_input, 
#     "style_input": style_input, 
#     "length_input": length_input
#     })

# if st.button("summarize"):
#     result = model.invoke(prompt)
#     st.write(result.content)