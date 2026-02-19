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