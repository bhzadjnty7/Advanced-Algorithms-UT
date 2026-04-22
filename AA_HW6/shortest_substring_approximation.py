def shortest_superstring_approximation(strings):
    """
    Approximation algorithm for Shortest Superstring Problem
    Time Complexity: O(n^2 * m) where n = number of strings, m = max string length
    Approximation Ratio: O(H_n) where H_n is the n-th harmonic number
    """
    
    def overlap(s1, s2):
        """Calculate maximum overlap between suffix of s1 and prefix of s2"""
        max_overlap = 0
        min_len = min(len(s1), len(s2))
        
        for i in range(1, min_len + 1):
            if s1[-i:] == s2[:i]:
                max_overlap = i
        
        return max_overlap
    
    def merge_strings(s1, s2, overlap_len):
        """Merge two strings with given overlap length"""
        return s1 + s2[overlap_len:]
    
    # Create a copy of input strings
    remaining_strings = strings.copy()
    
    # Start with the first string
    result = remaining_strings.pop(0)
    
    # Greedy approach: always merge with string having maximum overlap
    while remaining_strings:
        best_overlap = -1
        best_index = -1
        best_position = 0  # 0: append to result, 1: prepend to result
        
        for i, string in enumerate(remaining_strings):
            # Check overlap when appending string to result
            overlap_append = overlap(result, string)
            if overlap_append > best_overlap:
                best_overlap = overlap_append
                best_index = i
                best_position = 0
            
            # Check overlap when prepending string to result
            overlap_prepend = overlap(string, result)
            if overlap_prepend > best_overlap:
                best_overlap = overlap_prepend
                best_index = i
                best_position = 1
        
        # Merge the best candidate
        selected_string = remaining_strings.pop(best_index)
        
        if best_position == 0:
            # Append to result
            result = merge_strings(result, selected_string, best_overlap)
        else:
            # Prepend to result
            result = merge_strings(selected_string, result, best_overlap)
    
    return result

# Example usage and testing
def test_algorithm():
    """Test the approximation algorithm with examples"""
    
    # Test case 1: Simple case
    strings1 = ["ABCD", "CDEF", "EFGH"]
    result1 = shortest_superstring_approximation(strings1)
    print(f"Input: {strings1}")
    print(f"Output: {result1}")
    print(f"Length: {len(result1)}")
    print()
    
    # Test case 2: More complex case
    strings2 = ["GATC", "ATCG", "TCGA", "CGAT"]
    result2 = shortest_superstring_approximation(strings2)
    print(f"Input: {strings2}")
    print(f"Output: {result2}")
    print(f"Length: {len(result2)}")
    print()
    
    # Verify that all strings are substrings of the result
    def verify_solution(strings, superstring):
        for s in strings:
            if s not in superstring:
                return False
        return True
    
    print(f"Test 1 verification: {verify_solution(strings1, result1)}")
    print(f"Test 2 verification: {verify_solution(strings2, result2)}")

# Run the test
test_algorithm()