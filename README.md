# Máximo Subarreglo (Kadane + DaC)
Este proyecto explora el problema del Máximo Subarreglo mediante dos enfoques algorítmicos diferentes:
1. **Programación Dinámica** (Algoritmo de Kadane)
2. **Divide y Conquista**

El problema del Máximo Subarreglo consiste en encontrar el subarreglo contiguo dentro de un arreglo unidimensional de números que tenga la suma más grande.

## Implementaciones

### Algoritmo de Kadane (O(n))
El algoritmo de Kadane es un enfoque de programación dinámica que encuentra el máximo subarreglo en tiempo lineal O(n). La implementación mantiene dos variables: 
- La suma máxima encontrada hasta el momento (`max_so_far`)
- La suma máxima que termina en la posición actual (`current_max`)

Además, el algoritmo rastrea las posiciones de inicio y fin del subarreglo máximo.

### Algoritmo de Divide y Conquista (O(n log n))
La implementación de Divide y Conquista divide el problema en subproblemas más pequeños:
1. Encuentra el máximo subarreglo en la mitad izquierda.
2. Encuentra el máximo subarreglo en la mitad derecha.
3. Encuentra el máximo subarreglo que cruza el punto medio.
4. Retorna el máximo de los tres casos anteriores.

## Análisis de Rendimiento
El proyecto incluye funcionalidades para:
- Generar casos de prueba aleatorios de diferentes tamaños
- Medir el tiempo de ejecución de ambos algoritmos
- Visualizar el rendimiento comparativo mediante gráficas

## Resultados Esperados
- El algoritmo de Kadane (O(n)) debería superar consistentemente al enfoque de Divide y Conquista (O(n log n)) en términos de tiempo de ejecución, especialmente para entradas grandes.
- Ambos algoritmos deben producir resultados idénticos para el mismo conjunto de datos.

## Requisitos
- Python 3.x
- Bibliotecas: time, random, numpy, matplotlib

## Uso
```python
# Ejecutar comparación de rendimiento y visualización
python main.py

# Ejemplo básico de uso
ejemplo = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Ejemplo Kadane:", kadane(ejemplo))
print("Ejemplo Divide y Conquista:", find_max_subarray(ejemplo))
```

## Visualizaciones
El script genera una gráfica comparativa de rendimiento que se guarda como "performance_comparison.png", mostrando la relación entre el tamaño de la entrada y el tiempo de ejecución para ambos algoritmos.
