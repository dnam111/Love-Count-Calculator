def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    true_count = 0
    love_count = 0
    love_score = 0

    for letter in "true":
        count = 0
        for char in combined_names:
            if char == letter:
                count += 1
        true_count += count
    for letter in "love":
        count = 0
        for char in combined_names:
            if char == letter:
                count += 1
        love_count += count

    love_score = int(str(true_count) + str(love_count))
    print(love_score)

name_1 = input("Enter the first name: ")
name_2 = input("Enter the second name: ")
calculate_love_score(name_1, name_2)
