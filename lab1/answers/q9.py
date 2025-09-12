# Function to find the length of the longest substring without repeating characters
def longest_substring_without_repeating(s):
    # TODO: Implement the function
    max_length = 0
    ind1 = 0
    mem = {}
    for i in range(len(s)):
        max_length = max(max_length, i-ind1+1)
        if s[i] in mem:
            if mem[s[i]] > 0:
                while mem[s[i]] > 0:
                    if s[ind1] == s[i]:
                        mem[s[i]] -= 1
                    ind1 += 1
            mem[s[i]] = 1
        else:
            mem[s[i]] = 1
            
    return max_length



# Define main function
def main():
    input_string = "pwwkew"
    print(longest_substring_without_repeating(input_string))  # Expected output: 3 (substring "abc")


if __name__ == "__main__":
    main()