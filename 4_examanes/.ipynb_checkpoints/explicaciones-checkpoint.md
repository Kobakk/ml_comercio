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
| Motor (Llave) | Potencia (Valor) |
| :--- | :---: |
|2.0 |200 , 210 |
|1.6 | 100 , 110 |
