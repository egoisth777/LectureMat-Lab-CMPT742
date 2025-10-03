[](Project,%20Ray%20Marching%20SDFs.md)# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    # TODO: Implement a basic anagram check
    return sorted(str1) == sorted(str2)

# Follow-up: Modify the function to account for case sensitivity and spaces
def are_anagrams_ignore_case_spaces(str1, str2):
    # TODO: Implement anagram check ignoring case sensitivity and spaces
    st1 = "".join(str1.split()).lower()
    st2 = "".join(str2.split()).lower()
    return sorted(st1) == sorted(st2)


# Define main function
def main():
    string1 = "Listen"
    string2 = "Silent"
    print(are_anagrams(string1, string2))  # Expected output: True
    print(are_anagrams_ignore_case_spaces(string1, string2))  # Expected output: True


if __name__ == "__main__":
    main()