# BinaryCounters
 an Array-based binary counter with functions designed for cellular automata experimentation

# how to use:

### METHODS

#### BIT_OPERATION( \<BinaryCounter\>=binary, \<str\>=operator):
* ##### operator options are = "XOR","OR","AND","NAND,"XNOR","NOR","NOT"
* ##### binary must be the same length as owner of method.
 
#### increase(\<int\>=amount):
* ##### amount must be a positive integer, or results in no change
* ##### amount will not increase set bits, it will max at all 1's

#### decrease(\<int\>=amount):
* ##### amount must be a positive integer, or results in no change
* ##### amount will not wrap around in value, it will end at all 0's
 
#### read():
* ##### prints a status in the console

#### setbitLen(\<int\>=len):
* #####  len sets the length of the array holding the bits.

#### binToIn(\<int\>[]=bin):
* #####  bin is an array of binary numbers (or any numbers), such as \<BinaryCounter\>.binary
  
#### val():
* ##### returns value of binary

#### getThisBin(\<int\>=b):
* ##### b is calculated into an array of zero's and one's that represent it's binary, with a leading significant digit


  
#### rangeBinaryOperation(\<BinaryCounter\>=binary, \<Function\>=fn):
* binary may be a different length from the owner of this method
* this method iterates though and modifys its binary by running a fn on it, and the the matching index of the binary
* note that this wraps around the binary you supply, so it may be of any length.
* ##### notes on fn
* * #####   it is a function you supply
* * #####   it must return 0 or 1
* * #####   it's inputs are: (\<int\>=pos, \<int\>=bit1, \<int\>=bit2)
 * * * ###### pos begins at the least significant digit and move to the most significant digit in the array.
 * * * ###### bit1 is the method owner's bit
 * * * ###### bit2 is the comparison bit. derived from pos % the length of the comparison array

 
 ## example usage:
     BC1 = BinaryCounter(0,10)  
     BC2 = BinaryCounter(10,10)
     BC1.read()#[0,0,0,0,0,0,0,0,0,0]  left if most significant digit, right is least
     BC2.read()#[0,0,0,0,0,0,1,0,1,0]
     BC1.increase(1) 
     BC2.increase(386) 
     BC1.read()#[0,0,0,0,0,0,0,0,0,1]
     BC2.read()#[0,1,1,0,0,0,1,1,0,0]
     BC1.BIT_OPERATION(BC2,"OR")
     BC1.read()#[0,1,1,0,0,0,1,1,0,1]
     BC2.read()#[0,1,1,0,0,0,1,1,0,0]
     def randomFn(index,bit,b):#just a random equation that spits out 0,1
          return ((bit+b)*(index*b+1))%2  
     BC3 = BinaryCounter(15,5) #[0,1,1,1,1]
     BC1.rangeBinaryOperation(BC3,randomFn) #[1,0,0,0,0,0,0,0,1,1]
