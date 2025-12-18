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
       
    # all the other characters remains unchanged
   else:
      return ch
             
def decrypt_letter(ch, shift1, shift2):
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
   #lowercase letters
   if 'a' <=ch <='z':
      
      #for the lowercase letter in first half of the alphabet ie a to m
      if 'a' <= ch <='m':
         #reverse forward shift
         shift = -(shift1 * shift2)
      else:
         #reverse backward shift
         shift = (shift1 + shift2)
         return chr((ord(ch) - 97 + shift) % 26 + 97)
      
   elif 'A'<= ch <='Z':
      if 'A' <= ch <= 'M': 
              # reverse backward shift
            shift = shift1
      else:         
            # reverse forward shift
            shift = -(shift2 * shift2)
      return chr((ord(ch) - 65 + shift) % 26 + 65)
 
'''
EXAMPLE FOR THIS SCENARIO
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
Moving 'c' forward by 6 letters give us 'i'.

 now we have i as our encrypted letter
 to decrypt this we have rules to follow.
 Since, i is lowercase and in first half of the alphabet, the decryption rule tells us to shift backward by shift1*shift2 ie 6.

 Moving 'i' backward by 6 letters give us 'c'.
This demonstrates the core idea of our process.
 
Encryption moves letters according to the rules, and decryption reverses that exact movement to recover the original text.
'''
 
 #---Encrypt file--
 