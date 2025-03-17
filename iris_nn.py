from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Cargar el conjunto de datos Iris
iris = load_iris()
X, y = iris.data, iris.target

# 2. Dividir los datos en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 3. Normalizar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Definir la red neuronal con dos capas ocultas (10 y 5 neuronas)
mlp = MLPClassifier(hidden_layer_sizes=(10, 5), activation='relu', solver='adam', max_iter=1000, random_state=42)

# 5. Entrenar el modelo
mlp.fit(X_train, y_train)

# 6. Evaluar el modelo
y_pred = mlp.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# 7. Imprimir los resultados
print(f"Precisión del modelo en el conjunto de prueba: {accuracy:.4f}\n")
print("Reporte de Clasificación:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
