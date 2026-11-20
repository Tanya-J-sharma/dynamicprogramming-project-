
def solve(instance, seed=42):

    universe = instance["universe"]
    subsets = instance["subsets"]

    elements = sorted(universe)

    position = {
        element: i
        for i, element in enumerate(elements)
    }

    n = len(elements)
    full = (1 << n) - 1

    masks = []

    for subset in subsets:
        mask = 0

        for element in subset:
            mask |= 1 << position[element]

        masks.append(mask)

    memo = {}
    choice = {}

    def solve_mask(mask):

        if mask == full:
            return 0

        if mask in memo:
            return memo[mask]

        best = float("inf")
        best_subset = -1

        for i, subset_mask in enumerate(masks):

            new_mask = mask | subset_mask

            if new_mask == mask:
                continue

            candidate = 1 + solve_mask(new_mask)

            if candidate < best:
                best = candidate
                best_subset = i

        memo[mask] = best
        choice[mask] = best_subset

        return best

    # STEP 7: Solve the original problem
    optimum = solve_mask(0)

    # Check whether a cover exists
    if optimum == float("inf"):
        raise ValueError("No feasible cover")

    # STEP 8: Reconstruct the selected subsets
    answer = []
    current = 0

    while current != full:

        i = choice[current]

        answer.append(i)

        current = current | masks[i]

    # Return the selected subset indices
    return answer
