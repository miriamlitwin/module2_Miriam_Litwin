Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:5

---Receipt---
Traceback (most recent call last):
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 36, in <module>
    campus_cafe()
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 30, in campus_cafe
    print(f"{line_total(number_of_coffees)} = {format_currency(coffee)}")
TypeError: campus_cafe.<locals>.line_total() missing 1 required positional argument: 'qty'

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
Traceback (most recent call last):
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 37, in <module>
    campus_cafe()
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 6, in campus_cafe
    coffee = line_total(number_of_coffees * COFFEE_CONV)
UnboundLocalError: cannot access local variable 'line_total' where it is not associated with a value

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
Traceback (most recent call last):
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 37, in <module>
    campus_cafe()
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 8, in campus_cafe
    coffee = line_total(number_of_coffees * COFFEE_CONV)
TypeError: campus_cafe.<locals>.line_total() missing 1 required positional argument: 'qty'

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
Traceback (most recent call last):
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 37, in <module>
    campus_cafe()
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 8, in campus_cafe
    coffee = line_total(number_of_coffees * COFFEE_CONV)
TypeError: campus_cafe.<locals>.line_total() missing 1 required positional argument: 'qty'

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:5

---Receipt---
5 @$2.25 = $11.25
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
TOTAL: $28.47
Thank You!

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
enter tip percent:10
enter tip percent:10
enter tip percent:
====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?
====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:10
Traceback (most recent call last):
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 35, in <module>
    campus_cafe()
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 16, in campus_cafe
    total = compute_totals(subtotal_and_tax,subtotal_and_tip,subtotal)
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 11, in compute_totals
    return(tax, tip, total)
NameError: name 'tax' is not defined. Did you mean: 'max'?

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?
====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5
Traceback (most recent call last):
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 35, in <module>
    campus_cafe()
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 16, in campus_cafe
    total = compute_totals(subtotal_and_tax,subtotal_and_tip,subtotal)
NameError: name 'subtotal_and_tax' is not defined

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5
Traceback (most recent call last):
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 35, in <module>
    campus_cafe()
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 16, in campus_cafe
    total = compute_totals(tax,tip,total)
UnboundLocalError: cannot access local variable 'total' where it is not associated with a value

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:5

---Receipt---
5 @$2.25 = $11.25
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
Traceback (most recent call last):
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 35, in <module>
    campus_cafe()
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 33, in campus_cafe
    print(f"TOTAL: {format_currency(total)}")
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 18, in format_currency
    return f"${x:.2f}"
TypeError: unsupported format string passed to tuple.__format__

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:5

---Receipt---
5 @$2.25 = $11.25
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
TOTAL: $5.69
Thank You!

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:5

---Receipt---
5 @$2.25 = $11.25
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
TOTAL: $5.69
Thank You!

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:5

---Receipt---
5 @$2.25 = $11.25
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
Traceback (most recent call last):
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 35, in <module>
    campus_cafe()
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 33, in campus_cafe
    print(f"TOTAL: {format_currency(total)}")
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 18, in format_currency
    return f"${x:.2f}"
ValueError: Unknown format code 'f' for object of type 'str'

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:5

---Receipt---
5 @$2.25 = $11.25
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
TOTAL: $28.47
Thank You!

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
Tip: $1.25
TOTAL: $28.47
Thank You!

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
Tip: $1.25
TOTAL: $28.47
Thank You!

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5
Traceback (most recent call last):
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 36, in <module>
    campus_cafe()
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 19, in campus_cafe
    print_receipt(number_of_muffins,coffee,number_of_muffins,muffins,subtotal,tax,tip,total)
UnboundLocalError: cannot access local variable 'print_receipt' where it is not associated with a value

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:5


====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:5

5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
Tip: $1.25
TOTAL: $28.47
Thank You!

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:5

5 @$2.25= $11.25
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
Tip: $1.25
TOTAL: $28.47
Thank You!

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:5

5 @$2.25= $11.25
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
Tip: $1.25
TOTAL: $28.47
Thank You!

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:5

5 @$2.25= $11.25
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
Tip: $1.25
TOTAL: $28.47
Thank You!
<class 'float'>

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:5

5 @$2.25= $11.25
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
Tip: $1.25
TOTAL: $28.47
Thank You!
<class 'float'>

Warning (from warnings module):
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 36
    print_receipt(None(number_of_muffins,coffee,number_of_muffins,muffins,subtotal,tax,tip,total))
