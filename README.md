# titanic-disaster

This project builds logistic regression models (in both Python and R) to predict passenger survival on the Titanic dataset.

## Repository Structure
```plaintext
titanic-disaster/
├── src/
│   ├── app/
│   │   ├── main.py                  # Python logistic regression
│   │   └── Dockerfile               # Python Dockerfile
│   └── r_app/
│       ├── main.R                   # R logistic regression
│       └── Dockerfile               # R Dockerfile
├── requirements.txt                 # Python dependencies
├── .gitignore
└── README.md                        # this file
```

## Objective
Build and evaluate simple logistic regression models predicting `Survived` using selected passenger features from the Titanic dataset.

## Prerequisites
You only need:
1. Docker Desktop
2. Git installed (optional, for cloning)
> **You do NOT need to install Python or R locally** — both environments are fully containerized.

## Step 1 — Clone this Repository

```bash
git clone https://github.com/<your-username>/titanic-disaster.git
cd titanic-disaster
```

## Step 2 - Download the Data

Download the Titanic dataset from [Kaggle – Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data).

Create a folder called `data` inside `src` folder and place the two CSV files into the `src/data/` folder:

```plaintext
src/data/train.csv
src/data/test.csv
```

## Step 3 — Run the Python Container

### Build the Docker image

From your project root, run:

```bash
docker build -t titanic-app .
```

### Run the container
```bash
docker run --rm -v $(pwd)/src/data:/app/src/data titanic-app
```

This will:

1. Load and clean the data
2. Train a logistic regression model on `train.csv`
3. Output training accuracy
4. Generate predictions on `test.csv`
5. Save predictions to `src/data/predictions.csv`


## Step 4 — Run the R Container
### Build the Docker image

From your project root, run:

```bash
cd src/r_app
docker build -t titanic-r-app .
```

### Run the container
```bash
cd ../..
docker run --rm -v $(pwd)/src/data:/app/src/data titanic-r-app
```

This will:
1. Load and clean the data
2. Train a logistic regression model on `train.csv`
3. Output training accuracy
4. Predict on `test.csv`
5. Save predictions to `src/data/predictions_r.csv`


## Step 5 — Inspect the Outputs
After running both containers, your folder `src/data/` will contain:

```plaintext
train.csv
test.csv
predictions.csv         ← from Python model
predictions_r.csv       ← from R model
```

## Notes on Design
1. Both models use **logistic regression** trained on:
```plaintext
Pclass, Sex, Age, SibSp, Parch, Fare
```
2. Missing values are filled with median or mode.
3. All preprocessing and modeling steps are fully contained within each Docker image.
4. No external Python or R installation is needed.

