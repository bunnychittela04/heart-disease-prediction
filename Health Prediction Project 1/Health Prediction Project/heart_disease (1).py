import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pickle

# Load the dataset
data = pd.read_csv('heart.csv')

# Define categorical and numerical columns
categorical_cols = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
numerical_cols = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

# Apply preprocessing
scaler = StandardScaler()
data[numerical_cols] = scaler.fit_transform(data[numerical_cols])

# Split features and target
X = data.drop('target', axis=1)
y = data['target']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Evaluate the model
accuracy = knn.score(X_test, y_test)
print("Accuracy: {:.2f}%".format(accuracy * 100))

# Pickle the trained KNN model
with open("model.pkl", "wb") as file:
    pickle.dump(knn, file)
print("KNN model pickled successfully!")

# Load the trained KNN model
with open("model.pkl", "rb") as file:
    knn_model = pickle.load(file)

# Create a new data point (replace values with actual data)
new_data = pd.DataFrame({
    'age': [65],
    'sex': [1],
    'cp': [0],
    'trestbps': [145],
    'chol': [233],
    'fbs': [1],
    'restecg': [2],
    'thalach': [150],
    'exang': [0],
    'oldpeak': [2.3],
    'slope': [3],
    'ca': [0],
    'thal': [1]
})

# Preprocess the new data point
new_data[numerical_cols] = scaler.transform(new_data[numerical_cols])

# Predict whether the person has heart disease or not
prediction = knn_model.predict(new_data)
if prediction[0] == 0:
    print("The person does not have heart disease.")
else:
    print("The person has heart disease.")
