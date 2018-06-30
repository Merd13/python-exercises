def square_numbers(nums):
    for i in nums:
        yield (i*i)


#List : 
# def square_numbers(nums):
# 	squars = []
# 	for i in nums:
# 		squars.append(i * i)

# 	return squars



my_nums = square_numbers([1,2,3,4,6])

# my_nums = [(]x*x for x in [1,2,3,4,5]]
# my_nums = (x*x for x in [1,2,3,4,5])

# print next(my_nums)

# print 'lenght of my list is : {}'.format(len(my_nums))
# print 'My List Is: {} AND, lenght of my list is : {}'.format(my_nums, len(my_nums))


# print list(my_nums) # [1, 4, 9, 16, 25]

for num in my_nums:
    print num