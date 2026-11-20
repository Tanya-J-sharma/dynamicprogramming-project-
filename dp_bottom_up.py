
def solve(instance, seed=42):

    universe = instance["universe"]
    subsets = instance["subsets"]

    # Give every element a position.
    elements = sorted(universe)

    position = {
        element: i
        for i, element in enumerate(elements)
    }

    n = len(elements)
    full = (1 << n) - 1

    # Convert subsets into bitmasks.
    masks = []

    for subset in subsets:
        mask = 0

        for element in subset:
            mask |= 1 << position[element]

        masks.append(mask)

    # Create the DP table.
    INF = float("inf")
    n_states = 1 << n

    dp = [INF] * n_states

    parent_set = [-1] * n_states
    parent_mask = [-1] * n_states

    # Starting point: nothing covered.
    dp[0] = 0

    # Try every possible state.
    for mask in range(n_states):

        if dp[mask] == INF:
            continue

        # Try adding every subset.
        for i, subset_mask in enumerate(masks):

            new_mask = mask | subset_mask

            if dp[mask] + 1 < dp[new_mask]:

                dp[new_mask] = dp[mask] + 1

                parent_set[new_mask] = i
                parent_mask[new_mask] = mask

    # Check whether a solution exists.
    if dp[full] == INF:
        raise ValueError("No feasible cover")

    # Recover the selected subsets.
    answer = []
    current = full

    while current != 0:

        answer.append(parent_set[current])
        current = parent_mask[current]

    answer.reverse()

    return answer
