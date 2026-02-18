### ¿Para que sirve la validación cruzada?
Dividimos los datos en dos partes, uno de entrenamiento y otro de test.
- entrenamiento: para ajustar el modelo
- test: evaluar su capacidad de generalización (denominada prueba de realidad)

1. En la validación cruzada, dividimos los datos repetidamente en entrenamiento y test, obteniendo un modelo para cada para estos resultado de test se promedian, para tener una estimación más robusta del rendimineto. 

2. La forma más habitual es mediante validación *k-fold*, en el que **dividimos los datos en cojuntos del mismo tamaño** como **(k=5 o k=10)**.
   
### Método para entranar K-neighbors

```python
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

i = load_iris()
X, y = i.data, i.target

clasificador = KNeighborsClassifier()
```

## encadenado con tuberias 

dentro del dataset boston, tenemos que limpiar, imaginar y controlar. 


### ¿Para que sirven las métricas de rendimiento?

Como escoger el mejro modelo posible, 
