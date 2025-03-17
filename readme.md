# 🚀 Red Neuronal Multicapa para la Clasificación del Conjunto de Datos Iris 🌸  

¡Bienvenido a este proyecto de *Machine Learning*! Aquí entrenamos una **red neuronal multicapa** para clasificar flores del famoso **conjunto de datos Iris** 🌿🌺🌼 utilizando *scikit-learn* y Docker.  

---

## 📌 Descripción del Proyecto  
Este proyecto implementa una **Red Neuronal Artificial (RNA) con dos capas ocultas** utilizando `MLPClassifier` de `sklearn`. La red aprende a clasificar correctamente las especies de flores en el conjunto de datos Iris mediante *backpropagation* y optimización con *Adam*.  

### 📊 **Arquitectura de la Red**
- ✅ **Entrada:** 4 características del iris (longitud y ancho de pétalo/sépalo).  
- ✅ **Capas ocultas:** 2 capas ocultas con 10 y 5 neuronas.  
- ✅ **Salida:** 3 clases (*setosa*, *versicolor*, *virginica*).  
- ✅ **Función de activación:** *ReLU*.  
- ✅ **Entrenamiento:** *Backpropagation* con **1000 iteraciones**.  

📊 **Métrica clave:** Precisión de clasificación en el conjunto de prueba.  

---

## 🛠️ Requisitos
### 📌 **1️⃣ Opción 1: Ejecutar en tu Máquina (Python)**
Necesitas instalar las siguientes dependencias:  

```bash
pip install scikit-learn numpy matplotlib
```
### 📌 **2 Opción 2: Ejecutar en Docker (Recomendado)**
Si prefieres aislar el entorno con Docker, instala Docker y sigue las instrucciones más abajo.

## 🚀 Ejecución del Proyecto
### ▶ Ejecutar en Python
Si prefieres correrlo en tu sistema sin Docker:
```bash
python iris_nn.py
```
### ▶ Ejecutar en Docker
Si deseas ejecutarlo dentro de un contenedor Docker, sigue estos pasos:
1️⃣ Construir la imagen de Docker:
```bash
docker build -t iris_nn .
```
2️⃣ Ejecutar el contenedor:
```bash
docker run --rm iris_nn
```

## 📊 Ejemplo de Resultados
Tras entrenar la red, se obtiene un reporte de clasificación como este:
Precisión del modelo en el conjunto de prueba: 0.9667

Reporte de Clasificación:
              precision    recall  f1-score   support
   setosa        1.00       1.00      1.00        10
   versicolor    1.00       0.90      0.95        10
   virginica     0.91       1.00      0.95        10

   accuracy                           0.97        30
   macro avg      0.97       0.97      0.97        30
   weighted avg   0.97       0.97      0.97        30

### ¿Qué significa esto?
✅ Nuestra red neuronal clasifica correctamente el 96.67% de las muestras en el conjunto de prueba.
✅ Setosa se clasifica con 100% de precisión, mientras que versicolor y virginica tienen ligeros errores.

### 🎯 ¿Por qué es Importante este Proyecto?
🔥 Demuestra la eficacia de las redes neuronales en problemas de clasificación.
🔥 Es una excelente introducción a MLP y backpropagation en scikit-learn.
🔥 Es portable con Docker, permitiendo fácil ejecución en cualquier sistema.