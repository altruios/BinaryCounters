import BinaryCounters as BAC
from PIL import Image
import numpy as np
import os
import time
import math
import random
BC= BAC.BC
class TestBinaryCounter:
     def test_1_overflow(self):
          for i in range(100):
               bin=BC(i,i)
               bin.SET_V(bin.GET_MAX())
               a=bin.VAL()
               bin.INCREASE(1)
               assert a==bin.VAL()
     def test_2_overflow_infinity(self):
          for i in range(100):
               bin=BC(i,i)
               bin.SET_V(bin.GET_MAX())
               a=bin.VAL()
               bin.INCREASE(float('inf'))
               assert a==bin.VAL()
     def test_3_overflow_negative(self):
          for i in range(100):
               bin = BC(0,i)
               bin.DECREASE(i)
               assert bin.VAL()==0
     def test_4_overflow_negative_infinity(self):
          for i in range(100):
               bin = BC(0,i)
               bin.DECREASE(float('inf'))
               assert bin.VAL()==0
     def test_5_bad_input_text(self):
          stringNumbers = ["1","2","3","4","5","6","7","8","9","10","-1","-20","-0.311111","-.343,fa","hello world","three","THREE","0",""]
          for i in range(100):
               bin=BC(stringNumbers[(i%len(stringNumbers))],i)
               print(bin.VAL())
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
     def test_8_method_SORT(self):
          bin1=BC(15,6)
          bin2=BC(15,12)
          bin3=BC(31,8)
          bin4=BC(63,16)
          bin1.SORT_B(True)
          print(bin1.VAL())
          assert bin1.VAL()==60
          bin1.SORT_B(False)
          assert bin1.VAL()==15
          bin2.SORT_B(True)
          assert bin2.VAL()==3840
          bin2.SORT_B(False)
          assert bin2.VAL()==15
          bin3.SORT_B(True)
          assert bin3.VAL()==248
          bin3.SORT_B(False)
          assert bin3.VAL()==31
          bin4.SORT_B(True)
          assert bin4.VAL()==64512
          bin4.SORT_B(False)
          assert bin4.VAL()==63
     def test_9_method_SET_BIT(self):
          bin1=BC(0,10)
          for i in range(bin1._length()):
               bin1.SET_BIT(1,i)
          assert bin1.VAL()==1023
          for i in range(bin1._length()):
               bin1.SET_BIT(0,i)
          assert bin1.VAL()==0
          for i in range(bin1._length()):
               if(i%2==0):
                    bin1.SET_BIT(1,i)
          assert bin1.COUNT(True)==5
          assert bin1.COUNT(False)==5
     def test_10_method_INCREASE(self):
          bin1=BC(0,10)
          c = 0
          for i in range(bin1._length()):
               bin1.INCREASE(i)
               c = c + i
          assert bin1.VAL()==c
     def test_11_method_DECREASE(self):
          bin1=BC(90,10)
          c = 90
          for i in range(bin1._length()):
               bin1.DECREASE(i)
               c = c - i
          assert bin1.VAL()==c
     def test_12_method_DECREASE_MIN_ZERO(self):
          bin1 = BC(90,10)
          c=90
          for i in range(c):
               bin1.DECREASE(i)
               c=c-i
          assert bin1.VAL()==0
          assert c<0
     def test_13_method_SET_V(self):
          bin1=BC(90,10)
          c=120
          bin1.SET_V(c)
          assert bin1.VAL()==c
     def test_14_method_SET_V_Negative(self):
          bin1=BC(90,10)
          c=-120
          bin1.SET_V(c)
          assert bin1.VAL()==0
     def test_15_method_SHIFT_UP(self):
          pass
     
     def test_16_method_SHIFT_DOWN(self):
          pass
     
     def test_17_method_SHIFT_CIRCLE_F(self):
          pass
     
     def test_18_method_SHIFT_CIRCLE_R(self):
          pass
     
     def test_19_method_KEEP_ODD(self):
          bc1 = BC(2,10)
          bc1.KEEP_ODD(False)
          assert bc1.VAL()==1
          bc1.INCREASE(1)          
          bc1.KEEP_ODD(True)
          assert bc1.VAL()==3          
     def test_20_method_KEEP_EVEN(self):
          bc1 = BC(3,10)
          bc1.KEEP_EVEN(False)
          assert bc1.VAL()==2
          bc1.INCREASE(1)
          bc1.KEEP_EVEN(True)
          assert bc1.VAL()==4         
     def test_21_method_SORT_B(self):
          bc1= BC(15,10)
          assert bc1.VAL()==15
          bc1.SORT_B(True)
          assert bc1.VAL()==960
          bc1.SORT_B(False)
          assert bc1.VAL()==15
     def test_22_method_SECTION(self):
          bc1 = BC(15,10)
          bcArray = bc1.SECTION(5,9)
          print(bcArray)
          assert bcArray == [0,1,1,1]
     def test_23_method_SPAWN(self):
          bc1 = BC(15,10)
          bc2 = bc1.SPAWN(5,9)
          bcArray = [0,1,1,1]
          assert bcArray == bc2.BIN()
          pass
     def test_24_method_GET_MAX(self):
          bin1=BC(0,10)
          bin1Max = bin1.GET_MAX()
          assert bin1Max==1023
          bin1.SET_V(bin1.GET_MAX())
          assert bin1.VAL() ==bin1Max     
     def test_25_method_BIN(self):
          bin1=BC(0,10)
          bin1.SET_V(16)
          binArr = [0,0,0,0,0,1,0,0,0,0]
          binTest = bin1.BIN()
          print(binArr,binTest)
          assert binArr==binTest
     def test_26_method_GET_BIN_OF(self):
          bin1=BC(0,10)
          binArrTest=[1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1]
          binNumTest = 172305
          x =bin1.GET_BIN_OF(binNumTest)
          print(x,binArrTest)
          assert binArrTest == x
     def test_27_method_SET_BIT_LENGTH(self):
          bc1=BC(0,10)
          l=9
          bc1.SET_BIT_LENGTH(l)
          assert bc1._length()==l  
     def test_28_method_B_TO_I(self):
          binary = [0,1,1,1,1]
          bin1=BC(0,10)
          r = bin1.B_TO_I(binary)     
          assert r==15
     def test_29_method_S_BIT_OP(self):
          pass
     def test_30_method_W_BIT_OP(self):
          pass     
     def test_31_method_BIT_OP(self):
          ops = ["OR","XOR","AND","NOT","NAND","XNOR","NOR"]
          results=[]
          for operation in ops:
               bc1=BC(58,10)
               bc2=BC(992,10)
               bc1.BIT_OP(bc2,operation)
               results.append(bc1.BIN())
          assert results[0]==[1,1,1,1,1,1,1,0,1,0]
          assert results[1]==[1,1,1,1,0,1,1,0,1,0]
          assert results[2]==[0,0,0,0,1,0,0,0,0,0]
          assert results[3]==[0,0,0,0,0,1,1,0,1,0]
          assert results[4]==[1,1,1,1,0,0,0,1,0,1]
          assert results[5]==[1,1,1,1,0,1,1,0,1,0]
          assert results[6]==[0,0,0,0,0,0,0,1,0,1]