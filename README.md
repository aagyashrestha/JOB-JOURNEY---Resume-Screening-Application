# Resume-Screening-App
Resume Screening App With Python and Machine Learning 


link- [https://job--journey.streamlit.app/](https://job-journey.streamlit.app/)


Overview:

Job Journey is an automated resume screening application designed to categorize resumes into predefined job categories using machine learning techniques. This project utilizes natural language processing (NLP) and classification algorithms to streamline the initial phase of the recruitment process.

#Features

1)Automatic Resume Categorization The application employs a text classification approach, using Term Frequency-Inverse Document Frequency (TF-IDF) vectorization combined with a Multinomial Naive Bayes classifier. Integration: The tfidf.pkl preprocessed TF-IDF model and clf.pkl trained classifier are loaded and utilized in real-time within the Streamlit application (app.py).

2)Streamlit Interface The frontend is built using Streamlit, a Python framework for creating web applications. It provides an interactive environment where users can upload resumes and receive instant categorization results. Integration: The app.py script integrates backend Python functionalities with a user-friendly interface, facilitating seamless user interaction and feedback.

3)Python Backend Backend operations include data preprocessing, model training, and prediction. Python libraries such as pandas, scikit-learn, and joblib are used for data manipulation, machine learning model implementation, and serialization. Integration: Data preprocessing (data_cleaning.py), model training (model_training.py), and prediction (app.py) are integrated to handle resume uploads, process text data, and deliver categorized results.
<img width="1470" alt="Screenshot 2024-07-22 at 1 06 22 PM" src="https://github.com/user-attachments/assets/cc21fc25-c03c-4b13-a815-7bf92475f0d2">
<img width="1467" alt="Screenshot 2024-07-22 at 1 06 39 PM" src="https://github.com/user-attachments/assets/0b398c83-5064-4479-92ae-611ebe7a6488">
<img width="1470" alt="Screenshot 2024-07-22 at 1 06 50 PM" src="https://github.com/user-attachments/assets/b7f33090-d024-4401-a846-d8831bf7e621">
<img width="1470" alt="Screenshot 2024-07-22 at 1 06 58 PM" src="https://github.com/user-attachments/assets/df2a5242-092d-4f20-8110-beae2db44afc">
<img width="1469" alt="Screenshot 2024-07-22 at 1 07 04 PM" src="https://github.com/user-attachments/assets/4c26d7dc-5feb-4b1b-8170-230b968b106b">
<img width="1470" alt="Screenshot 2024-07-22 at 1 07 11 PM" src="https://github.com/user-attachments/assets/4a7fb1c0-aeda-4a7c-bbc1-422a3707b5fe">
<img width="1470" alt="Screenshot 2024-07-22 at 1 07 17 PM" src="https://github.com/user-attachments/assets/5fe5e132-14c0-484a-a239-43baf9156553">
