sumOfCalories =[]
sumCl = 0

with open('data.txt') as f:
    for cl in f.readlines():
        if str(cl) == '\n':
            sumCl = 0
        else:    
            sumCl = sumCl + int(str(cl))
            sumOfCalories.append(sumCl)

    print("Max sum of calories: ",max(sumOfCalories))
    sortedCalories = sorted(sumOfCalories)
    sumOflastSortedCalories = sum(sortedCalories[-3:])
    print("Sum of last 3 soreted Calories: ", int(str(sumOflastSortedCalories)))

f.close()