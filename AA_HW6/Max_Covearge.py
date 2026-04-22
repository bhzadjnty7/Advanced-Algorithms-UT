def max_coverage(towers, users, k):
    """
    towers: list of sets, each representing users covered by a tower
    users: set of all users
    k: number of towers we can select
    """
    selected_towers = []  # Selected towers
    covered_users = set()  # Covered users
    
    for _ in range(k):
        # Find the tower that covers the most new users
        max_additional_coverage = 0
        best_tower = None
        
        for i, tower in enumerate(towers):
            if i not in selected_towers:
                # Calculate the number of new users this tower covers
                new_coverage = len(tower - covered_users)
                if new_coverage > max_additional_coverage:
                    max_additional_coverage = new_coverage
                    best_tower = i
        
        # If a tower was found that covers new users
        if best_tower is not None:
            selected_towers.append(best_tower)
            covered_users = covered_users.union(towers[best_tower])
    
    return selected_towers, covered_users