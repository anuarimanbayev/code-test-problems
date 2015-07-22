# REVIEW
# Exam Statistics

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for i in grades:
        print(i)

print(print_grades(grades))

def grades_sum(scores):
    total = 0
    for i in scores:
        total += i
    return total

def grades_average(grades):    
    average = grades_sum(grades)/float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance = variance + (average - score) ** 2
    result = variance / float(len(scores))
    return result

def grades_std_deviation(variance):
    return variance ** 0.5
    
print(grades_sum(grades))
print(grades_average(grades))
print(grades_variance(grades))

variance = grades_variance(grades)

print(grades_std_deviation(variance))
