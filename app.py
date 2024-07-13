import streamlit as st
import pickle
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://aagyashrestha12:pass@cluster0.jnp1qjg.mongodb.net/")
db = client["authentication"]
jobs_collection = db["jobs"]
profiles_collection = db["profiles"]

# Load models
clf = pickle.load(open('clf.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))

tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Function to clean resume text
def clean_resume(resume_text):
    clean_text = re.sub('http\S+\s*', ' ', resume_text)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+', '', clean_text)
    clean_text = re.sub('@\S+', '  ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)
    return clean_text.strip()

# Mapping of category IDs to job titles
category_mapping = {
    15: "Java Developer",
    23: "Testing",
    8: "DevOps Engineer",
    20: "Python Developer",
    24: "Web Designing",
    12: "HR",
    13: "Hadoop",
    3: "Blockchain",
    10: "ETL Developer",
    18: "Operations Manager",
    6: "Data Science",
    22: "Sales",
    16: "Mechanical Engineer",
    1: "Arts",
    7: "Database",
    11: "Electrical Engineering",
    14: "Health and fitness",
    19: "PMO",
    4: "Business Analyst",
    9: "DotNet Developer",
    2: "Automation Testing",
    17: "Network Security Engineer",
    21: "SAP Developer",
    5: "Civil Engineer",
    0: "Advocate",
}

# Function to add a job posting to the database
def add_job_posting(job_title, job_description, category_id, company_name):
    job_data = {
        "job_title": job_title,
        "job_description": job_description,
        "category_id": int(category_id),
        "company_name": company_name
    }
    jobs_collection.insert_one(job_data)
    st.success("Job posting added successfully!")

# Function to display job postings based on category
def display_job_postings(category_id):
    st.subheader("Job Openings Matching Your Category:")
    job_cursor = jobs_collection.find({"category_id": int(category_id)})
    for job in job_cursor:
        st.markdown(
            f'<div class="job-item">'
            f'<h3>{job.get("job_title", "No Title")}</h3>'
            f'<p><strong>Company Name:</strong> {job.get("company_name", "No Company Name")}</p>'
            f'<p><strong>Job Description:</strong> {job.get("job_description", "No Description")}</p>'
            f'</div>',
            unsafe_allow_html=True
        )

# Function to display all job postings
def display_all_job_postings():
    st.subheader("All Job Openings:")
    job_cursor = jobs_collection.find()
    for job in job_cursor:
        st.markdown(
            f'<div class="job-item">'
            f'<h3>{job.get("job_title", "No Title")}</h3>'
            f'<p><strong>Company Name:</strong> {job.get("company_name", "No Company Name")}</p>'
            f'<p><strong>Job Description:</strong> {job.get("job_description", "No Description")}</p>'
            f'</div>',
            unsafe_allow_html=True
        )

# Function to display job analytics dashboard
def display_analytics_dashboard():
    total_jobs = jobs_collection.count_documents({})
    st.metric("**Total Job Postings**", total_jobs)
    category_stats = jobs_collection.aggregate([
        {"$group": {"_id": "$category_id", "count": {"$sum": 1}}}
    ])
    st.write("---")
    st.write("**Job Postings by Category:**")
    for stat in category_stats:
        category_name = category_mapping.get(stat["_id"], "Unknown")
        st.write(f"{category_name}: {stat['count']}")

# Function to display job seeker analytics
def display_job_seeker_analytics():
    total_job_seekers = profiles_collection.count_documents({})
    st.metric("**Total Job Seekers**", total_job_seekers)

    job_titles_stats = profiles_collection.aggregate([
        {"$group": {"_id": "$desired_job_title", "count": {"$sum": 1}}}
    ])
    st.write("---")
    st.write("**Desired Job Titles Distribution:**")
    for stat in job_titles_stats:
        st.write(f"{stat['_id']}: {stat['count']}")

# Function to display job seeker profiles
def display_job_seeker_profiles():
    st.subheader("Job Seeker Profiles")
    job_seekers_cursor = profiles_collection.find()
    for job_seeker in job_seekers_cursor:
        st.markdown(
            f'<div class="job-item">'
            f'<p><strong>Name:</strong> {job_seeker.get("name", "Unknown")}</p>'
            f'<p><strong>Email:</strong> {job_seeker.get("email", "Unknown")}</p>'
            f'<p><strong>Desired Job Title:</strong> {job_seeker.get("desired_job_title", "Not specified")}</p>'
            f'</div>',
            unsafe_allow_html=True
        )

# Function to add a job seeker profile to the database
def add_job_seeker_profile(name, email, desired_job_title):
    job_seeker_data = {
        "name": name,
        "email": email,
        "desired_job_title": desired_job_title
    }
    profiles_collection.insert_one(job_seeker_data)
    st.success("Job seeker profile added successfully!")

# Function to display user profile input form
def display_user_profile():
    st.subheader("Job Seeker Profile")
    st.write("Please add your profile below:")
    name = st.text_input("Name")
    email = st.text_input("Email")
    desired_job_title = st.text_input("Desired Job Title")

    if st.button("Add Profile"):
        add_job_seeker_profile(name, email, desired_job_title)

# Main function to handle the application navigation and functionality
def main():
    st.set_page_config(page_title="Job Journey", layout="wide")

    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.markdown('<div class="title-section"><h1>JOB JOURNEY</h1></div>', unsafe_allow_html=True)
    st.subheader("   ")

    nav_selection = st.sidebar.radio(
        "**Resume Screening Application**",
        ("Home", "Market Analysis", "All Job Openings","Job Seekers","Add Job", "Add Profile"),

    )
    for _ in range(30):
        st.sidebar.write("")

    st.sidebar.write("-Aagya Shrestha")
    if nav_selection == "Home":

        st.subheader("Find job that meets your resume!")
        uploaded_file = st.file_uploader('Upload Resume', type=['txt', 'pdf'])

        if uploaded_file is not None:
            try:
                resume_bytes = uploaded_file.read()
                resume_text = resume_bytes.decode('utf-8')
            except UnicodeDecodeError:
                resume_text = resume_bytes.decode('latin-1')

            cleaned_resume = clean_resume(resume_text)
            input_features = tfidf.transform([cleaned_resume])
            prediction_id = clf.predict(input_features)[0]

            category_name = category_mapping.get(prediction_id, "Unknown")

            st.markdown(
                f'<div class="prediction-result">Predicted Category: {category_name}</div>',
                unsafe_allow_html=True
            )

            display_job_postings(prediction_id)

        st.image("images/logo.jpg", use_column_width=True)

    elif nav_selection == "Market Analysis":
        col1, col2 ,col3= st.columns(3)

        with col1:
            display_analytics_dashboard()

        with col3:
            display_job_seeker_analytics()

    elif nav_selection == "Add Job":
        st.subheader("Add Job Posting")
        job_title = st.text_input("Job Title")
        job_description = st.text_area("Job Description")
        company_name = st.text_input("Company Name")
        category_id = st.selectbox("Category", list(category_mapping.keys()),
                                   format_func=lambda x: category_mapping[x])
        if st.button("Add Job Posting"):
            add_job_posting(job_title, job_description, category_id, company_name)


    elif nav_selection == "Job Seekers":
        display_job_seeker_profiles()

    elif nav_selection == "Add Profile":
        display_user_profile()

    elif nav_selection == "All Job Openings":
        display_all_job_postings()

if __name__ == "__main__":
    main()
