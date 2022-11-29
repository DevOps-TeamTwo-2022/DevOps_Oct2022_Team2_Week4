import pytest 
from helloworld import helloworld

def test_testOne():
  theInput = "Test"
  result = helloworld(theInput)
  
  assert len(result) > 10 or len(result) == 0, "Input string too long!"
  #assert len(result) < 10 or len(result) == 0, "Input string too long!"
    
test_testOne()  
