# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a,b,c):
    return max([a,b,c])

print(max_num(1,2,3))
print(max_num(50,25,1))
print(max_num(40,30,20))

# Write a Python function called mult_list() to multiply all the numbers in a list.

def  mult_list(num):
    if len(num) == 0:
        return 0
    
    prod = num[0]

    if len(num) > 1:
        for i in num[1:]:
            prod = prod * i

        return prod
    
print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([10]))
# Write a Python function called rev_string() to reverse a string.

def rev_string(my_string):
    return my_string[::-1]

print(rev_string(""))
print(rev_string("reverse"))
print(rev_string("a string"))

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(3,2,4))     
print(num_within(3,1,3))     
print(num_within(10,2,5))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

triangle = [[1],[1,1]]
def pascal(n):

  if n < 1:
    print("Need more rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2

    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]

      length = len(row_prev)+1
      for i in range(length):

        if i == 0:
          row.append(1)

        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])

        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    for row in triangle:
      print(row)

pascal(1)
pascal(9)