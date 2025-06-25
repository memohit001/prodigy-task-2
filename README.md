# 🚢 Titanic Dataset - Exploratory Data Analysis (EDA)

This project explores the famous [Titanic dataset](https://www.kaggle.com/c/titanic) using **Python**, focusing on **data cleaning**, **feature engineering**, and **exploratory data analysis (EDA)** to uncover meaningful patterns related to passenger survival.

---

## 📂 Dataset Information

The dataset provides information on passengers aboard the Titanic, including features like:

- **Survived** (0 = No, 1 = Yes)
- **Pclass** (Ticket class)
- **Sex**
- **Age**
- **SibSp** (Siblings/Spouses aboard)
- **Parch** (Parents/Children aboard)
- **Fare**
- **Embarked** (Port of Embarkation)

---

## ✅ Objectives

- Clean and preprocess the dataset
- Handle missing data
- Encode categorical variables
- Create new meaningful features (e.g., FamilySize)
- Visualize survival trends using graphs and plots
- Analyze correlations between features and survival

---

## 🛠️ Technologies Used

- Python 3.x
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)

---

## 📊 Key Insights

- **Women** had a much higher survival rate than men.
- **1st class passengers** were more likely to survive than 2nd and 3rd class.
- **Children** had a higher survival probability.
- **Family size** had a non-linear effect — small families fared better.
- Passengers who **embarked from Cherbourg** had a higher chance of survival.

---

## 📈 Sample Visualizations

- Count plot of survivors vs non-survivors
- Bar plots comparing survival by gender, class, and port
- Age distribution histograms and violin plots
- Heatmap showing feature correlations

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/titanic-eda.git
cd titanic-eda
