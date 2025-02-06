#DFS + Backtracking
from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0

    # Try all possible orders using permutations
    for perm in permutations(dungeons):
        hp, count = k, 0
        for required, taken in perm:
            if hp >= required:  # Can enter the dungeon
                hp -= taken  # Lose HP
                count += 1
            else:
                break  # Stop when we can't enter a dungeon
        max_dungeons = max(max_dungeons, count)  # Update max dungeons explored

    return max_dungeons
# Complexity Analysis
# Generating permutations: O(N!)
# Checking each order: O(N)
# Total Complexity: O(N × N!), which is feasible for N ≤ 8 (~40,320 worst case).

# def solution(k, dungeons):
#     answer = 0
#     dungeons.sort(reverse = True, key=lambda x: x[0]-x[1])
    
#     for required, taken in dungeons:
#         if k >= required:
#             answer += 1
#             k -= taken
#     return answer

# Alternative: Faster DFS Without Permutations
# If N grows larger (e.g., N = 1000), we should use a backtracking DFS to prune unnecessary paths.

# hp: Current available HP.
# dungeons: List of available dungeons.
# visited: Boolean list to track explored dungeons.
# count: Number of dungeons explored so far.
def dfs(hp, dungeons, visited, count):
    #Keeps track of the maximum number of dungeons explored.
    global max_dungeons
    max_dungeons = max(max_dungeons, count)  # Update max explored count
    
    # Try every dungeon that hasn't been visited and has enough HP.
    # Mark dungeon as visited, recursively call dfs, then undo (backtrack).
    for i in range(len(dungeons)):
        if not visited[i] and hp >= dungeons[i][0]:  # Can explore
            visited[i] = True
            dfs(hp - dungeons[i][1], dungeons, visited, count + 1)
            visited[i] = False  # Backtrack


# Initializes max_dungeons = 0.
# Starts DFS with all dungeons unvisited.
# Returns the maximum number of dungeons explored.
def solution(k, dungeons):
    global max_dungeons
    max_dungeons = 0
    visited = [False] * len(dungeons)
    dfs(k, dungeons, visited, 0)
    return max_dungeons

# Instead of trying every permutation (O(N!) complexity), we use DFS with backtracking to efficiently explore possible dungeon sequences without generating all permutations explicitly.

# DFS is useful because:

# We try each dungeon in any order without pre-sorting or pre-generating permutations.
# We backtrack if a dungeon cannot be explored, preventing unnecessary searches.
# We track visited dungeons to avoid revisiting the same one in a sequence.


#🔹 DFS avoids generating all permutations explicitly, making it faster than brute-force permutations.
#🔹 Still runs efficiently for N ≤ 8 but better scales for N ≈ 1000.

# Why This is Faster than Brute-Force Permutations?
# Approach	Time Complexity	Explanation
# Brute-force (Permutations)	O(N!)	Tries every order explicitly
# DFS with Backtracking	O(N × 2^N)	Only explores valid dungeon orders
# Why O(N × 2^N)?
# For each dungeon, we either explore it or skip it (binary choice).
# There are 2^N possible dungeon exploration paths.
# Each path takes O(N) operations (since we iterate over dungeons).
# For N = 8, brute-force O(8!) = 40,320, while DFS runs in ~256 steps (O(8 × 2⁸)), a massive improvement!

#summary
# DFS with Backtracking avoids unnecessary computations.
# Much faster than brute-force permutations (O(N × 2^N) vs O(N!)).
# Efficient for N ≤ 1000 dungeons.
# Finds the maximum dungeons explored in optimal order.