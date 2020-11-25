def max_sub_array_01(nums) -> int:
    if bool(nums):
        global_max = local_max = nums[0]
        s = e = r = 0
        for i in range(1, len(nums)):
            if nums[i] > local_max + nums[i]:
                local_max = nums[i]
                r = i
            else:
                local_max = local_max + nums[i]
            if local_max > global_max:
                global_max = local_max
                s = r
                e = i
        res = 0
        for v in nums[s:e + 1]:
            res += v
        return res


a1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub_array_01(a1))
