import math

# Maximum Subarray Sum Size K

# Time Complexity: O(n * k)

# def max_subarray_sum_size_k(nums, k):
#    max_sum = float('-inf')
#    for i in range(0, len(nums) - k + 1):
#       current_sum = sum(nums[i : i + k])
#        if current_sum > max_sum:
#           max_sum = current_sum
#   return max_sum

# Time Complexity: O(n)

def max_subarray_sum_size_k(nums, k):
    current_sum = sum(nums[:k])         # Space Complexity: O(k) because nums is a copy, use a separate
                                        # for loop and compute sum to get an O(1) Space
    max_sum = current_sum
    for i in range(0, len(nums) - k):
        current_sum -= nums[i]
        current_sum += nums[i + k]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


# Maximum Subarray Product Size K

# Time Complexity: O(n * k)

# def max_subarray_product_size_k(nums, k):
#    max_prod = float('-inf')
#    for i in range(0, len(nums) - k + 1):
#        current_prod = math.prod(nums[i : i + k])
#        if current_prod > max_prod:
#            max_prod = current_prod
#    return max_prod

# Time Complexity: O(n)

def max_subarray_product_size_k(nums, k):
    current_prod = math.prod(nums[:k])
    max_prod = current_prod
    for i in range(0, len(nums) - k):
        current_prod /= nums[i]
        current_prod *= nums[i + k]
        if current_prod > max_prod:
            max_prod = current_prod
    return max_prod

# Find Target Sum with K Fixed Size

def target_subarray_size_k(nums, target, k):
    count = 0
    currSum = sum(nums[:k])
    if currSum == target:
        count += 1
    for i in range(0, len(nums) - k):
        currSum -= nums[i]
        currSum += nums[i + k]
        if currSum == target:
            count += 1
    return count

# Find Target Sum with Variable Window Size

def find_subarray_sum(nums, target_sum):
    start = 0
    window_sum = 0
    for end in range(0, len(nums)):
        window_sum += nums[end]
        while window_sum > target_sum:
            window_sum -= nums[start]
            start += 1
        if window_sum == target_sum:
            return [start, end]

# Longest Subarray Sum

def longest_subarray_sum(nums, target_sum):
    start = 0
    currInterval = 0
    longest = -1
    window_sum = 0
    for end in range(0, len(nums)):
        window_sum += nums[end]
        while window_sum > target_sum:
            window_sum -= nums[start]
            start += 1
        if window_sum == target_sum:
            currInterval = end - start + 1
            longest = max(currInterval, longest)
    return longest




nums = [1, 4, 1, 10, 25, 3, 5, 0, 26]
nums1 = [1, 4, 1, 6, -3, 3, -5, 2, 26]
nums2 = [2, 3, 2, 2, 3, 1, 3, 8, 5, 0, 2, 4]
nums3 = [3, 1, 4, 9, 2, 1, 7, 5]
nums4 = [4, 3, 3, 2, 1, 5, 2, 3, 5, 10, 1]
print(max_subarray_sum_size_k(nums, 4))
print(max_subarray_product_size_k(nums1, 4))
print(target_subarray_size_k(nums2, 7, 3))
print(find_subarray_sum(nums3, 10))
print(longest_subarray_sum(nums4, 10))

