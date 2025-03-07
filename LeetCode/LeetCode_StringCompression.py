def compress(chars):
        write = 0  # Position to write in the chars array
        read = 0   # Position to read in the chars array
        
        while read < len(chars):
            char = chars[read]
            count = 0

            # Count consecutive occurrences of the current character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write the character
            print(chars)
            chars[write] = char
            write += 1
            print(chars)
            # Write the count if it's more than 1
            if count > 1:
                for digit in str(count):  # Convert count to string and store each digit
                    chars[write] = digit
                    print(chars)
                    write += 1

        return write  # New length of the array

compress(["a","a","b","b","c","c","c"])