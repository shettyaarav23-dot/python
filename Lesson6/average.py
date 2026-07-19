# 1) Take three integer inputs from the user and store them in `a`, `b`, and `c`.
a=3
b=8
c=10
# 2) Calculate the average of `a`, `b`, and `c`:
average=(a+b+c)/3
print(average)
# 3) Compare `avg` with `a`, `b`, and `c` using if–elif:

# - If `avg` is greater than all three numbers, print that it is higher than `a`, `b`, and `c`.
if average>a and average>b and average>c:
    print("it is greater than all")
elif average>a and average>b:
    print("it is greater than a and b")
elif average>b and average>c:
    print("it is greater than b and c")
else:
    print("invalid condition")
# - Else if `avg` is greater than `a` and `b`, print that it is higher than `a` and `b`.

# - Else if `avg` is greater than `a` and `c`, print that it is higher than `a` and `c`.

# - Else if `avg` is greater than `b` and `c`, print that it is higher than `b` and `c`.

# - Else if `avg` is greater than only `a`, print that it is just higher than `a`.

# - Else if `avg` is greater than only `b`, print that it is just higher than `b`.

# - Else if `avg` is greater than only `c`, print that it is just higher than `c`.

# 4) If none of the above conditions match, print "invalid input".