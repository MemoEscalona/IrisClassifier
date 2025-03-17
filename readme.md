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
