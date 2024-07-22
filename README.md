# Resume-Screening-App
Resume Screening App With Python and Machine Learning 


link- [https://job--journey.streamlit.app/](https://job-journey.streamlit.app/)


Overview:

Job Journey is an automated resume screening application designed to categorize resumes into predefined job categories using machine learning techniques. This project utilizes natural language processing (NLP) and classification algorithms to streamline the initial phase of the recruitment process.

#Features

1)Automatic Resume Categorization The application employs a text classification approach, using Term Frequency-Inverse Document Frequency (TF-IDF) vectorization combined with a Multinomial Naive Bayes classifier. Integration: The tfidf.pkl preprocessed TF-IDF model and clf.pkl trained classifier are loaded and utilized in real-time within the Streamlit application (app.py).

2)Streamlit Interface The frontend is built using Streamlit, a Python framework for creating web applications. It provides an interactive environment where users can upload resumes and receive instant categorization results. Integration: The app.py script integrates backend Python functionalities with a user-friendly interface, facilitating seamless user interaction and feedback.

3)Python Backend Backend operations include data preprocessing, model training, and prediction. Python libraries such as pandas, scikit-learn, and joblib are used for data manipulation, machine learning model implementation, and serialization. Integration: Data preprocessing (data_cleaning.py), model training (model_training.py), and prediction (app.py) are integrated to handle resume uploads, process text data, and deliver categorized results.
