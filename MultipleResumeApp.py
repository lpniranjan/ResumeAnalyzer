import streamlit as st
from dotenv import load_dotenv
import DocumentHandler as PDFCharacterTextSplitter
import EmbeddingHandler as PDFTextEmbedding
import ConversationHandler as CurrentConversation
import ResumeHandler as ResumeAnalasis
from HTMLTemplate import css, CV_template, ANA_template

def HandleUserQuestion(userQuestion):
     questionResponse = st.session_state.conversation({'question':userQuestion})
     st.write(questionResponse)

load_dotenv()
st.set_page_config(page_title="CV Screening", page_icon=":document:")
st.write(css, unsafe_allow_html=True)

if "conversation" not in st.session_state:
     st.session_state.conversation = None

with st.sidebar:
     st.subheader("Available CV's")
     pdf_docs = st.file_uploader("Upload your CVs here",accept_multiple_files=True)
     
     #if st.button("Process"):
     #     with st.spinner("Processing"):
               
               # Get CV text
     #          rawPDFText = PDFCharacterTextSplitter.GetPDFText(pdf_docs)
               #st.write(rawPDFText)
               
               # Get text chunks becasue we can't process tokensize exceed the limit (2048)
     #          textChunks = PDFCharacterTextSplitter.GetTextChunks(rawPDFText)
               #st.write(textChunks)

               #Get text embedings
     #          textEmbeddings = PDFTextEmbedding.GetVectoreStore(textChunks)
               #st.write(textEmbeddings)

               #Get conversation chain
     #          st.session_state.conversation = CurrentConversation.GetConversationChain(textEmbeddings)

st.header("Analyze the CV bank")
userQuestion = st.text_input("Please enter your job title:")


if st.button("Find") and userQuestion:
      with st.spinner("Searching"):
          resumeAnalysisData = ResumeAnalasis.GetResumeResult(pdf_docs,userQuestion)
          #st.write(resumeAnalysisData)
          for x,y in resumeAnalysisData.items():
               st.write(CV_template.replace("{{MSG}}", x),unsafe_allow_html=True)
               st.write(ANA_template.replace("{{MSG}}", y[0]["analysis"]),unsafe_allow_html=True)


