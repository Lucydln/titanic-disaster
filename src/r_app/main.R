cat("Starting Titanic R model...\n")

# --- Load training data ---
df <- read.csv("src/data/train.csv")
cat("Training data loaded successfully.\n")
print(head(df))

# --- Check missing values ---
cat("\nChecking missing values:\n")
print(colSums(is.na(df)))

# --- Fill missing values ---
df$Age[is.na(df$Age)] <- median(df$Age, na.rm = TRUE)
df$Embarked[is.na(df$Embarked)] <- names(sort(table(df$Embarked), decreasing = TRUE))[1]
cat("Missing values filled.\n")

# --- Encode categorical variables ---
df$Sex <- ifelse(df$Sex == "male", 1, 0)

# --- Define features ---
features <- c("Pclass", "Sex", "Age", "SibSp", "Parch", "Fare")
X <- df[, features]
y <- df$Survived

# --- Train logistic regression model ---
cat("\nTraining logistic regression model...\n")
model <- glm(y ~ ., data = X, family = binomial)
cat("Model training complete.\n")

# --- Predict on training data ---
pred_probs <- predict(model, X, type = "response")
pred <- ifelse(pred_probs > 0.5, 1, 0)

# --- Measure training accuracy ---
train_acc <- mean(pred == y)
cat(sprintf("Training accuracy: %.3f\n", train_acc))

# --- Load test data ---
test <- read.csv("src/data/test.csv")
cat("\nTest data loaded successfully.\n")

# --- Fill missing values in test data ---
test$Age[is.na(test$Age)] <- median(df$Age, na.rm = TRUE)
test$Embarked[is.na(test$Embarked)] <- names(sort(table(df$Embarked), decreasing = TRUE))[1]
test$Sex <- ifelse(test$Sex == "male", 1, 0)

# --- Predict on test data ---
X_test <- test[, features]
test_pred_probs <- predict(model, X_test, type = "response")
test$Predicted_Survived <- ifelse(test_pred_probs > 0.5, 1, 0)

# --- Save predictions ---
write.csv(test[, c("PassengerId", "Predicted_Survived")],
          "src/data/predictions_r.csv", row.names = FALSE)
cat("\nPredictions saved to src/data/predictions_r.csv\n")
cat("R Titanic model complete.\n")
