import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("Starting Titanic survivability model...")

# --- Load training data ---
print("\nLoading training data...")
df = pd.read_csv("src/data/train.csv")
print("Training data loaded successfully!")
print("First 5 rows:")
print(df.head())

# --- Check missing values ---
print("\nChecking missing values in training data:")
print(df.isnull().sum())

# --- Handle missing values ---
print("\nFilling missing values...")
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
print("Missing values filled.")

# --- Encode categorical variables ---
print("\nEncoding 'Sex' column...")
df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})
print("Encoding complete. Unique values in 'Sex':", df['Sex'].unique())

# --- Define features and target ---
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
X = df[features]
y = df['Survived']
print("\nSelected features:", features)
print("Feature matrix shape:", X.shape)
print("Target variable shape:", y.shape)

# --- Train logistic regression model ---
print("\nTraining Logistic Regression model...")
model = LogisticRegression(max_iter=1000)
model.fit(X, y)
print("Model training complete.")

# --- Evaluate model on training data ---
print("\nEvaluating training performance...")
y_pred = model.predict(X)
train_acc = accuracy_score(y, y_pred)
print(f"Training accuracy: {train_acc:.3f}")

# --- Load test data ---
print("\nLoading test data...")
test = pd.read_csv("src/data/test.csv")
print("Test data loaded successfully!")
print("First 5 rows of test data:")
print(test.head())

# --- Handle missing values in test data ---
print("\nFilling missing values in test data...")
test['Age'] = test['Age'].fillna(df['Age'].median())
test['Fare'] = test['Fare'].fillna(df['Fare'].median())
test['Embarked'] = test['Embarked'].fillna(test['Embarked'].mode()[0])
print("Missing values filled in test data.")

# --- Encode categorical variables in test data ---
print("\nEncoding 'Sex' column in test data...")
test['Sex'] = test['Sex'].map({'male': 1, 'female': 0})
print("Encoding complete. Unique values in 'Sex':", test['Sex'].unique())

# --- Predict on test data ---
print("\nGenerating predictions on test data...")
X_test = test[features]
test['Predicted_Survived'] = model.predict(X_test)
print("Predictions complete.")
print("Preview of predictions:")
print(test[['PassengerId', 'Predicted_Survived']].head())

# --- Save predictions ---
output_path = "src/data/predictions.csv"
test[['PassengerId', 'Predicted_Survived']].to_csv(output_path, index=False)
print(f"\nPredictions saved to {output_path}")

print("\nTitanic model run complete.")
