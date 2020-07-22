#Variable - stores a single piece of delattr

#name = data
score = 0
name = "Bob"
health = 5
pizza_topping = "pineaplle"

#LOOPS - repeats code for a given amount of times or until a condition is met 

#FOR LOOP - repeats code for a # of times

#syntax: for i in range(#) 
          #compile

# for = logic statement 
# i = loop variables, labels which literation we're on in the loop 
# in 
# range(#) = a function that will repeat the loop for the number of times defined in the parenthesis

#for i in range(4):
  #print("hello")

#for i in range(4):
  #print("bye")
#for i in range(4):
  #for i in range(5):
    #print("yikes")



while pizza_topping == "pinaepple":
  for i in range(4):
    print("yum")
  print("cheese")
  pizza_topping = "pepperoni"

  
#CONDITIONALS - if/else statements test of a condition is true then do an action, if it is not, do something else

#SYNTAX
# if - first condition to test
#elif - secondary condition to test, can have unlimited amount of elif # else - the last contion 


#num = input('give me a number: ')
#used integer function to turn num from a string data type to a integer
#num = int(num)


#if num > 5:
 # print("greater than 5")
#elif num < 5:
 # print("less than 5")
#else:
 # print("equal to 5")
# Write a Python program to test if a number is positive or negative. The program will ask the user to input a number, then it will 
# display what the number is.

#pos number = < 0
#neg number = > 0

num = input('give me a number: ')
num = int(num)

if num > 0:
  print("postitive number")
elif num < 0: 
  print("negative number")
else:
  print("equal to 0")

