

def getMaximumSpending(books, budget):
    total_spending = 0
    total_books = 0
    books.sort()
    for b in books:
        if total_spending + b < budget:
            total_spending += b
            total_books += 1

    return total_books, total_spending

if __name__ == '__main__':
    books = [7, 8, 9, 10, 8, 7, 10, 5, 8, 9]
    budget = 50

    result_book, result_spending = getMaximumSpending(books, budget)
    print(result_book)
    print(result_spending)

