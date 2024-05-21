def heapify(arr, n, i, key=lambda x: x):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and key(arr[l]) > key(arr[largest]):
        largest = l
    if r < n and key(arr[r]) > key(arr[largest]):
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)

def heap_sort(arr, key=lambda x: x):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key)
def sort_routes(routes, criterion):
    if criterion == 'distance':
        key = lambda route: route[1]
    elif criterion == 'layovers':
        key = lambda route: len(route[0]) - 2
    else:
        return routes

    heap_sort(routes, key=key)
    return routes

routes = [
    (['City A', 'City B', 'City C'], 1000),  # Example route with distance 1000
    (['City A', 'City D', 'City E', 'City C'], 1500),  # Example route with distance 1500
    # Add more routes as needed
]

# Example usage:
sorted_by_distance = sort_routes(routes, 'distance')
sorted_by_layovers = sort_routes(routes, 'layovers')

print("Sorted by Distance:",sorted_by_distance)
print("\nSorted by Layovers:",sorted_by_layovers)
