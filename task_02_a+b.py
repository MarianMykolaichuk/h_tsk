# Define integer variables a and b.
#  Read values a and b from console and calculate: 
# a + b 
# a - b 
# a * b 
# a / b. 
# Output obtained results.


var_a = input("a = ")
var_b = input("b = ")

add = int(var_a) + int(var_b)
subt = int(var_a) - int(var_b)
multi = int(var_a) * int(var_b)
div  = int(var_a) / int(var_b)
print("a + b = " + str(add))
print("a - b = " + str(subt))
print("a * b = " + str(multi))
print("a / b = " + str(div))
