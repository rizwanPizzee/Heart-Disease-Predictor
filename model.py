import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.pipeline import make_pipeline

df = pd.read_csv('heart.csv')

target = "HeartDisease"

all_cols = df.columns.tolist()
feature_cols = [col for col in all_cols if col != target]

categorical_cols = df[feature_cols].select_dtypes(include=['object', 'category']).columns.tolist()
numerical_cols = df[feature_cols].select_dtypes(include=['number']).columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numerical_cols),
        ("cat", OneHotEncoder(drop='first', handle_unknown='ignore'), categorical_cols),
    ],
    remainder='drop'
)

pipeline = make_pipeline(
    preprocessor,
    RandomForestClassifier(n_estimators=100, random_state=42)
)

X = df[feature_cols]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, stratify=y, random_state=42)
pipeline.fit(X_train, y_train)

pickle.dump(pipeline, open('model.pkl', 'wb'))