SyntaxWarning: 'NoneType' object is not callable; perhaps you missed a comma?
>>> 
====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:5

5 @$2.25= $11.25
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
Tip: $1.25
TOTAL: $28.47
Thank You!
<class 'float'>

Warning (from warnings module):
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 37
    print_receipt(None(number_of_muffins,coffee,number_of_muffins,muffins,subtotal,tax,tip,total))
SyntaxWarning: 'NoneType' object is not callable; perhaps you missed a comma?
>>> 
====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

Traceback (most recent call last):
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 40, in <module>
    main()
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 25, in main
    print(f"How many coffees?{number_of_coffees}")
NameError: name 'number_of_coffees' is not defined

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5
<class 'float'>
Traceback (most recent call last):
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 40, in <module>
    main()
NameError: name 'main' is not defined. Did you mean: 'min'?

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:5

5 @$2.25= $11.25
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
Tip: $1.25
TOTAL: $28.47
Thank You!
<class 'float'>

Warning (from warnings module):
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 40
    print_receipt(None(number_of_muffins,coffee,number_of_muffins,muffins,subtotal,tax,tip,total))
SyntaxWarning: 'NoneType' object is not callable; perhaps you missed a comma?
>>> 
====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?-1
Please write an amount greater than or equal to 0
how many muffins?
====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?-1
enter tip percent:10

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?-1
Enter tip percent:10

5 @$2.25= $11.25
-1 @$2.75= $-2.75
Subtotal: $8.50
Tax(8.875%): $0.75
Tip: $0.85
TOTAL: $10.10
Thank You!
<class 'float'>

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?-1
how many muffins?5
enter tip percent:10

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?-1
How many muffins?5
Enter tip percent:10

-1 @$2.25= $-2.25
5 @$2.75= $13.75
Subtotal: $11.50
Tax(8.875%): $1.02
Tip: $1.15
TOTAL: $13.67
Thank You!
<class 'float'>

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?-1
Please write an amount greater than or equal to 0
how many muffins?5
enter tip percent:10

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?-1
How many muffins?5
Enter tip percent:10

-1 @$2.25= $-2.25
5 @$2.75= $13.75
Subtotal: $11.50
Tax(8.875%): $1.02
Tip: $1.15
TOTAL: $13.67
Thank You!
<class 'float'>

Warning (from warnings module):
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 42
    print_receipt(None(number_of_muffins,coffee,number_of_muffins,muffins,subtotal,tax,tip,total))
SyntaxWarning: 'NoneType' object is not callable; perhaps you missed a comma?
>>> 
====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:10

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:10

5 @$2.25= $11.25
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
Tip: $2.50
TOTAL: $29.72
Thank You!
<class 'float'>

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?-1
Please write an amount greater than or equal to 0
how many coffees?-1
how many muffins?
====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?-1
Please write an amount greater than or equal to 0
how many muffins?1
enter tip percent:10

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?1
Enter tip percent:10

5 @$2.25= $11.25
1 @$2.75= $2.75
Subtotal: $14.00
Tax(8.875%): $1.24
Tip: $1.40
TOTAL: $16.64
Thank You!
<class 'float'>

Warning (from warnings module):
  File "C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py", line 45
    print_receipt(None(number_of_muffins,coffee,number_of_muffins,muffins,subtotal,tax,tip,total))
SyntaxWarning: 'NoneType' object is not callable; perhaps you missed a comma?
>>> 
====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:-1
Please write an amount greater than or equal to 0
enter tip percent:10

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:10

5 @$2.25= $11.25
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
Tip: $2.50
TOTAL: $29.72
Thank You!
<class 'float'>

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

====== RESTART: C:\Users\benzl\OneDrive\Documents\Campus Cafe for tues.py ======
how many coffees?5
how many muffins?5
enter tip percent:5

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:5

5 @$2.25= $11.25
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
Tip: $1.25
TOTAL: $28.47
Thank You!
>>> 
======== RESTART: C:/Introduction to Programming/Campus Cafe for tues.py =======
how many coffees?5
how many muffins?5
enter tip percent:10

===Campus Cafe===
Coffee:$2.25
Muffin:$2.75

How many coffees?5
How many muffins?5
Enter tip percent:10

5 @$2.25= $11.25
5 @$2.75= $13.75
Subtotal: $25.00
Tax(8.875%): $2.22
Tip: $2.50
TOTAL: $29.72
Thank You!
