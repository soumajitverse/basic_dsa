def compress(chars):
    n = len(chars)
    idx = 0
    i = 0

    while i < n:
        ch = chars[i]
        count = 0

        # count repeating characters
        while i < n and chars[i] == ch:
            count += 1
            i += 1

        chars[idx] = ch
        idx += 1

        if count > 1:
            for digit in str(count):
                chars[idx] = digit
                idx += 1

    return idx


# taking input
chars = input("Enter characters separated by space: ").split()

length = compress(chars)

print("Compressed Length:", length)
print("Compressed Array:", chars[:length])