def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1

    print (counter)
    
    print(sorted(counter.items(), key=lambda item: item[1]))

    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]

    return letter

print("Running: get_most_common_letter('hello')")
print("Expected: l")
print("Actual:", get_most_common_letter("hello"))


