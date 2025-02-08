def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book, key=len, reverse=True)
    numbers = {}
    for i,num in enumerate(phone_book):
        num_len = len(num)
        for n in numbers.keys():
            if num==n[:num_len]:
                return False
            else:
                continue
        numbers[num] =  numbers.get(num, i) 

        
    return answer

# def solution(phone_book):
#     phone_book.sort()  # Sort in lexicographical order (e.g., ["119", "1195524421", "97674223"])

#     for i in range(len(phone_book) - 1):
#         if phone_book[i + 1].startswith(phone_book[i]):  # Check if next number starts with current
#             return False
#     return True


solution(["123", "13", "134"])