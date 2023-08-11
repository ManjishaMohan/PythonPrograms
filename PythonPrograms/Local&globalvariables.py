# 1.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#2.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#3.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#4.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#5th question:

x = "awesome"

def myfunc():
  global x
  x = "super"

myfunc()

print("Python is " + x)

#-------------------------
def some_func():
  print("Inside some_func")

  def some_inner_func():
    var = 10
    print("Inside inner function, value of var:", var)

  some_inner_func()
  print("Try printing var from outer function: ", var)


some_func()
