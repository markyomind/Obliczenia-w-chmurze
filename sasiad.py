import random
import math
import matplotlib.pyplot as plt
import time

#losowanie polozen miast
def generate_cities(num_cities, x_range=(0, 1000), y_range=(0, 1000)):
   
    return [(random.uniform(*x_range), random.uniform(*y_range)) for _ in range(num_cities)]

#liczenie odleglosci miedzy miastami
def calculate_distance_matrix(cities):
    
    num_cities = len(cities)
    distance_matrix = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                x1, y1 = cities[i]
                x2, y2 = cities[j]
                distance_matrix[i][j] = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance_matrix

#liczenie ktore miasto najblizej
def nearest_neighbor(distance_matrix, start=0):
    
    n = len(distance_matrix)
    visited = [False] * n  #odwiedzone miasta
    path = [start]        
    visited[start] = True
    total_cost = 0         #calkowita droga

    current_city = start
    for _ in range(n - 1):
        # Find the nearest unvisited city
        nearest_city = None
        min_distance = float('inf')
        for city in range(n):
            if not visited[city] and distance_matrix[current_city][city] < min_distance:
                nearest_city = city
                min_distance = distance_matrix[current_city][city]

        #przemieszczenie do najblizszego miasta
        path.append(nearest_city)
        visited[nearest_city] = True
        total_cost += min_distance
        current_city = nearest_city

    #powrot do miasta startowego
    total_cost += distance_matrix[current_city][start]
    path.append(start)

    return path, total_cost

#rysowanie drogi
def plot_cities_and_path(cities, path, filename="wykres_drogi.png"):
    
    x_coords = [cities[i][0] for i in path]
    y_coords = [cities[i][1] for i in path]

    plt.figure(figsize=(10, 6))
    plt.scatter(*zip(*cities), color='blue', label='Miasta')
    plt.plot(x_coords, y_coords, color='red', linestyle='-', marker='o', label='Trasa')
    
    for i, (x, y) in enumerate(cities):
        plt.text(x, y, str(i), fontsize=8, color='green')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Problem komiwojażera - algorytm najbliższego sąsiada')
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

#wywolywanie funkcji
num_cities = 5000
cities = generate_cities(num_cities)

start_time = time.time()
distance_matrix = calculate_distance_matrix(cities)
path, cost = nearest_neighbor(distance_matrix, start=0)
end_time = time.time()

execution_time = end_time - start_time

print("Optymalna kolejnosc odwiedzania miast:", path)
print("Calkowita droga:", cost)
print(f"Czas obliczen: {execution_time:.4f} sekund")

plot_cities_and_path(cities, path, filename="wykres_drogi.png")
print("Wykres zapisano w pliku 'wykres_drogi.png'.")
