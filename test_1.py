

"""
This program wants to determine which payment option is better out of the two payment options.
The first option consists of $100 per day for 10 days. The second option consists of 1 dollar per day 
with the dollar amount being doubled each day for 10 days. This program will use two functions to calculate the 
amount of money earned. function1 will be used to calculate the amount for option1 and function2 will be used 
to calculate the amount for option2.

funtion1 will output and calculate $100 * 10 days.
function2 will loop 10 times, as the amount doubles with each time; and then the amount is added to the total.

If Option 1 is better, then the given output will be "Option 1 is better".
If Option 2 is better, then the given output will be "Option 2 is better".
If the amount is equal or the same, the given output will be "Option 1 and Option 2 pays the same".

"""

"""
# option1
  return 100 * 10

# option2 
  amount = 1 
  list1 = []
  loop 10 times 
    add amount to list1
    amount *= 2
  sum = sum of all items in the loop
  return sum 
# main 
  var1 = option1
  var2 = option2

  if var1 = var2
    "Option 1 and Option 2 pays the same"
  if var1 > var2
     "Option 1 is better"
  else
     "Option 2 is better"

main
"""

def option1():
    return 100 * 10

def option2():
    amount = 1
    list1= []
    for i in range(0,10):
     list1.append(amount)
     amount *= 2
    print("list1", list1)
    total = sum(list1)
    return total

def main():
    answer = ""
    var1 = option1()
    var2 = option2()
    if var1 == var2:
        answer= "Option 1 and Option 2 pays the same."
    elif var1 < var2:
        answer= "Option 2 is better."
    else:
        answer= "Option 1 is better."
    
    #print(var1)
    #print(var2)
    print (answer)

main()







