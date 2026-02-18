## funciones group_by 

```python
df['horsepower'] = df['horsepower'].fillna(df.groupby('engine_size')['horsepower'].transform('mean'))

df['horsepower'] = df['horsepower'].fillna(df['horsepower'].mean())
```

### group by 

agrupamos filas de una misma tabla que comparten valor 

```python 
df.groupby('engine_size')['horsepower'].mean()
```
partimos de una tabla desordenada

| Motor (Llave) | Potencia (Valor) |
| :--- | :---: |
|2.0 |200 |
|1.6 | 100 |
|2.0 | 210 |
|1.6 | 110 |

1. Agrupamos en valores similares de la col a seleccionar (motor )
| Motor (Llave) | Potencia (Valor) |
| :--- | :---: |
|2.0 |200 |
|2.0 | 210 |
|1.6 | 100 |
|1.6 | 110 |

¿O ocurre lo siguiente? Los convierte en cadenas: 

```python
df.groupby('engine_size')['horsepower'].mean()
```
| Motor (Llave) | Potencia (Valor) |
| :--- | :---: |
|2.0 |200 , 210 |
|1.6 | 100 , 110 |

La verdad es que no solo los agrupa, ordena y apartir de ahi 


### ver las cardinalidades de las columnas 

Todo el trabajo de núnermos sobre relaciones y cardinalidad entre columnas, se llama cardinalidad. 

- Para detectar columnas no informativas: se buscan aquellas **que no aportan variabilidad** o que estan tan vacías que no permiten extraer patrones.
1. columnas constante (varianza zero ):   `unique() == 1` una columna tiene varianza 0, no puede explicar cambios en otras variables.
2. identificadores únicos ( alta cardinalidad ): 