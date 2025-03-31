"""
Problema: Máximo Subarreglo (Kadane + DaC)
Autores: Gerson Ramírez
         Diego Valenzuela
Descripción: Este proyecto explora el problema del Máximo Subarreglo mediante dos enfoques 
             algorítmicos: Programación Dinámica (Kadane) y Divide y Conquista.
Curso: Análisis y Diseño de Algoritmos - UVG 2025
"""

import time
import random
import numpy as np
import matplotlib.pyplot as plt


def kadane(arr):
    max_so_far = current_max = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if current_max + arr[i] < arr[i]:
            current_max = arr[i]
            s = i
        else:
            current_max += arr[i]

        if current_max > max_so_far:
            max_so_far = current_max
            start = s
            end = i

    return max_so_far, start, end

def max_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    sum_temp = 0
    max_left = mid

    for i in range(mid, low - 1, -1):
        sum_temp += arr[i]
        if sum_temp > left_sum:
            left_sum = sum_temp
            max_left = i

    right_sum = float('-inf')
    sum_temp = 0
    max_right = mid + 1

    for i in range(mid + 1, high + 1):
        sum_temp += arr[i]
        if sum_temp > right_sum:
            right_sum = sum_temp
            max_right = i

    return left_sum + right_sum, max_left, max_right

def max_subarray_dac(arr, low, high):
    if low == high:
        return arr[low], low, high

    mid = (low + high) // 2

    left_sum, left_low, left_high = max_subarray_dac(arr, low, mid)
    right_sum, right_low, right_high = max_subarray_dac(arr, mid + 1, high)
    cross_sum, cross_low, cross_high = max_crossing_subarray(arr, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_sum, left_low, left_high
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_sum, right_low, right_high
    else:
        return cross_sum, cross_low, cross_high

def find_max_subarray(arr):
    return max_subarray_dac(arr, 0, len(arr) - 1)

def measure_time(algorithm, test_cases):
    times = []
    for case in test_cases:
        start_time = time.time()
        algorithm(case.copy())  # Usar copia para mantener original intacto
        times.append(time.time() - start_time)
    return times

def generate_test_cases(num_cases=30, min_size=100, max_size=10000):
    sizes = np.linspace(min_size, max_size, num_cases, dtype=int)
    test_cases = []
    for size in sizes:
        arr = [random.randint(-100, 100) for _ in range(size)]
        test_cases.append(arr)
    return test_cases

def plot_performance(sizes, kadane_times, dac_times):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, kadane_times, label="Kadane (O(n))", marker='o')
    plt.plot(sizes, dac_times, label="Divide y Conquista (O(n log n))", marker='s')
    plt.xlabel("Tamaño del arreglo (n)")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Comparación de rendimiento: Kadane vs Divide y Conquista")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("performance_comparison.png")
    plt.show()

if __name__ == "__main__":
    test_cases = generate_test_cases()

    kadane_times = measure_time(kadane, test_cases)
    dac_times = measure_time(find_max_subarray, test_cases)

    sizes = [len(tc) for tc in test_cases]

    plot_performance(sizes, kadane_times, dac_times)

    ejemplo = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Ejemplo Kadane:", kadane(ejemplo))
    print("Ejemplo Divide y Conquista:", find_max_subarray(ejemplo))
