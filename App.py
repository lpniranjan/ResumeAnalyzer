import streamlit as st
from dotenv import load_dotenv
import ResumeHandler as ResumeAnalasis
from HTMLTemplate import css, CV_template, ANA_template, SC_template_ng, SC_template_ps
import LinkedinApiHandler as LinkedInData
import GithubApiHandler as GitHubData
import JsonContentHandler as JsonAnalysis
import KeywordHandler as keywordAnalysis

load_dotenv()
st.set_page_config(page_title="Resume Screening", page_icon=":document:")
st.write(css, unsafe_allow_html=True)

if "userQuestion" not in st.session_state:
     st.session_state['userQuestion'] = ''

with st.sidebar:
     st.subheader("Job Profile")
     jobTitle = st.text_input('Job title(ex:"Python developer"):')
     exLevel = st.text_input('Experience level(ex:"5"):')
     comLevel = st.text_input('Communication level(ex:"high level of proficiency in English"):')
     comCultre  = st.text_input('Company culture(ex:"Results-Driven"):')
     st.subheader("Candidate Profile")
     pdf_doc = st.file_uploader("Upload your candidate resume here and click 'Forecast'",accept_multiple_files=False)
    
st.header("Analysis of candidate resume")
if st.sidebar.button("Forecast"):
     if jobTitle and pdf_doc:
          st.session_state['userQuestion'] = "Please analyze this resume for "+jobTitle+" post";
          
          if exLevel:
               exLevelnum = GitHubData.NumberToWords(exLevel)
               st.session_state['userQuestion'] = "Please analyze this resume for "+exLevelnum+" years experience "+jobTitle+" post.";
          
          if comLevel:
               st.session_state['userQuestion'] = "Please analyze this resume for "+jobTitle+" post with "+comLevel+", both written and verbal.";

          if comCultre:
               st.session_state['userQuestion'] = "Please analyze this resume for "+jobTitle+" post and compatibility with our company culture of "+comCultre+".";
          
          if comLevel and comCultre:
               st.session_state['userQuestion'] = "Please analyze this resume for "+jobTitle+" post with "+comLevel+", both written and verbal and compatibility with our company culture of "+comCultre+".";

          if exLevel and comCultre:
               exLevelnum = GitHubData.NumberToWords(exLevel)
               st.session_state['userQuestion'] = "Please analyze this resume for "+exLevelnum+" years experience "+jobTitle+" post and compatibility with our company culture of "+comCultre+".";

          if comLevel and exLevel:
               exLevelnum = GitHubData.NumberToWords(exLevel)
               st.session_state['userQuestion'] = "Please analyze this resume for "+exLevelnum+" years experience "+jobTitle+" post with "+comLevel+", both written and verbal.";

          if exLevel and comLevel and comCultre:
               exLevelnum = GitHubData.NumberToWords(exLevel)
               st.session_state['userQuestion'] = "Please analyze this resume for "+exLevelnum+" years experience "+jobTitle+" post with "+comLevel+", both written and verbal and compatibility with our company culture of "+comCultre+".";     
          
          st.text_area("Forecast this candidate based on:",st.session_state['userQuestion'])   
          with st.spinner("Analyzing"):
               resumeAnalysisData = ResumeAnalasis.GetSingleResumeResult(pdf_doc,st.session_state['userQuestion'],jobTitle)
               for x,y in resumeAnalysisData.items():
                    jobDescription = st.text_area("Job description:",(y[0]["jobDescription"]).strip(),height=100)                    
                    st.text_area("Technical skills:",(y[0]["jobSkills"]).strip(),height=100) 
                    st.write(CV_template.replace("{{MSG}}", "Resume forecast:"),unsafe_allow_html=True)
                    st.write(ANA_template.replace("{{MSG}}", (y[0]["analysis"]).strip()),unsafe_allow_html=True)
                    
                    linkedInURL = st.sidebar.text_input("LinkedIn profile:",(y[0]["linkedinURL"]).strip())
                    st.sidebar.text_input("FaceBook profile:",(y[0]["facebookURL"]).strip())
                    gitURL = st.sidebar.text_input("Github account:",(y[0]["githubURL"]).strip())
                    st.sidebar.text_input("Hackerank:")
                    st.sidebar.text_input("SO:")
                    
                    if linkedInURL and linkedInURL != '':
                         linkdata = LinkedInData.GetLinkedInProfileData(linkedInURL)
                         st.write(CV_template.replace("{{MSG}}", "LinkedIn forecast:"),unsafe_allow_html=True)
                         st.write(ANA_template.replace("{{MSG}}", (JsonAnalysis.ProcessJsonData(linkdata)).strip()),unsafe_allow_html=True)
                    
                    if gitURL and gitURL != '':
                         st.write(CV_template.replace("{{MSG}}", "GitHub forecast:"),unsafe_allow_html=True)
                         st.write(ANA_template.replace("{{MSG}}", (GitHubData.GetGithubRepoDetails(gitURL)).strip()),unsafe_allow_html=True)
                    
                  
                    #kew2 = keywordAnalysis.GetKeywords((y[0]["analysis"]).strip())
                    #st.write(kew2)

                    #similarity_score = round(((kew1.similarity(kew2)) * 100),2)
                    #st.write(similarity_score)

                    summaryScre = 'Forecast score: '+str(y[0]["matchingPercentage"])+' %'
                    if y[0]["matchingPercentage"]>50:
                     st.write(SC_template_ps.replace("{{MSG}}", summaryScre),unsafe_allow_html=True)  
                    else:
                      st.write(SC_template_ng.replace("{{MSG}}", summaryScre),unsafe_allow_html=True)        
     else:
          st.error('Please check whether "job title" inserted and "Resume" uploaded', icon="⚠️")                   
              
 

