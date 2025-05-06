import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

emails = [
    ("Free lottery winner! Claim now!", 1),
    ("Meeting at 3pm tomorrow", 0),
    ("Get rich quick! Investment opportunity", 1),
    ("Project deadline reminder", 0),
    ("URGENT: Your account needs verification", 1),
    ("Lunch meeting with team", 0),
    ("100% Free iPhone! Click here", 1),
    ("Weekly report attached", 0),
    ("Nigerian prince needs your help", 1),
    ("Schedule for next week", 0),
]

X = [email[0] for email in emails]
y = [email[1] for email in emails]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

classifier = MultinomialNB()
classifier.fit(X_train_vectors, y_train)

def detect_spam(text):
    text_vector = vectorizer.transform([text])
    prediction = classifier.predict(text_vector)[0]
    probability = classifier.predict_proba(text_vector)[0]
    
    return {
        'is_spam': bool(prediction),
        'confidence': float(max(probability)),
        'prediction': 'SPAM' if prediction == 1 else 'HAM'
    }

test_emails = [
    "Congratulations! You've won $1,000,000!",
    "Hi, can we reschedule our meeting to 2pm?",
    "URGENT: Your payment is pending!",
    "Monthly team sync tomorrow at 10am"
]

print("Spam Detection Results:")
print("-" * 50)
for email in test_emails:
    result = detect_spam(email)
    print(f"\nEmail: {email}")
    print(f"Prediction: {result['prediction']}")
    print(f"Confidence: {result['confidence']:.2f}")

if __name__ == "__main__":
    y_pred = classifier.predict(X_test_vectors)
    print("\nModel Performance:")
    print("-" * 50)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
