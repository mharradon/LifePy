from __future__ import print_function
from LifePy import LifePy
from time import sleep

# Initialize function with module name, function name
func = LifePy('getStr','getStr')

print("Change the getStr function while test is running. It won't update if an exception is thrown by the function or on import.")

while True:
  print(func())
  sleep(0.5)
