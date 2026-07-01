# 🏠 House Price Prediction using Machine Learning

A Machine Learning project that predicts house prices based on multiple housing features such as bedrooms, bathrooms, square footage, location details, and other property characteristics.

The project follows a structured ML workflow including data preprocessing, feature analysis, model training, and prediction using XGBoost Regressor.

---

## 🚀 Features

✔ Data preprocessing and cleaning  
✔ Correlation analysis and visualization  
✔ Handling categorical features  
✔ Train-test data splitting  
✔ XGBoost model training  
✔ Performance evaluation using metrics  
✔ House price prediction system  
✔ Structured project organization using `src`

---

## 📂 Project Structure

```text
House_Price_Prediction/
│
├── data/
│   └── housing_data.csv
│
├── models/
│   └── trained_model.pkl
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── README.md
├── requirements.txt
├── .gitignore
│
└── .venv/
```

---

## 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Hellboy28D/House_Price_Prediction.git
```

Move into project directory:

```bash
cd House_Price_Prediction
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

### Mac/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run preprocessing:

```bash
python src/preprocess.py
```

Train the model:

```bash
python src/train.py
```

Run prediction:

```bash
python src/predict.py
```

---

## 📊 Model Evaluation

The model performance is measured using:

### Mean Absolute Error (MAE)

```text
MAE measures the average prediction error
between actual and predicted house prices
```

### R² Score

```text
R² Score indicates how well the model
fits the data
```

---

## 📈 Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Feature Analysis
   ↓
Encoding Categorical Data
   ↓
Train-Test Split
   ↓
XGBoost Model Training
   ↓
Model Evaluation
   ↓
Prediction System
```

---

## 🔮 Future Improvements

- Hyperparameter tuning
- Better feature engineering
- Model deployment using Flask or Streamlit
- Save and load trained models
- Performance optimization using Rust
- Add real-time prediction API

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

---

## 📜 License

This project is open-source and created for learning and educational purposes.

---

## 👨‍💻 Author

Hellboy28D

GitHub:
https://github.com/Hellboy28D

LinkedIn:
Add your LinkedIn profile here

---
⭐ If you found this project useful, consider giving it a star.
