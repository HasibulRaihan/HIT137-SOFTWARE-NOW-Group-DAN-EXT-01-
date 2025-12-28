# Group Name: DAN/EXT 01
# Group Members: 4
# Member 1: Md Hasibul Raihan - S397592
# Member 2: Tanisa Sanam Vabna - S397593
# Member 3: JESHIKA SAPKOTA - S399269
# Member 4: LADDA DAWSON - S382273

#Create a program that reads the text file "raw_text.txt", encrypts its contents using a simple encryption method, and writes the encrypted text to a new file "encrypted_text.txt". Then create a function to decrypt the content and a function to verify the decryption was successful.

"""Requirements
The encryption should take two user inputs (shift1, shift2), and follow these rules:
• For lowercase letters:
o If the letter is in the first half of the alphabet (a-m): shift forward by shift1 *
shift2 positions
o If the letter is in the second half (n-z): shift backward by shift1 + shift2
positions
• For uppercase letters:
o If the letter is in the first half (A-M): shift backward by shift1 positions
o If the letter is in the second half (N-Z): shift forward by shift2² positions
(shift2 squared)
• Other characters:
o Spaces, tabs, newlines, special characters, and numbers remain
unchanged
"""

# ----------------------- MAIN PROGRAM START -----------------------


'''In the code, marker are used. ^ for lowercase a-m, ~ for n-z, # for A-M and @ for N-Z
The marker is used to remember which encryption rule was applied to each character. During decryption, it tells the program the correct inverse operation to recover the original letter.
'''
def encrypt_letter(ch, shift1, shift2):
   
   """encryption function with three parameters.
   ch -> character to encrypt
   shift1 (int)->first shift value entered by user
   shift2 (int)->second shift value entered by user
   """

    #condition for the lowercase letters
   if 'a'<= ch <='z':
      
      #for the lowercase letter in first half of the alphabet ie a to m
      if 'a'<= ch <='m':
        #shift character forward 
        shift=shift1*shift2 
        
         #shift character forward and wrap around using module 26 and using marker ^
        return '^'+ chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
      
      else: #for the lowercase letter in second half of the alphabet (n-z)
         
         shift=-(shift1+shift2)    #shift character backward 

         #shift character backward and wrap around using module 26 and marker ~
         return '~' + chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
      
    
   elif 'A'<= ch <='Z':
       
       #for the uppercase letter in first half of the alphabet ie A to M
       if 'A' <= ch <='M':
          shift =-shift1 #shift backward by shift1 position
         
          #shift character backward and wrap around using module 26 and marker #
          return '#' + chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        
       else:
          #for the uppercase letter in second half of the alphabet

          shift =shift2**2 # shift forward by shift2² positions 

          #shift forward and warp around using 26 and using marker @
          return '@' + chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
       
    # all the other characters remains unchanged
   else:
      return ch
   
             
def decrypt_letter(marker, ch, shift1, shift2):
   
   """decryption function with three parameters.
   ch -> character to encrypt
   shift1 (int)->first shift value entered by user
   shift2 (int)->second shift value entered by user

   The decryption reverses the encryption rules.
   Lowercase a-m: backward by shift1*shift2 
   Lowercase n-z: forward by shift1+shift2
   Uppercase A-M: forward by shift1
   Uppercase N-Z: backward by shift2**2
   """

   if marker == '^':  # marker used for lowercase a–m
        shift = -(shift1 * shift2)
        return chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
   elif marker == '~':  # marker used for lowercase n–z
        shift = shift1 + shift2
        return chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
   
   elif marker == '#':  # marker used for uppercase A–M
        shift = shift1
        return chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
   
   elif marker == '@':  # marker used for uppercase N–Z
        shift = -(shift2 ** 2)
        return chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
   
   else:
        return ch

'''
EXAMPLE FOR SHIFT SCENARIO WITH MARKERS
 Suppose we have:
 shift 1=2
 shift 2 = 3

 We calculate : 
 shift1*shift2=6
 shift1+shift2=5
 shift 2^2=3^2=9

 Let's consider the letter 'c'
 then through encyption rules, c is in lowercase and belongs to the first half of the alphabet ie a to m.

 According to the encryption rule, c will be forwarded by shift1*shift2 ie 6.
Moving 'c' forward by 6 letters give us 'i' and marker ^ added
   - Result stored in file: '^i'

Decryption:
   - Marker '^' tells us it's lowercase a-m
   - Reverse shift: backward by 6
   - Original letter recovered: 'c'

Letter: 'B' (uppercase, first half A-M)
   - Encryption rule: backward by shift1 = 2
   - Encrypted letter: 'Z'
   - Marker added: '#'
   - Result stored: '#Z'

   Decryption:
   - Marker '#' tells us it's uppercase A-M
   - Reverse shift: forward by 2
   - Original letter recovered: 'B'
'''
 
 #---Encrypt file--
 
def encrypt_file(shift1, shift2):
    
    #Opens the file raw_text.txt in read mode.Reads the entire content of the file as a single string and stores the original (unencrypted) text in the variable raw.
    with open("raw_text.txt", "r") as f:
        raw = f.read()

    #initialized an empty string where the encrypted text will be stored
    encrypted = ""

    #Loops through each character in the original text
    for ch in raw:
        
        #Sends each character to the encrypt_letter() function. The returned encrypted character is added to the encrypted string.
        encrypted += encrypt_letter(ch, shift1, shift2)

#    # Write the encrypted text into a new file ie encrypted_text.txt
    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted)


 #---Decrypt file--

def decrypt_file(shift1, shift2):

    # Open the encrypted text file in read mode
    with open("encrypted_text.txt", "r") as f:
        enc = f.read()

    # Initialize an empty string to store the decrypted output
    decrypted = ""

    # Initialize index variable to iterate through the encrypted string
    i = 0

    # Loop through the encrypted text character by character
    while i < len(enc):

        # Get the current character from the encrypted text
        ch = enc[i]

        # Check if the character is a marker indicating an encryption rule
        if ch in ['^', '~', '#', '@']:

            # Store the marker to identify which encryption rule was used
            marker = ch

            # Get the actual encrypted character that follows the marker
            real_char = enc[i + 1]

            # Decrypt the character using the marker and shift values
            decrypted += decrypt_letter(marker, real_char, shift1, shift2)

              # Move the index forward by 2 (marker + character)
            i += 2
        else:
            # If the character is not a marker, add it directly to decrypted text
            decrypted += ch

            # Move to the next character
            i += 1

    with open("decrypted_text.txt", "w") as f:
        f.write(decrypted)


# VERIFY DECRYPTION
def verify():
    
    # Read the original text from the raw input file
    with open("raw_text.txt", "r") as f:
        original = f.read()

   # Read the decrypted text from the decrypted output file
    with open("decrypted_text.txt", "r") as f:
        decrypted = f.read()

    # Compare the original text with the decrypted text
    if original == decrypted:
        print("\n✔ Decryption successful!")
    else:
        print("\n✘ Decryption failed.")

#--------main function-----------
def main():
   # Ask the user to enter the first shift value
    shift1 = int(input("Enter shift1: "))

    # Ask the user to enter the first shift value
    shift2 = int(input("Enter shift2: "))

   # Inform the user that encryption has started
    print("Encrypting...")
    encrypt_file(shift1, shift2)

    print("Decrypting...")
    decrypt_file(shift1, shift2)

#here the verification is done whether decryption is success or is failed.
    print("Verifying...")
    verify()

main()
