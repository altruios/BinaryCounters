import math
import random

#python module for array based binary counters: 
#work in progress
class BinaryCounter:
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
          newRaw = self.binToInt(self.binary)
          if(newRaw>self.maximum):
               newRaw=self.maximum
               self.binary=self._paddedBinary(newRaw)
          self.rawNumber=newRaw
          return newRaw 
     def _isBinOverflow(self,digits):
          test =True;
          for bit in digits:
               if(bit == 0):
                    test = False
          if(test==True):
               print(f"bin overflow!")
          return test;
     def _paddedBinary(self,rn):
          digits = self.getBin(rn)
          if(len(digits)> self.padd):
               print("overflow")
               while(len(digits)>0):
                    digits.pop()
               while(len(digits)<=self.padd):
                    digits.append(1)   
          if(len(digits)==self.padd):
               if(self.binToInt(digits)>=self.maximum):
                    print("overflow x")
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
          if(i2>0):
               return 0
          return i1
     def _checkLength(self,otherBin):
          if(self._length()!=len(otherBin)):
               print("bit lengths must be equal")
               raise Exception("bit's not equal");       
     def _operateOnList(self,otherBinaryCounter, fn):
          OperatedList=[] 
          for i,bit in enumerate(otherBinaryCounter):
               OperatedList.append(fn(self.binary[i],bit))
          return OperatedList
     def _XOR(self, otherBinaryCounter):
          self._checkLength(otherBinaryCounter)
          return self._operateOnList(otherBinaryCounter,self._xorF)
     def _AND(self,otherBinaryCounter):
          self._checkLength(otherBinaryCounter)
          return self._operateOnList(otherBinaryCounter,self._andf)
     def _OR(self,otherBinaryCounter):
          self._checkLength(otherBinaryCounter)
          return self._operateOnList(otherBinaryCounter,self._orf)
     def _NOT(self,otherBinaryCounter):
          self._checkLength(otherBinaryCounter)
          return self._operateOnList(otherBinaryCounter,self._notf)
     def _NAND(self,otherBinaryCounter):
          self._checkLength(otherBinaryCounter)
          return self._operateOnList(otherBinaryCounter,self._nandf)
     def _XNOR(self,otherBinaryCounter):
          self._checkLength(otherBinaryCounter)
          return self._operateOnList(otherBinaryCounter,self._xnorf)
     def _NOR(self,otherBinaryCounter):
          self._checkLength(otherBinaryCounter)
          return self._operateOnList(otherBinaryCounter,self._norf)
     def BIT_OPERATION(self, OBC,functionName):
          if(functionName=="OR"):
               self.binary=self._OR(OBC.binary)
               self._conformRaw()
          elif(functionName=="XOR"):
               self.binary=self._XOR(OBC.binary)
               self._conformRaw()
          elif(functionName=="AND"):
               self.binary=self._AND(OBC.binary)
               self._conformRaw()
          elif(functionName=="NOT"):
               self.binary=self._NOT(OBC.binary)
               self._conformRaw()
          elif(functionName=="NAND"):
               self.binary=self._NAND(OBC.binary)
               self._conformRaw()
          elif(functionName=="XNOR"):
               self.binary=self._NOT(OBC.binary)
               self._conformRaw()
          elif(functionName=="NOR"):
               self.binary=self._NOR(OBC.binary)
               self._conformRaw()
          else:
               raise Exception("unknown operation, known operations are OR,XOR,AND,NOT,NAND,XNOR,NOR")
     def rangeBinaryOperation(self,otherBinaryCounter, arbitrayFunction):
          #other binCounter may be of different length;
          #arbitrayfunction MUST return 0,1, and assume zero or 1 inputs
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
     def read(self):
          print(f'binary:{self.binary} value:{self.rawNumber}',end="\n")
     def increase(self,amount):
          self.rawNumber= min(self.rawNumber+amount,self.maximum)
          self._conform()
     def decrease(self,amount):
          self.rawNumber=max(0,self.rawNumber-amount) 
          self._conform()
     def binToInt(self,bin):
          result = 0;
          l = len(bin);
          for index,bit in enumerate(bin):
               result = result + (bit*math.pow(2,l-index-1))
          return result
     def setbitLen(self,pad):
          self.padd= pad
     def val(self):
          return self.rawNumber
     def getBin(self,rn):
          if rn==0:
               return [0]
          digits = []
          while rn:
               digits.append(int(rn%2))
               rn//=2
          return digits[::-1]

if(__name__ == "__main__"):
     #tests
     BC1 = BinaryCounter(0,10)
     BC2 = BinaryCounter(10,10)
     BC3 = BinaryCounter(15,5)
     BC1.read()
     BC2.read()
     BC3.read()
     BC1.increase(1)
     BC2.increase(386)
     BC1.read()
     BC2.read()
     BC1.BIT_OPERATION(BC2,"OR")
     print("or")
     BC1.read()
     BC2.read()
     def randomFn(index,bit,b):
          #honestly. just a random eqaution that spits out 0,1
          newValue = ((bit+b)*(index*b+1))%2
          return newValue
     BC1.rangeBinaryOperation(BC3,randomFn)
     print("range function")
     BC1.read()