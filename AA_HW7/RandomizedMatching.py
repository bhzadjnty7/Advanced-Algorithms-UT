def randomized_matching(bolts, nuts):
    if len(bolts) <= 1:
        return [(bolts[0], nuts[0])]
    
    # Select a random bolt
    pivot_bolt = random.choice(bolts)
    
    # Partition nuts based on the pivot bolt
    smaller_nuts, equal_nuts, larger_nuts = partition_nuts(nuts, pivot_bolt)
    
    # Find the matching nut
    matching_nut = equal_nuts[0]
    
    # Partition bolts based on the matching nut
    smaller_bolts, larger_bolts = partition_bolts(bolts, matching_nut, pivot_bolt)
    
    # Recursive solution
    result = [(pivot_bolt, matching_nut)]
    result.extend(randomized_matching(smaller_bolts, smaller_nuts))
    result.extend(randomized_matching(larger_bolts, larger_nuts))
    
    return result