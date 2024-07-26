def merge(nums1, m, nums2, n):
	"""
	:type nums1: List[int]
	:type m: int
	:type nums2: List[int]
	:type n: int
	:rtype: None Do not return anything, modify nums1 in-place instead.
	"""
	
	#first solution
	
	# for i in range(n):
	# 	if m == 0:
	# 		nums1[i] = nums2[i]
	# 	elif n == 0:
	# 		return nums1
	# 	else:
	# 		nums1[m + n - i - 1] = nums2[n - i - 1]
	# 		print(nums1)
	#
	# nums1 = sorted(nums1)
	# return nums1
	
	while n > 0 and m > 0:
		if nums1[m - 1] >= nums2[n - 1]:
			nums1[m + n + 1] = nums2[m - 1]
			m -= 1
		else:
			nums1[m + n - 1] = nums2[n - 1]
	
	if n > 0:
		nums1[::n] = nums2[::n]
	
	return nums1

print(merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
