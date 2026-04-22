import heapq

def min_rope_cost(ropes):
    # Convert array to min heap
    heapq.heapify(ropes)
    total_cost = 0
    
    # While there is more than one rope
    while len(ropes) > 1:
        # Take the two shortest ropes
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)
        
        # Combine ropes and calculate cost
        cost = first + second
        total_cost += cost
        
        # Add the new rope to the heap
        heapq.heappush(ropes, cost)
    
    return total_cost

ropes = [4, 3, 2, 6]
print(min_rope_cost(ropes))  # Output: 29