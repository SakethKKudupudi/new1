#Example 1: Using __class__.__name__
class Vehicle:
    def name(self, name):
        return name

v = Vehicle()
print(v.__class__.__name__)
#__class__ is the attribute of the class to which it is associated and __name__ is a special variable in Python. 
# Its functionality depends on where it is used.
# Create an object v of class Vehicle().
# Print the name of the class using __class__.__name__.


#Example 2: Using type() and __name__ attribute
class Vehicle:
    def name(self, name):
        return name

v = Vehicle()
print(type(v).__name__)
#Using attribute __name__ with type(), 
# you can get the class name of an instance/object as shown in the example above.

# type() gives the class of object v and __name__ gives the class name.

# Python Program to Differentiate Between type() and isinstaunce()
class Polygon:
    def sides_no(self):
        pass

class Triangle(Polygon):
    def area(self):
        pass

obj_polygon = Polygon()
obj_triangle = Triangle()

print(type(obj_triangle) == Triangle)   	# true
print(type(obj_triangle) == Polygon)    	# false

print(isinstance(obj_polygon, Polygon)) 	# true
print(isinstance(obj_triangle, Polygon))	# true
#In the above example, we see that type() cannot distinguish whether an instance of a class is somehow related to the base class. 
#In our case, although obj_triangle is an instance of child class Triangle, it is inherited from the base class Polygon. 
#If you want to relate the object of a child class with the base class, you can achieve this with instance().