import spacy
from collections import Counter

def analyze_cv_for_post(cv_text, job_post_requirements):
    nlp = spacy.load("en_core_web_sm")
    
    # Process CV text
    cv_doc = nlp(cv_text)

    # Tokenize and count words in CV
    cv_word_counts = Counter(token.text.lower() for token in cv_doc if token.is_alpha)

    # Tokenize and count words in job post requirements
    job_post_word_counts = Counter(job_post_requirements.lower().split())

    # Calculate the percentage match
    total_words_in_cv = sum(cv_word_counts.values())
    matched_words = sum((cv_word_counts & job_post_word_counts).values())
    percentage_match = (matched_words / total_words_in_cv) * 100

    return percentage_match

# Example usage
cv_text = "John Doe is a software engineer with 5 years of experience in Python development."
job_post_requirements = "We are looking for a software engineer with experience in Java development."

result = analyze_cv_for_post(cv_text, job_post_requirements)
print(f"Percentage match: {result:.2f}%")
