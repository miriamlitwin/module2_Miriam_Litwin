'''
1. defines main
2. defines constant price for a coffee
3. defines constant price for a muffin
4. asks user for amount of coffee and returns it as an integer
5. if amount is less than 0, prints an error and asks user to reenter
6. asks user for amount of muffins and returns it as an integer
7. if amount is less than 0, prints an error and asks user to reenter
8. returns as float and calculates the price
9. calculates price of coffee
10. calculates price of muffins
11. calculates subtotal and returns as float
12. calculates tax
13. asks user to enter tip percent and returns it as an integer
14. if amount is less than 0, prints an error and asks user to reenter
15. calculates tip
16. calculates total
17. returns float to the hundreths place for the upcoming calculations
18. prints receipt
19. calls main
'''
def main():
    COFFEE_CONV = 2.25
    MUFFIN_CONV = 2.75
    number_of_coffees = int(input("how many coffees?"))
    if number_of_coffees<=0:
        print("Error: Please enter an amount greater than or equal to 0")
        number_of_coffees = int(input("how many coffees?"))
    number_of_muffins = int(input("how many muffins?"))
    if number_of_muffins<=0:
        print("Error: Please enter an amount greater than or equal to 0")
        number_of_muffins = int(input("how many muffins?"))
    def line_total(unit_price:float,qty:int)->float:
        return(unit_price*qty)
    coffee = line_total(COFFEE_CONV, number_of_coffees)
    muffins = line_total(MUFFIN_CONV,number_of_muffins)
    subtotal = float(coffee + muffins)
    tax = subtotal * 0.08875
    tip_percent = int(input("enter tip percent:"))
    if tip_percent<=0:
        print("Please write an amount greater than or equal to 0")
        tip_percent = int(input("enter tip percent:"))
    tip = subtotal * tip_percent/100
    def compute_totals(subtotal:float,tax:float,tip:float)->tuple[float,float,float]:
        return(tax+tip+subtotal)
    total = compute_totals(tax,tip,subtotal)
    def format_currency(x:float)->str:
        return f"${x:.2f}"
    def print_receipt(number_of_coffees:int,coffee:float,number_of_muffins:int,muffins:float,subtotal:float,tax:float,tip:float,total:float)->None:
        print()
        print(f"===Campus Cafe===")
        print(f"Coffee:$2.25")
        print(f"Muffin:$2.75")
        print()
        print(f"How many coffees?{number_of_coffees}")
        print(f"How many muffins?{number_of_muffins}")
        print(f"Enter tip percent:{tip_percent}")
        print()
        print(f"{number_of_coffees} @$2.25= {format_currency(coffee)}")
        print(f"{number_of_muffins} @$2.75= {format_currency(muffins)}")
        print(f"Subtotal: {format_currency(subtotal)}")
        print(f"Tax(8.875%): {format_currency(tax)}")
        print(f"Tip: {format_currency(tip)}")            
        print(f"TOTAL: {format_currency(total)}")
        print("Thank You!")
    print_receipt(number_of_muffins,coffee,number_of_muffins,muffins,subtotal,tax,tip,total)
main()
