# SIMULACIÓN DE LO CLÁSICO A LO CUÁNTICO

Este es un repositorio que tiene algunas funciones diferentes para realizar algunas operaciones para diferentes sistemas.
1. Los experimentos de la canicas con coeficiente booleanos
2. Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.
3. Experimento de las múltiples rendijas cuántico.
4. Cree una función para graficar con un diagrama de barras que muestre las probabilidades de un vector de estados.




### Ejecutar Test.

- Clonar repositorio ``` git clone https://github.com/Juc28/CNYT-DeLoClasicoALoCuantico.git ```

- Cambiar directorio ``` cd CNYT-DeLoClasicoALoCuantico ```

- Ejecutar .py correspondiente ``` py TestClassicToQuantum.py ```


### Para sistemas deterministas:

Si desea usar una función por su cuenta, solo tiene que abrir el archivo **classToQuan.py** y ejecutarlo usando esta sintaxis:
```python
m = [[c, d], [e, f]]			 # Boolean matrix
v = [[a], [b]]                           # Real vector
t = s					 # Entero
NombreDeLaFuncion(m, v, t)
```

### Para sistemas probabilísticos:

Si desea usar una función por su cuenta, solo tiene que abrir el archivo **classToQuan.py** y ejecutarlo usando esta sintaxis:
```python
m = [[i, j], [k, l]]	 	         # Real matrix
v = [[a], [b]]                           # Real vector
t = s					 # Entero
NombreDeLaFuncion(m, v, t)
```

### Para sistemas cuánticos:

Si desea usar una función por su cuenta, solo tiene que abrir el archivo **classToQuan.py** y ejecutarlo usando esta sintaxis:
```python
m2 = [[[i, j], [k, l]], [[m, n], [o, p]]] # Complex matrix
v1 = [[a, b], [c, d]]                     # Complex vector
t = s			        	  # Entero
NombreDeLaFuncion(m, v, t)
```

### Para plots:

Si desea usar una función por su cuenta, solo tiene que abrir el archivo **classToQuan.py** y ejecutarlo usando esta sintaxis:
```python
v = [a, b, c, d]                 # Real vector
NombreDeLaFuncion(v)
```
Esta función no tiene una prueba porque implementará una imagen, por lo que si desea probarla, simplemente ejecútela como se indica en la información anterior.

### AUTOR

> Juliana Castro [Juc28](https://github.com/Juc28)
