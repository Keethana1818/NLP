def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)

    # initialize matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # fill matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # deletion
                dp[i][j - 1] + 1,      # insertion
                dp[i - 1][j - 1] + cost  # substitution
            )

    return dp, dp[m][n]


word1 = "START"
word2 = "STARE"

matrix, distance = levenshtein_distance(word1, word2)

print("Levenshtein Distance:", distance)
print("\nMatrix:")
for row in matrix:
    print(row)
