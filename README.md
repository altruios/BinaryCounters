# BinaryCounters
 an Array-based binary counter with functions designed for cellular automata experimentation

# INSTALL INSTRUCTION
```
pip install BinaryCounters
```



# how to use:
## BinaryCounter(\<int\>=val,\<int\>=bitLength)
* #### val is the starting value of the binary,
* #### bitLength is the size of the array holding the binary.

### FUNCTIONS:
* ##### these are the logical gates - AND,NAND,OR,XOR,XNOR,NOR,NOT.
* ##### they are included for convinence - and can be used anywhere an 'arbitray function' can be used (they fit the requirments of having the inputs i,bit1,bit2, and give a 0/1 as the output).
* ##### note: these are not meant for anything other than binary, these are not meant to be called, but to be passed into a method as an argument.

### METHODS

#### KEEP_EVEN(\<bool\>=increaseBool):
* ##### increase bool determines if number increases or decreases
* ##### forces an even number by shifting value by 1
 
#### KEEP_ODD(\<bool\>=increaseBool):
* ##### increase bool determines if number increases or decreases
* ##### forces an even number by shifting value by 1

#### SORT_B(\<bool\>=fromSig):
* ##### fromSig if true, sorts all 1's to the most significant digit
* ##### sorts the binary

#### SECTION(\<int\>=start,\<int\>=stop):
* ##### returns a new array of that section of binary

#### SPAWN(\<int\>=start,\<int\>=stop):
* ##### returns a new \<BinaryCounter\> from that section of binary

#### COUNT(\<bool\>=willCountOnes):
* ##### willCountOnes if true,  this function will return number of 1's, otherwise it will return the number of 0's 

#### SHIFT_UP( \<int\>=amount):
* ##### logically shifts binary \<\< up

#### SHIFT_DOWN( \<int\>=amount):
* ##### logically shifts binary \>\> down

#### SHIFT_CIRCLE( \<int\>=amount, \<bool\>=dir):
* ##### dir determines rotational direction. If True:
* ##### rotates the binary by an amount = 1: (0,0,0,1)=>(1,0,0,0) amount = 2: (0,0,0,1)=>(0,1,0,0)
* ##### If False:
* ##### rotates the binary by an amount = 1: (1,1,0,1)=>(1,0,1,1) amount = 2: (1,1,1,0)=>(1,0,1,1) 

#### BIT_OP( \<BinaryCounter\>=binary, \<str\>=operator):
* ##### operator options are = "XOR","OR","AND","NAND,"XNOR","NOR","NOT"
* ##### binary must be the same length as owner of method.
 
#### INCREASE(\<int\>=amount):
* ##### amount must be a positive integer, or results in no change
* ##### amount will not increase set bits, it will max at all 1's

#### DECREASE(\<int\>=amount):
* ##### amount must be a positive integer, or results in no change
* ##### amount will not wrap around in value, it will end at all 0's
 
#### COUNT(\<bool\>=countOnes):
* ##### if countOnes: count 1's in binary, else count 0's 

#### READ():
* ##### prints a status in the console

#### SIZE():
* ##### returns the length of the binary array

#### GET_MAX():
* ##### returns the maximum int value based on size of array.

#### SET_BIT_LENGTH(\<int\>=len):
* #####  len sets the length of the array holding the bits.

#### B_TO_I(\<int\>[]=bin):
* #####  bin is an array of binary numbers (or any numbers), such as \<BinaryCounter\>.binary
* ##### returns an int

#### VAL():
* ##### returns value of binary

#### BIN():
* ##### returns array that represents binary
  
#### SET_V(\<int\>=value):
* ##### sets value of binary

#### GET_BIN_OF(\<int\>=b):
* ##### b is calculated into an array of zero's and one's that represent it's binary, with a leading significant digit

#### SET_BIT(\<int\>=val,\<int\>=pos)
* ##### val is 1/0,
* ##### pos is goes from least significant digit to most
* ##### pos is 0 based
  
#### W_BIT_OP(\<BinaryCounter\>=binary, \<Function\>=fn):
* ##### WRAPPED BIT OPERATION: the second array is looped over if it is smaller than the method's owner
* ##### binary may be a different length from the owner of this method
* ##### this method iterates though and modifys its binary by running a fn on it, and the the matching index of the binary
* ##### note that this wraps around the binary you supply, so it may be of any length.

#### S_BIT_OP(\<BinaryCounter\>=binary, \<Function\>=fn):
* ##### STATIONARY BIT OPERATION: there is no wrap lke in W_BIT_OP, if the binary you pass in has a smaller bitLength,  S_BIT_OP will operate from smallest significant digit to largest, and return the original binary when it runs of of the binary you pass in. 
* ##### binary may be a different length from the owner of this method
* ##### this method iterates though and modifys its binary by running a fn on it, and the the matching index of the binary
* ##### note that this wraps around the binary you supply, so it may be of any length.



* ###### notes on fn
* * ######   it is a function you supply
* * ######   it must return 0 or 1
* * ######   it's inputs are: (\<int\>=pos, \<int\>=bit1, \<int\>=bit2)
 * * * ######  pos begins at the least significant digit and move to the most significant digit in the array.
 * * * ###### bit1 is the method owner's bit
 * * * ###### bit2 is the comparison bit. derived from pos % the length of the comparison array

 
 ## example usage:
     BC1 = BinaryCounter(0,10)  
     BC2 = BinaryCounter(10,10)
     print(BC1.val()) #[0,0,0,0,0,0,0,0,0,0]  left if most significant digit, right is least
     print(BC2.val()) #[0,0,0,0,0,0,1,0,1,0]
     BC1.increase(1) 
     BC2.increase(386) 
     print(BC1.val()) #[0,0,0,0,0,0,0,0,0,1]
     print(BC2.val()) #[0,1,1,0,0,0,1,1,0,0]
     BC1.BIT_OP(BC2,"OR")
     print(BC1.val()) #[0,1,1,0,0,0,1,1,0,1]
     print(BC2.val()) #[0,1,1,0,0,0,1,1,0,0]
     def randomFn(index,bit,b):#just a random equation that spits out 0,1
          return ((bit+b)*(index*b+1))%2  
     BC3 = BinaryCounter(15,5) #[0,1,1,1,1]
     BC1.R_BIT_OP(BC3,randomFn) 
     print(BC1.val()) #[1,0,0,0,0,0,0,0,1,1]

     #to have a smaller array act on a larger:
     #use W_BIT_OP and pass in the logical function
     #give it the binary (any array of bits)
     BC1.W_BIT_OP(BC3, OR) # OR these arrays together, and since BC3 is smaller, loop over until you cover all elements of BC1    
     #use S_BIT_OP to 
     BC1.S_BIT_OP(BC3, OR) # OR these arrays together, and since BC3 is smaller, so it returns BC1 partially unmodified    





