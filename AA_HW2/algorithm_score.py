def min_books_needed(scores):
    n = len(scores)
    # Initialize the books array
    books = [1] * n  # Each person gets at least one book
    
    # Left to right pass
    for i in range(1, n):
        if scores[i] > scores[i-1]:
            books[i] = books[i-1] + 1
            
    # Right to left pass
    for i in range(n-2, -1, -1):
        if scores[i] > scores[i+1]:
            books[i] = max(books[i], books[i+1] + 1)
    
    return sum(books)  # Total number of books needed

scores = [1, 2, 4, 2, 3, 1]
print(min_books_needed(scores))