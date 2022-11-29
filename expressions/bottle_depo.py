#bottle deposists
one_litre_or_less=0.10
more_than_one_litre=0.25
less=int(input("how many containers less than one litre"))
more=int(input("how many containers more than one litre"))
refund=less * one_litre_or_less + more * more_than_one_litre 
print("your total refund will be",refund,"$")
