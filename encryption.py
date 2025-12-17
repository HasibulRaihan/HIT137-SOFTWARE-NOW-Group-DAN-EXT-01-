# Group Name: DAN/EXT 01
# Group Members: 4
# Member 1: Md Hasibul Raihan - S397592
# Member 2: Tanisa Sanam Vabna - S397593
# Member 3: JESHIKA SAPKOTA - S399269
# Member 4: LADDA DAWSON - S382273

#Create a program that reads the text file "raw_text.txt", encrypts its contents using a simple encryption method, and writes the encrypted text to a new file "encrypted_text.txt". Then create a function to decrypt the content and a function to verify the decryption was successful.

# ----------------------- MAIN PROGRAM START -----------------------



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
        
         #shift character forward and wrap around using module 26
        return chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
      
      else: #for the lowercase letter in second half of the alphabet (n-z)
         
         shift=-(shift1+shift2)    #shift character backward 

         #shift character backward and wrap around using module 26
         return chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
      
    
   elif 'A'<= ch <='Z':
       
       #for the uppercase letter in first half of the alphabet ie A to M
       if 'A' <= ch <='M':
          shift =-shift1 #shift backward by shift1 position
          return chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        
       else:
          #for the uppercase letter in second half of the alphabet

          shift =shift2**2 # shift forward by shift2² positions 

          #shift forward and warp around using 26
          return chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
       
   else:
      return ch
             
    #check if the character is an uppercase letter
   