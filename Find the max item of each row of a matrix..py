

# he max item of each row of a matrix.


matrics = [ [13,65,70],
              [76,80,100],
              [65,80,95]
              ]
max_item = []
for row in matrics:
    max_value = row[0]
    for item in row:
        if item > max_value:
            max_value = item
    max_item.append(max_value)
print(f"The maximum numbers in matrics is: {max_item}")    