# main.py
import matplotlib.pyplot as plt
from src.bubble_sort import bubble_sort_array, LinkedList, bubble_sort_linked_list
from src.utils import measure_time_and_metrics_array, measure_time_linked_list, generate_random_array, generate_random_linked_list, save_results

# Testando para diferentes tamanhos de dados
sizes = [100, 1000, 10000]
array_times = []
linked_list_times = []
array_comparisons = []
linked_list_comparisons = []
array_swaps = []
linked_list_swaps = []

# Gerando os dados para Arrays e Listas Ligadas
for size in sizes:
    # Array
    arr = generate_random_array(size)
    time, comparisons, swaps = measure_time_and_metrics_array(bubble_sort_array, arr)
    array_times.append(time)
    array_comparisons.append(comparisons)
    array_swaps.append(swaps)

    # Lista Ligada
    linked_list = generate_random_linked_list(size)
    time, comparisons, swaps = measure_time_linked_list(bubble_sort_linked_list, linked_list)
    linked_list_times.append(time)
    linked_list_comparisons.append(comparisons)
    linked_list_swaps.append(swaps)

# Salvando os resultados
save_results('data/array_results.csv', sizes, array_times, array_comparisons, array_swaps)
save_results('data/linked_list_results.csv', sizes, linked_list_times, linked_list_comparisons, linked_list_swaps)

# Gerando gráficos
def plot_results():
    plt.figure(figsize=(12, 8))

    # Gráfico de tempo de execução
    plt.subplot(2, 2, 1)
    plt.plot(sizes, array_times, label="Array - Tempo", color='blue', marker='o')
    plt.plot(sizes, linked_list_times, label="Lista Ligada - Tempo", color='red', marker='o')
    plt.xlabel("Tamanho do Array/Listas")
    plt.ylabel("Tempo de Execução (segundos)")
    plt.title("Tempo de Execução")
    plt.legend()

    # Gráfico de comparações
    plt.subplot(2, 2, 2)
    plt.plot(sizes, array_comparisons, label="Array - Comparações", color='blue', marker='o')
    plt.plot(sizes, linked_list_comparisons, label="Lista Ligada - Comparações", color='red', marker='o')
    plt.xlabel("Tamanho do Array/Listas")
    plt.ylabel("Número de Comparações")
    plt.title("Número de Comparações")
    plt.legend()

    # Gráfico de trocas
    plt.subplot(2, 2, 3)
    plt.plot(sizes, array_swaps, label="Array - Trocas", color='blue', marker='o')
    plt.plot(sizes, linked_list_swaps, label="Lista Ligada - Trocas", color='red', marker='o')
    plt.xlabel("Tamanho do Array/Listas")
    plt.ylabel("Número de Trocas")
    plt.title("Número de Trocas")
    plt.legend()

    # Exibir os gráficos
    plt.tight_layout()
    plt.show()

plot_results()
