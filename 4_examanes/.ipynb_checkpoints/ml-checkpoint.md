# Flujo de procesamiento 

¿Qué es el flujo de procesamineto?
Imputación, escalado, codificación de un dataset:

Lo que creo que hacemos es pasarle x cantidad de variables del 
- Librerias mas útilizadas:
```python 
objv = 'n_col'

x = df.drop(columnas = [objv])
y = df[objv]

n_col = x.select_dtypes(include=['int64', 'float64']).columns
cat_col = x.select_dtypes(include=['object', 'category']).columns

num_transformer = Pipeline(steps = [
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

cat_transformer = Pipeline(steps = [
    ('imputer', SimpleImputer(strategy='mean')),
    ('onehot', OneHotEncoder(handle_unkown = 'ignore', sparse_output=False))
])

preprocessor = ColumnTransformer(
    transformers = [
        ('num', num_transformer, n_col),
        ('cat', cat_transfoermer, cat_cols)
    ]
)
```

1. Selección de x, y determina si sera supervisado o no supervisado. En este caso como solo utilizamos X una var sera sin supervisar.
2. Seleccionamos  valores categóricos y númericos.
3. En el objeto pipeline especificamos que vamos a realizar:
    - numericos: rellenar con la media.
    - categóricos: convertirlo a valores binarios.
4. La columna de transformación

# Aplicar modelo 

Modelo linear para la predicción de precios de un vehículo a partir de sus características.
```python
from sklearn.linear_model import LinearRegression

model_linear = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

model_linear.fit(X_train, y_train)

y_pred = model_linear.predict(X_test)
```
Visualizamos los datos de diferencia en una tabla: 

```python
comparativa = pd.DataFrame({'Real': y_test, 'Predicción': y_pred.round(2)})
comparativa['Error (€)'] = (comparativa['Real'] - comparativa['Predicción']).abs()
print(comparativa.head(10))
```


# La tuberia es clave para el procesamiento de datos:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

modelo_pipeline = Pipeline(steps=[
    ('scaler', StandardScaler()),      # Paso 1: escalado
    ('modelo', RandomForestClassifier())  # Paso 2: modelo
])

modelo_pipeline.fit(X_train, y_train)
predicciones = modelo_pipeline.predict(X_test)
```

Luego aplicamos el modelo 

datos -> preprocesamiento(pipeline) -> selección modelo -> evaluación 