

class Person:
	def __init__(self,first,last):		
	   self.first=first
	   self.last=last
	    
	def set_f(self,first):
		  self.first=first
	def get_f(self):
	   return self.first
	def set_l(self,last):
		  self.last=last
	def get_l(self):         
          return self.last
    
        
          
print("---------------------------------")

p=Person('kat','papa')
print("Hello!!!My name is {}.".format(p.get_f()))


