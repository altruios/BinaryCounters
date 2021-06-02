#import numpy as np //to be implemented to speed increase :)
#python module for array based binary counters: 
#work in progress
import random
def XOR(i,i1,i2):   return i1^i2
def OR(i, i1,i2):   return i1|i2
def AND(i,i1,i2):   return i1&i2
def XNOR(i,i1,i2):  
     if not i1==i2: return 1
     else: return 0
def NAND(i,i1,i2):
     if(i1 and i1): return 0
     else:          return 1
def NOR(i,i1,i2):
     if(not i1 and not i2):   return 1
     else:                    return 0
def NOT(i,i1,i2):
     if(i2>0): return 0
     else:     return i1
class BC:
     def __init__(self, startNum,padd):
          safeStart =0
          safePadd=1
          if(isinstance(startNum,str)):
               startNum=0
          if(isinstance(padd, str)):
               padd=1
          if((not isinstance(startNum,int))): 
               if(isinstance(startNum,float)):    
                    try:      safeStart=int(startNum)
                    except:   safeStart=0
               else:          safeStart=0
          else:               safeStart=startNum
          if(not isinstance(padd,int)):
               if(isinstance(padd,float)):       
                    try:      safePadd=int(padd) 
                    except:   safePadd=1
               else:          safePadd=padd
          if(safeStart<0):    self.rawNumber=0
          else:               self.rawNumber=safeStart
          if(safePadd<1):     self.padd=1
          else:               self.padd=safePadd
          self.binary = []
          self.rawNumber = int(startNum)
          self.padd = int(padd)
          self.maximum = ((2**self.padd)-1)
          self._conform()
     def _conform(self):
          self.binary = self._paddedBinary(self.rawNumber)
          self.raw = self._conformRaw()
     def _conformRaw(self):
          newRaw = self.B_TO_I(self.binary)
          if(newRaw>self.maximum):
               newRaw=self.maximum
               self.binary=self._paddedBinary(newRaw)
          self.rawNumber=int(newRaw)
          return newRaw 
     def _isBinOverflow(self,digits):
          test =True;
          for bit in digits:
               if(bit == 0): test = False
          return test;
     def _paddedBinary(self,rn):
          digits = self.GET_BIN_OF(rn)
          if(len(digits)> self.padd):
               while(len(digits)>0):
                    digits.pop()
               while(len(digits)<=self.padd):
                    digits.append(1)   
          if(len(digits)==self.padd):
               if(self.B_TO_I(digits)>=self.maximum):
                    while(len(digits)>0):
                         digits.pop()
                    while(len(digits)<self.padd):
                         digits.append(1)

          while(len(digits)<self.padd):
               digits.insert(0,0)
          return digits
     def _length(self): 
          return len(self.binary)
     def _checkLength(self,otherBin):
          if(self._length()!=len(otherBin)):
               raise Exception("bit's not equal");   

    
     def _operateOnList(self,otherBinaryCounter, fn):
          OperatedList=[] 
          for i,bit in enumerate(otherBinaryCounter):
               OperatedList.append(fn(i,self.binary[i],bit))
          return OperatedList
     def XOR(self, otherBinaryCounter):
          return self._operateOnList(otherBinaryCounter.binary,XOR)
     def AND(self,otherBinaryCounter):
          return self._operateOnList(otherBinaryCounter.binary,AND)
     def OR(self,otherBinaryCounter):
          return self._operateOnList(otherBinaryCounter.binary,OR)
     def NOT(self,otherBinaryCounter):
          return self._operateOnList(otherBinaryCounter.binary,NOT)
     def NAND(self,otherBinaryCounter):
          return self._operateOnList(otherBinaryCounter.binary,NAND)
     def XNOR(self,otherBinaryCounter):
          return self._operateOnList(otherBinaryCounter.binary,XNOR)
     def NOR(self,otherBinaryCounter):
          return self._operateOnList(otherBinaryCounter.binary,NOR)
     def BIT_OP(self, OBC,functionName):
          self._checkLength(OBC.binary)
          if(functionName=="OR"):       self.binary=self.OR(OBC)
          elif(functionName=="XOR"):    self.binary=self.XOR(OBC)
          elif(functionName=="AND"):    self.binary=self.AND(OBC)
          elif(functionName=="NOT"):    self.binary=self.NOT(OBC)
          elif(functionName=="NAND"):   self.binary=self.NAND(OBC)
          elif(functionName=="XNOR"):   self.binary=self.XNOR(OBC)
          elif(functionName=="NOR"):    self.binary=self.NOR(OBC)
          else:                         raise Exception("unknown operation, known operations are OR,XOR,AND,NOT,NAND,XNOR,NOR")
          self._conformRaw()
     def W_BIT_OP(self,otherBinaryCounter, arbitrayFunction):
          x=[]
          l=len(otherBinaryCounter.binary)
          sl = self._length()-1
          for index,bit in enumerate(self.binary):
               pos = l-index-1
               pos2= sl-index;
               wrappedPos = pos%l
               i1 = self.binary[pos2]
               i2 = otherBinaryCounter.binary[wrappedPos]
               value = arbitrayFunction(pos,i1,i2)
               x.append(value)
          if(len(x)!=len(self.binary)):
               raise Exception("what the what?");
          x.reverse()
          self.binary = x
          self._conformRaw()
     def S_BIT_OP(self,otherBinaryCounter, arbitrayFunction):
          x=[]
          l=len(otherBinaryCounter.binary)
          sl = self._length()-1
          for index,bit in enumerate(self.binary):
               pos = l-index-1
               pos2 = sl-index
               if(pos>=0):
                    i2 = otherBinaryCounter.binary[pos]
                    i1 = self.binary[pos2]
                    value = arbitrayFunction(pos,i1,i2)
                    x.append(value)
               else: #copy the original array

                    value = self.binary[pos2]
                    x.append(value)
          if(len(x)!=len(self.binary)):
               raise Exception("what the what?");
          x.reverse()
          self.binary = x
          self._conformRaw()
     def READ(self):
          return (f'binary:{self.binary} value:{self.rawNumber}\n')
     def INCREASE(self,amount):
          self.rawNumber= min(self.rawNumber+amount,self.maximum)
          self._conform()
     def DECREASE(self,amount):
          self.rawNumber=max(0,self.rawNumber-amount) 
          self._conform()
     def B_TO_I(self,bin):
          result = 0;
          l = len(bin);
          for index,bit in enumerate(bin):
               position = l-index-1
               tarBit = bin[position]
               result = result + (tarBit*(2**index))
          return result
     def SET_BIT_LENGTH(self,pad):
          self.padd= pad
          self._conform()
     def VAL(self):
          return self.rawNumber
     def GET_BIN_OF(self,rn):
          if rn==0: return [0]
          digits = []
          while rn:
               digits.append(int(rn%2))
               rn//=2
          return digits[::-1]
     def BIN(self):
          return self.binary
     def SET_BIT(self,bitVal,pos):
          try:
               l=self._length()
               index = l-pos-1
               if(index<0 or index>l):
                    raise Exception("out of bounds")     
               self.binary[index]=bitVal
               self._conformRaw()
          except Exception as e:
               print("excepted", e)
               print("did not set anything")

     def SET_V(self,val):
          self.rawNumber=max(min(self.maximum,val),0);
          self._conform()
     def SHIFT_UP(self,val):
          last = self.rawNumber
          if(isinstance(val,int)):
               if(val>0):
                    try: self.rawNumber=self.rawNumber<<val
                    except: self.rawNumber=last
               else:
                    print(val)
                    raise Exception("negative input not allowed")
          else:
               raise Exception("bad input: use integers")
          if(self.rawNumber<0):
               self.rawNumber=0
          if(self.rawNumber>self.GET_MAX()):
               self.rawNumber=self.GET_MAX()
          self._conform()
     def SHIFT_DOWN(self,val):
          last = self.rawNumber
          if(isinstance(val,int)):
               if(val>0):
                    try: self.rawNumber=self.rawNumber>>val
                    except: self.rawNumber=last
               else:
                    raise Exception("negative input not allowed")
          else:
               raise Exception("bad input: use integers")
          if(self.rawNumber<0):
               self.rawNumber=0
          if(self.rawNumber>self.GET_MAX()):
               self.rawNumber=self.GET_MAX()
          self._conform()
     def SHIFT_CIRCLE(self,amount,bGoForward):
          if(bGoForward):
               for i in range(amount):
                    bit = self.binary.pop()
                    self.binary.insert(0,bit)
          else:
               for i in range(amount):
                    bit = self.binary.pop(0)
                    self.binary.append(bit)
          self._conformRaw()
     def COUNT(self, willCountOnes):
          c=0
          if(willCountOnes):  c = self.binary.count(1)
          else:               c = self.binary.count(0)
          return c
     def KEEP_ODD(self,increaseBool):
          if(self.binary[len(self.binary)-1]!=1):
               if(increaseBool):   self.INCREASE(1)
               else:               self.DECREASE(1)
     def KEEP_EVEN(self,increaseBool):
          if(self.binary[len(self.binary)-1]!=0):
               if(increaseBool):   self.INCREASE(1)
               else:               self.DECREASE(1)
     def SORT_B(self,bFromSignificantDigit):
          if(bFromSignificantDigit):
               self.binary.sort(reverse=True)
          else:
               self.binary.sort()
          self._conformRaw()
     def SECTION(self,start,stop):
          return self.binary[start:stop]
     def SPAWN(self,start,stop):
          section = self.SECTION(start,stop);
          sB = self.B_TO_I(section);
          l=len(section)
          return BC(sB,l)
     def GET_MAX(self):
          return self.maximum
