import imp

class LifePy(object):
  def __init__(self,module_name,func_name):
    self.module_name = module_name
    self.func_name = func_name
    self.i=0
    self.module = self.get_module()
    self.inc()

  def __call__(self,*args,**kwargs):
    try:
      new_module = self.get_module()
      result = getattr(new_module,self.func_name)(*args,**kwargs)
      self.module = new_module
      self.inc()
    except Exception as E:
      print(E)
      result = getattr(self.module,self.func_name)(*args,**kwargs)
    return result
 
  def get_module(self):
    return imp.load_module(self.module_name+str(self.i), *imp.find_module(self.module_name))
  
  def inc(self):
    self.i = self.i+1
