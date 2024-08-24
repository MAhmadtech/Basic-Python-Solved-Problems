


# Write a program to find histogram of a given set of numbers. Take bin size from user. Print the result in the form of a dictionary


numbers = [12, 15, 7, 10, 22, 5, 9, 14, 18, 20]  
bin_size = int(input("Enter the bin size: "))  


histogram = {}

for number in numbers:
    bin_range = (number // bin_size) * bin_size
    if bin_range in histogram:
        histogram[bin_range] =  histogram[bin_range] + 1
    else:
        histogram[bin_range] = 1


print("Histogram:", histogram)
