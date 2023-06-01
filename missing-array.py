def isMissing(arrayInput):
    dedupedRange = set(arrayInput)  # remove any duplicate values
    sortedRange = sorted(dedupedRange)  # sort from lowest to highest so we can iterate
    missing = 0

    for num in range(sortedRange[0], sortedRange[-1]+1):
        # if not isinstance(num, int):
        #     print("Invalid input, non-numeric value detected")
        if num <= 0:
            print("Invalid input, negative number detected")
            break
        if num not in sortedRange:
            missing = num
            if missing == 0:
                return "nothing is missing"
            else:
               return str(missing) + " is missing"



print(isMissing([4, 5, 1, 3, 5]))  # 2 is missing
print(isMissing([4, 3, 5, 6, 8, 2, 1, 3]))  # 7 is missing
print(isMissing([1, 2, 3, 4]))  # nothing is missing
print(isMissing([4, 5, -1, 3, 5]))  # THROW ERROR Invalid input, non-numeric value detected
# print(isMissing([3, 4, 5, 6, 'cfg']))  # THROW ERROR Invalid input, non-numeric value detected
