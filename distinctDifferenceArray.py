def distinctDifferenceArray(nums: List[int]) -> List[int]:
    n = len(nums)
    prefix = [0] * n
    suffix = [0] * n

    seen_prefix = set()
    for i in range(n):
        seen_prefix.add(nums[i])
        prefix[i] = len(seen_prefix)

    seen_suffix = set()
    for i in range(n - 1, -1, -1):
        suffix[i] = len(seen_suffix)
        seen_suffix.add(nums[i])

    return [prefix[i] - suffix[i] for i in range(n)]