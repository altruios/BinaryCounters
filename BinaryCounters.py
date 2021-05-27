import math
import random

#python module for array based binary counters: 
#work in progress
class BC:
     def __init__(self, startNum,padd):
          self.binary = []
          self.rawNumber = startNum
          self.padd = padd
          self.maximum = math.pow(2,self.padd)-1
          self._conform()
     def _conform(self):
          self.binary = self._paddedBinary(self.rawNumber)
          self.raw = self._conformRaw()
     def _conformRaw(self):
          newRaw = self.B_TO_I(self.binary)
          if(newRaw>self.maximum):
               newRaw=self.maximum
               self.binary=self._paddedBinary(newRaw)
          self.rawNumber=newRaw
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
     def _xorF(self,i1,i2):
          return i1^i2
     def _orf(self, i1,i2):
          return i1|i2
     def _andf(self,i1,i2):
          return i1&i2
     def _nandf(self,i1,i2):
          if(i1 and i1): return 0
          else:          return 1
     def _xnorf(self,i1,i2):
          return not i1==i2
     def _norf(self,i1,i2):
          if(not i1 and not i2):   return 1
          else:                    return 0
     def _notf(self,i1,i2):
          if(i2>0): return 0
          else:     return i1
     def _checkLength(self,otherBin):
          if(self._length()!=len(otherBin)):
               raise Exception("bit's not equal");       
     def _operateOnList(self,otherBinaryCounter, fn):
          OperatedList=[] 
          for i,bit in enumerate(otherBinaryCounter):
               OperatedList.append(fn(self.binary[i],bit))
          return OperatedList
     def _XOR(self, otherBinaryCounter):
          return self._operateOnList(otherBinaryCounter,self._xorF)
     def _AND(self,otherBinaryCounter):
          return self._operateOnList(otherBinaryCounter,self._andf)
     def _OR(self,otherBinaryCounter):
          return self._operateOnList(otherBinaryCounter,self._orf)
     def _NOT(self,otherBinaryCounter):
          return self._operateOnList(otherBinaryCounter,self._notf)
     def _NAND(self,otherBinaryCounter):
          return self._operateOnList(otherBinaryCounter,self._nandf)
     def _XNOR(self,otherBinaryCounter):
          return self._operateOnList(otherBinaryCounter,self._xnorf)
     def _NOR(self,otherBinaryCounter):
          return self._operateOnList(otherBinaryCounter,self._norf)
     def BIT_OP(self, OBC,functionName):
          self._checkLength(OBC.binary)
          if(functionName=="OR"):       self.binary=self._OR(OBC.binary)
          elif(functionName=="XOR"):    self.binary=self._XOR(OBC.binary)
          elif(functionName=="AND"):    self.binary=self._AND(OBC.binary)
          elif(functionName=="NOT"):    self.binary=self._NOT(OBC.binary)
          elif(functionName=="NAND"):   self.binary=self._NAND(OBC.binary)
          elif(functionName=="XNOR"):   self.binary=self._NOT(OBC.binary)
          elif(functionName=="NOR"):    self.binary=self._NOR(OBC.binary)
          else:                         raise Exception("unknown operation, known operations are OR,XOR,AND,NOT,NAND,XNOR,NOR")
          self._conformRaw()
     def R_BIT_OP(self,otherBinaryCounter, arbitrayFunction):
          x=[]
          l=len(otherBinaryCounter.binary)
          for index,bit in enumerate(self.binary):
               pos = l-index-1
               value = arbitrayFunction(pos,bit,otherBinaryCounter.binary[pos%l])
               x.append(value)
          if(len(x)!=len(self.binary)):
               raise Exception("what the what?");
          self.binary = x
          self._conformRaw()
     def READ(self):
          print(f'binary:{self.binary} value:{self.rawNumber}',end="\n")
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
               result = result + (bit*math.pow(2,l-index-1))
          return result
     def SET_BIT_LENGTH(self,pad):
          self.padd= pad
     def VAL(self):
          return self.rawNumber
     def GET_BIN_OF(self,rn):
          if rn==0: return [0]
          digits = []
          while rn:
               digits.append(int(rn%2))
               rn//=2
          return digits[::-1]
     def SET_BIT(self,bitVal,pos):
          try:
               l=self._length()
               index = l-pos-1
               if(index<0 or index>l):
                    raise Exception("out of bounds")     
               self.binary[index]=bitVal
          except Exception as e:
               print("excepted", e)

if(__name__ == "__main__"):
     #tests
     BC1 = BC(0,10)
     BC2 = BC(10,10)
     BC3 = BC(15,5)
     BC1.READ()
     BC2.READ()
     BC3.READ()
     BC1.INCREASE(1)
     BC2.INCREASE(386)
     BC1.READ()
     BC2.READ()
     BC1.BIT_OP(BC2,"OR")
     print("OR")
     BC1.READ()
     BC2.READ()
     def RFN(I,B1,B2):
          #honestly. just a random eqaution that spits out 0,1
          return ((I*B1+1)*(I*B2+1))%2
     BC1.R_BIT_OP(BC3,RFN)

     print("range function")
     BC1.READ()
     BC1.SET_BIT(1,9)     
     BC1.READ()