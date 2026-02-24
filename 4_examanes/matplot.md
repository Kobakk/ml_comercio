# visualización 

## nube de puntos
- valores númericos por parte del eje x
  
```python
import matplotlib.pyplot as plt
plt.figure(figsize=(15, 10)) # tamañó del cuadro, importante para fijar 
plt.scatter(df["x_eje"],df["y_eje"])
```

## vista de barras

```python
plt.bar(df["x_eje"],df["y_eje"])
```

## ejemplos vista boxplot
Necesitamso realizar alguna transformación con estos valores 

- valores númericos por parte del eje x

```python
plt.figure(figsize=(12,7))

marcas = sorted(df['brand'].unique()) # marcas ordenadas por orden alfabetico
precio_marca = [df[df['brand'] == marca]['price'] for marca in marcas] # no entiendo la siguiente consulta

plt.bloxpot(
    precio_marca,
    marcas,
    patch_artist=True,
    boxprops=dict(facecolor='blue', color='navy')
)
 ```