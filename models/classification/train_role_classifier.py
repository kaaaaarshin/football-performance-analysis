import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.svm import SVC

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

df = pd.read_csv(
    "data/processed/player_roles.csv"
)

print(df.head())

X = df.drop(
    columns=[
        "player",
        "cluster",
        "role"
    ]
)

y = df["role"]

label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)

print(
    label_encoder.classes_
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)

scaler = StandardScaler()

X_train = scaler.fit_transform(
    X_train
)

X_test = scaler.transform(
    X_test
)

model = SVC(
    kernel="rbf",
    C=1.0,
    gamma="scale",
    random_state=42
)

model.fit(
    X_train,
    y_train
)

y_pred = model.predict(
    X_test
)

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nAccuracy:")
print(round(accuracy * 100, 2), "%")

print(
    "\nClassification Report:\n"
)

print(
    classification_report(
        y_test,
        y_pred,
        target_names=label_encoder.classes_
    )
)

print(
    "\nConfusion Matrix:\n"
)

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)