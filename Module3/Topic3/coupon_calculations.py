'''
Program: coupon_calculations.py
Author: Reagan Zierke
Last date modified: 09/07/22

This program prompts users for the price of an item, coupons, and discounts. It then returns the total price of the order after shipping and tax.
'''

#Sets a constant tax rate (6%)
tax = 1.06

#Asks user for price of order
order = float(input("Enter the price of the order: "))
#Asks user for coupon amount
print("Here are the available cash off coupons for use."
      "\n1. No Coupon"
      "\n2. $5 off"
      "\n3. $10 off")
coupon = int(input("Enter the number that corresponds to the coupon you'd like to apply: "))
#Asks user for discount rate
print("Here are the available discount coupons for use."
      "\n1. No Coupon"
      "\n2. 10% off"
      "\n3. 15% off"
      "\n4. 20% off")
discount = int(input("Enter the number that corresponds to the coupon you'd like to apply: "))

#Apply cash coupon using if and elif statements
if coupon == 2:
    order = order - 5.0
elif coupon == 3:
    order = order - 10.0
else:
    order = order

#Apply discount coupon using if and elif statements
if discount == 2:
    order = order - (0.1*order)
elif discount == 3:
    order = order - (0.15*order)
elif discount == 4:
    order = order - (0.2*order)
else:
    order = order

#Apply tax
order_after_tax = order*tax

#Add Shipping
if order < 10.0:
    shipping = 5.95
elif order < 30.0:
    shipping = 7.95
elif order < 50.0:
    shipping = 11.95
else:
    shipping = 0
order = order_after_tax + shipping

print(f"Your order after coupons, tax, and shipping cost {order: .2f}.")

