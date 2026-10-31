import heapq

def min_connection_cost(cables: list[int]) -> int:
    heap = cables.copy()
    heapq.heapify(heap)

    total_cost = 0
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        connected_cable = first + second
        total_cost += connected_cable
        heapq.heappush(heap, connected_cable)

    return total_cost

if __name__ == "__main__":
    cables = [4, 3, 2, 6]

    total_cost = min_connection_cost(cables)

    print(f"Мінімальні загальні витрати: {total_cost}")