provinces_list = []

# Open the provinces.txt file for reading.
with open('provinces.txt') as provinces:

    # Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
    for province in provinces:
        province = province.strip()
        provinces_list.append(province)

# Print the entire list.
print(provinces_list)

# Remove the first element from the list.
provinces_list.pop(0)

# Remove the last element from the list.
provinces_list.pop()

# Replace all occurrences of "AB" in the list with "Alberta".
for i in range(len(provinces_list)):
    if provinces_list[i] == 'AB':
        provinces_list[i] = 'Alberta'

# Count the number of elements that are "Alberta" and print that number.
alberta_appears = provinces_list.count('Alberta')

print(f'\nAlberta occurs {alberta_appears} times in the modified list.')
