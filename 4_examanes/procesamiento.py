
df = pd.read_csv("archivo.csv")

df.head()
df.describe()
"""
Valores númiercos 
Valores Categóricos
"""
col_num = df.select_dtypes(include=['number']).columns
col_categ = df.select_dtypes(include=['object', "category"]).columns

for col in col_num:
    unicos = df[col].nunique()
    print(f"col {col} tiene {unicos} calores únicos.")

print(list(col_num))
print(list(col_categ))

"""
detectar valores nulos 
y posiblemenre rellenar con la media
"""
print(df.isna().sum())
print(df.isna().mean() * 100)
# rellenar con la media con el mismo tamaño del motor 
df['horsepower'] = df['horsepower'].fillna(df.groupby('engine_size')['horsepower'].transform('mean'))
df['horsepower'] = df['horsepower'].fillna(df['horsepower'].mean())
"""
columnas no informativas
"""
no_constantes = [col for col in df.columns if df[col].nunique() <= 1]
"""
[col for col in df.columns if df[col].nunique() <= 1]

for col in df.columns
    if df[col].nunique() <=1 
        no_constantes += col
"""

"""
columnas con exceso de nulos
"""
umbral_nulo = 0.5
muchos_nulos = df.columns[df.isnull().mean() > umbral_nulos].tolist()
"""
eliminar columnas innecesarias 
df.drop(columns=['nombre_columna'])

"""

plt.figure(figsize=(11, 6))
#df_plot = df.dropna(subset=["x_col", "y_col"]) # paso opcional, eliminar nube de puntos 
plt.scatter(
    df_plot["x_col"],
    df_plot["y_col"]
    alpha=0.6,
    color="blue",
    edgecolors="white",
    linewidth=0.5
)
# una manera simple la nube de puntos
plt.scatter(
    df["x_col"],
    df["y_col"],
    color="blue"
)

# de una manera simple la 