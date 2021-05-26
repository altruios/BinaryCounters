import math
import random

#python module for array based binary counters: 
#work in progress
class BinaryCounter:
     def __init__(self, startNum,padd):
          self.binary = []
          self.rawNumber = startNum
          self.padd = padd
          self.conform()
          self.max = math.pow(2,self.padd)-1
          print("self max",self.max)
          print("\n\n\n\n")
     def conform(self):
          self.binary = self.paddedBinary(self.rawNumber)
          self.conformRaw()
     def checkBinIsOverflow(self,digits):
          test =True;
          for bit in digits:
               if(bit == 0):
                    test = False
          if(test==True):
               print(f"\n\n\nb{digits}, {self.rawNumber}\n\n")
          return test;
     def paddedBinary(self,rn):
          digits = self.getBin(rn)
          if(len(digits)> self.padd):
               print("overflow")
               while(len(digits)>0):
                    digits.pop()
               while(len(digits)<=self.padd):
                    digits.append(1)   
          if(len(digits)==self.padd):
               if(self.readBin(digits)>=self.max):
                    print("overflow x")
                    while(len(digits)>0):
                         digits.pop()
                    while(len(digits)<self.padd):
                         digits.append(1)

          while(len(digits)<self.padd):
               digits.insert(0,0)
          return digits
     def readBin(self,bin):
          result = 0;
          l = len(bin);
          for index,bit in enumerate(bin):
               result = result + (bit*math.pow(2,l-index))
          return result
     def length(self):
          return len(self.binary)
     def getBin(self,rn):
          if rn==0:
               return []
          digits = []
          while rn:
               digits.append(int(rn%2))
               rn//=2
          return digits[::-1]
     def increase(self,amount):
          self.rawNumber= max(self.rawNumber+amount,self.max)
          self.conform()
     def decrease(self,amount):
          self.rawNumber=max(0,self.rawNumber-amount) 
          self.conform()
     def val(self):
          return self.rawNumber
     def binary(self):
          return self.binary
     def setPad(self,pad):
          self.padd= pad
     def read(self):
          print(f'binary:{self.binary} value:{self.rawNumber} bitLength: {self.padd} ',end="\n")
     def conformRaw(self):
          newRaw = 0
          for index,bit in enumerate(self.binary):
               newRaw = newRaw + round(math.pow(2,self.padd-index) * bit)
          print(f"new raw:{newRaw}, old raw:{self.rawNumber}", end="\n")
          self.rawNumber=newRaw
     def BIT_OPERATION(self, OBC,functionName):
          if(functionName=="OR"):
               self.binary=self.OR(OBC.binary)
               self.conformRaw()
          elif(functionName=="XOR"):
               self.binary=self.XOR(OBC.binary)
               self.conformRaw()
          elif(functionName=="AND"):
               self.binary=self.AND(OBC.binary)
               self.conformRaw()
          elif(functionName=="NOT"):
               self.binary=self.NOT(OBC.binary)
               self.conformRaw()
          else:
               raise Exception("unknown operation, known operations are OR,XOR,AND,NOT")
     def _xorF(self,i1,i2):
          return i1^i2
     def _orf(self, i1,i2):
          return i1|i2
     def _andf(self,i1,i2):
          return i1&i2
     def _notf(self,i1,i2):
          if(i2>0):
               return 0
          return i1
     def checkLength(self,otherBin):
          if(self.length()!=len(otherBin)):
               print("bit lengths must be equal")
               raise Exception("bit's not equal");       
     def _operateOnList(self,otherBinaryCounter, fn):
          OperatedList=[] 
          print(f"{otherBinaryCounter}debug")
          print("operating on lists: bin, other bin:  ",self.binary,otherBinaryCounter)
          for i,bit in enumerate(otherBinaryCounter):
               OperatedList.append(fn(self.binary[i],bit))
          print(f"returning {fn}'ed {OperatedList} opedList")
          return OperatedList
     def XOR(self, otherBinaryCounter):
          self.checkLength(otherBinaryCounter)
          return self._operateOnList(otherBinaryCounter,self._xorF)
     def AND(self,otherBinaryCounter):
          self.checkLength(otherBinaryCounter)
          return self._operateOnList(otherBinaryCounter,self._andf)
     def OR(self,otherBinaryCounter):
          self.checkLength(otherBinaryCounter)
          return self._operateOnList(otherBinaryCounter,self._orf)
     def NOT(self,otherBinaryCounter):
          self.checkLength(otherBinaryCounter)
          return self._operateOnList(otherBinaryCounter,self._notf)
     def rangeBinaryOperation(self,otherBinaryCounter, arbitrayFunction):
          #other binCounter may be of different length;
          #arbitrayfunction MUST return 0,1, and assume zero or 1 inputs
          x=[]
          for index,bit in enumerate(self.binary):
               value=0
               for i,b in enumerate(otherBinaryCounter.binary):
                    value = arbitrayFunction(index,i,bit,b, value)
               x.append(value)
          if(len(x)!=len(self.binary)):
               raise Exception("what the what?");
          self.binary = x
          self.conformRaw()
if(__name__ == "__main__"):
     #tests
     BC1 = BinaryCounter(0,10)
     BC2 = BinaryCounter(10,10)
     BC3 = BinaryCounter(0,6)
     renderCountTest = 200
     def PickRandomFunction(bc1,bc2):
          r1=random.random()
          r2=random.random()
          if(r1>0.5):
               if(r2>0.5):
                    bc1.BIT_OPERATION(bc2,"OR")
                    print("bc1 OR bc2")
               else:
                    bc1.BIT_OPERATION(bc2,"XOR")
                    print("bc1 XOR bc2")

          else:
               if(r2>0.5):
                    bc2.BIT_OPERATION(bc1,"AND")
                    print("bc2 AND bc1")

               else:
                    bc2.BIT_OPERATION(bc1,"NOT")
                    print("bc2 NOT bc1")
     def fuzzyZor(index,i,bit,b,lastValue):
          value = lastValue;
          newValue = ((bit+i)*(index*b+1))%2
          return newValue

     for i in range(renderCountTest):
          print(f"i{i}")
          print("\r", end="");
          print("BC1 is:  ",end="");
          BC1.read()
          print("\n");
          BC1.rangeBinaryOperation(BC3, fuzzyZor)
          print("bc1 after:  ",end="")
          BC1.read()
          PickRandomFunction(BC1,BC2);
          print("bc1 after random function");
          BC1.read()
          print("bc2 afrer random function")
          BC2.read()
          print("now xoring");
          BC1.BIT_OPERATION(BC2,"XOR")
          BC1.increase(1)
          BC3.increase(3)