import statistics

##################################################
nums = [3, 5, 2, 7, 8, 10]

    
print(statistics.mean(nums))
print(statistics.stdev(nums))
print(statistics.median_low(nums))
print(statistics.median(nums))

####################################################

megicians = ['alice', 'david', 'carolina']
for megician in megicians:
    print(f"{megician.title()}, that was a great trick!")
    print(f"I can't wait to see you next trick, {megician.title()}.\n")
print('Thank you, everyone. That was a great magic show!')