if(__name__ == "__main__"):
     #tests
     class TestBinaryCounter:
          def test_1_overflow(self):
               for i in range(1_000):
                    bin=BC(i,i)
                    bin.SET_V(bin.GET_MAX())
                    a=bin.VAL()
                    bin.INCREASE(1)
                    assert a==bin.VAL()
          def test_2_overflow_infinity(self):
               for i in range(1_000):
                    bin=BC(i,i)
                    bin.SET_V(bin.GET_MAX())
                    a=bin.VAL()
                    bin.INCREASE(float('inf'))
                    assert a==bin.VAL()
          def test_3_overflow_negative(self):
               for i in range(1_000):
                    bin = BC(0,i)
                    bin.DECREASE(i)
                    assert bin.VAL()==0
          def test_4_overflow_negative_infinity(self):
               for i in range(1_000):
                    bin = BC(0,i)
                    bin.DECREASE(float('inf'))
                    assert bin.VAL()==0
          def test_5_bad_input_text(self):
               stringNumbers = ["1","2","3","4","5","6","7","8","9","10","-1","-20","-0.311111","-.343,fa","hello world","three","THREE","0",""]
               for i in range(1_000):
                    bin=BC(stringNumbers[(i%len(stringNumbers))],i)
                    assert bin.VAL()==0;
          def test_6_method_COUNT(self):
               bin1=BC(15,6)
               bin2=BC(15,12)
               bin3=BC(31,8)
               bin4=BC(63,16)
               assert bin1.COUNT(True)==4
               assert bin1.COUNT(False)==2
               assert bin2.COUNT(True)==4
               assert bin2.COUNT(False)==8
               assert bin3.COUNT(True)==5
               assert bin3.COUNT(False)==3
               assert bin4.COUNT(True)==6
               assert bin4.COUNT(False)==10
          def test_7_method_VAL(self):
               for i in range(1_000):
                    x = int(round(random.random()*1000))
                    bin = BC(x*i,i+10);
                    assert bin.VAL() == (x*i)


     t = TestBinaryCounter()
     print("testing");
     t.test_1_overflow()
     t.test_2_overflow_infinity()
     t.test_3_overflow_negative()
     t.test_4_overflow_negative_infinity()
     t.test_5_bad_input_text()
     t.test_6_method_COUNT()
     t.test_7_method_VAL()
     print("tested:YAY!")