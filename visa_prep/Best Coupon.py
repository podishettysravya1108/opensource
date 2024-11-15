bill_amount=int(input())
x=bill_amount*(10/100)
discount1=bill_amount-x
discount2=bill_amount-100
print(min(int(discount1),discount2))
