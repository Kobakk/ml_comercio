## f(n) mas útilizadas de pandas
```python
# explorativo
df.head() # 5 filas
df.tail() # 5 filas
df.info() # tipos y nulos
df.describe() # estadísticos básicos
df.shape() # filas x columnas 

# selección 
df["col"] # columna -> serie
df[["col1", "col2"]] # multiples columnas
df.loc[] # por etiquetas
df.iloc[] # por posiciones

# limpieza nulos 
df.isna().sum() # conteo de nulos
df.fillna(valor) # rellenar  nulos
df.dropna() # eliminar nulos
df.drop(columns=["nombre_columna"]) #eliminar columna

# agregaciones
df.mean() #media de una columna
df.mode()[0] # moda columna
df.groupby("col") # agrupar por columna
 
```