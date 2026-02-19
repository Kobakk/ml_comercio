# La agrupación
%%17-02-2026%%
Objetivo: Rellenar valores vacios con nulos. 

```python
df['horsepower'] = df['horsepower'].fillna(df.groupby('engine_size')['horsepower'].transform('mean'))

df['horsepower'] = df['horsepower'].fillna(df['horsepower'].mean())
```

## `group_by`

Agrupamos filas de una misma tabla que comparten valor.  

```python 
df.groupby('engine_size')['horsepower'].mean()
```
1. Partimos de una tabla desordenada:

| Motor (Llave) | Potencia (Valor) |
| :--- | :---: |
|2.0 |200 |
|1.6 | 100 |
|2.0 | 210 |
|1.6 | 110 |

2. Agrupamos en valores similares de la col a seleccionar (motor )
| Motor (Llave) | Potencia (Valor) |
| :--- | :---: |
|2.0 |200 |
|2.0 | 210 |
|1.6 | 100 |
|1.6 | 110 |

- ¿O ocurre lo siguiente? Los convierte en cadenas: 

```python
df.groupby('engine_size')['horsepower'].mean()
```
| Motor (Llave) | Potencia (Valor) |
| :--- | :---: |
|2.0 |200 , 210 |
|1.6 | 100 , 110 |

La verdad es que no solo los agrupa, ordena y apartir de ahí, usamos un código como `mean()` o `count()`: 

- Con el mean: 
| Motor (Llave) | Potencia (Valor) |
| :--- | :---: |
|2.0 |205 |
|1.6 | 105 |

- Con el count():
| Motor (Llave) | Potencia (Valor) |
| :--- | :---: |
|2.0 |2 |
|1.6 | 1 |  

### ver las cardinalidades de las columnas 

Todo el trabajo de núnermos sobre relaciones y cardinalidad entre columnas, se llama cardinalidad. 

- Para detectar columnas no informativas: se buscan aquellas **que no aportan variabilidad** o que estan tan vacías que no permiten extraer patrones.
1. Columnas constante (varianza zero ):   `unique() == 1` una columna tiene varianza 0, no puede explicar cambios en otras variables.
2. Identificadores únicos ( alta cardinalidad ):
