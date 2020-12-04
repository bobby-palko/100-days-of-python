from art import logo

# Alphabet list to use for our cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Sweet ASCII art
print(logo)

is_finished = False


def caesar(text, shift, direction):

    # Cut down large shift values to stay in the range of the list
    shift = shift % len(alphabet)

    if direction == "decode":
        shift = -shift

    shifted_text = ""

    for char in text:

        # We're only scrambling letters, so ignore spaces, numbers, symbols.
        if char in alphabet:
            # Set the index of the replacement letter
            replacement_index = alphabet.index(char) + shift

            # Check to see if shifting will cause an index out of range, and wrap accordingly
            if replacement_index >= len(alphabet):
                replacement_index -=len(alphabet)

            # Update the new String with the shifted letter
            shifted_text += alphabet[replacement_index]
            
        else:
            shifted_text += char
        
    print(f"The {direction}d text is {shifted_text}.")

# Loop the program until we're done
while not is_finished:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    still_use = input("Would you like to continue? Y/N: ").lower()
    if still_use == "n":
        is_finished = True

print("Goodbye!")
