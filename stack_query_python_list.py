'''
This is full implementation stack using python list. init() is optional , it eas reqd. for this case.
check push, pop and query methods
'''

import sys 

stk = []
min_stk = []
top = -1
min_top = -1 


def query():
  global stk, min_stk, top, min_top 
  if len(min_stk) == 0:
    return "Empty"
  else:
    return min_stk[min_top]

def pop():
  global stk, min_stk, top, min_top
  if len(stk) != 0:
    x = stk.pop()
    top -= 1 
  
  if len(min_stk)!= 0 and x == min_stk[min_top]:
    min_stk.pop()
    min_top -= 1 
  

def push(num):
  global stk, min_stk, top, min_top 
  stk.append(num)
  top += 1 
  if len(min_stk) == 0:
    min_stk.append(num)
    min_top += 1 
  elif num >= min_stk[min_top]:
    min_stk.append(num)
    min_top += 1 

def init():
  global stk, min_stk, top, min_top 
  stk = []
  min_stk = []
  top = min_top = -1
    
if __name__ == "__main__":
  T = int(sys.stdin.readline().strip())
  for ti in range(T):
    print(f'Case {ti+1}:')
    init()
    nq = int(sys.stdin.readline().strip())
    for q in range(nq):
      inst = sys.stdin.readline().strip()
      if inst[0] == "A":
        cmd, num = inst.split(' ')
        push(int(num))
      elif inst[0] == "Q":
        print(query())
      elif inst[0] == "R":
        pop()
