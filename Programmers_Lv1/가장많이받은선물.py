from collections import defaultdict

def solution(friends, gifts):
    # Initialize dictionaries to track sent and received gifts
    sent = defaultdict(int)
    received = defaultdict(int)

    # Parse the gifts list to populate sent and received counts
    for gift in gifts:
        giver, receiver = gift.split()
        sent[giver] += 1
        received[receiver] += 1

    # Calculate gift indices
    gift_index = {friend: sent[friend] - received[friend] for friend in friends}

    # Initialize dictionary to track gifts received next month
    next_month_gifts = defaultdict(int)

    # Compare all pairs of friends
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            friend1 = friends[i]
            friend2 = friends[j]

            # Gifts exchanged between friend1 and friend2
            count1_to_2 = sum(1 for g in gifts if g == f"{friend1} {friend2}")
            count2_to_1 = sum(1 for g in gifts if g == f"{friend2} {friend1}")

            if count1_to_2 > count2_to_1:
                next_month_gifts[friend1] += 1
            elif count2_to_1 > count1_to_2:
                next_month_gifts[friend2] += 1
            else:
                # If counts are equal or no gifts exchanged, compare gift indices
                if gift_index[friend1] > gift_index[friend2]:
                    next_month_gifts[friend1] += 1
                elif gift_index[friend2] > gift_index[friend1]:
                    next_month_gifts[friend2] += 1
                # Otherwise, no gift is exchanged

    # Return the maximum number of gifts received next month
    return max(next_month_gifts.values(), default=0)



# def solution(friends, gifts):
#     # Initialize dictionaries for sent and received gifts with all friends having a count of 0
#     sent = {friend: 0 for friend in friends}
#     received = {friend: 0 for friend in friends}

#     # Parse the gifts list to populate sent and received counts
#     for gift in gifts:
#         giver, receiver = gift.split()
#         sent[giver] += 1
#         received[receiver] += 1

#     # Calculate gift indices
#     gift_index = {friend: sent[friend] - received[friend] for friend in friends}

#     # Initialize dictionary to track gifts received next month
#     next_month_gifts = {friend: 0 for friend in friends}

#     # Compare all pairs of friends
#     for i in range(len(friends)):
#         for j in range(i + 1, len(friends)):
#             friend1 = friends[i]
#             friend2 = friends[j]

#             # Gifts exchanged between friend1 and friend2
#             count1_to_2 = sum(1 for g in gifts if g == f"{friend1} {friend2}")
#             count2_to_1 = sum(1 for g in gifts if g == f"{friend2} {friend1}")

#             if count1_to_2 > count2_to_1:
#                 next_month_gifts[friend1] += 1
#             elif count2_to_1 > count1_to_2:
#                 next_month_gifts[friend2] += 1
#             else:
#                 # If counts are equal or no gifts exchanged, compare gift indices
#                 if gift_index[friend1] > gift_index[friend2]:
#                     next_month_gifts[friend1] += 1
#                 elif gift_index[friend2] > gift_index[friend1]:
#                     next_month_gifts[friend2] += 1
#                 # Otherwise, no gift is exchanged

#     # Return the maximum number of gifts received next month
#     return max(next_month_gifts.values(), default=0)
