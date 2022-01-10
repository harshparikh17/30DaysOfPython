print("Welcome to Our Shop")
print("Product-Redmi note 10 \n Price-1900  /n To buy this type 1" )
print("Product-Boat rockerz Headphone \n Price-1800 \n To buy this type 2")
print("Product-Mi PowerBank(10000mh) \n Price-2000 \n To buy this type 3")
print("Product-Samsung Tablet \n Price-18000 \n To buy this type 4")
print("Product-Sony Smart Tv \n Price-30000 \n To buy this product type 5")
a=int(input("Type your Product number:"))
if(a==1):
    print("Thanks For Selecting Redmi note 10")
    print("You have coupon code-DISC")
    d=input("Type your coupon code to get some disconnt:")
    if(d=="DISC"):
        pay=19000-19000*(20/100)
        print(f"You have got 20% discount")
        print(f"Net payable amount is:{pay}")
    else:
        print("You have Enter invalid coupon code")

if(a==2):
    print("Thanks For Selecting Boat rockerz Headphone")
    print("You have coupon code-DISC")
    d=input("Type your coupon code to get some disconnt:")
    if(d=="DISC"):
        pay=1800-1800*(5/100)
        print(f"You have got 5% discount")
        print(f"Net payable amount is:{pay}")
    else:
        print("You have Enter invalid coupon code")

if(a==3):
    print("Thanks For Selecting Mi PowerBank(10000mh)")
    print("You have coupon code-DISC")
    d=input("Type your coupon code to get some disconnt:")
    if(d=="DISC"):
        pay=2000-2000*(10/100)
        print(f"You have got 10% discount")
        print(f"Net payable amount is:{pay}")
    else:
        print("You have Enter invalid coupon code")

if(a==4):
    print("Thanks For Selecting Samsung Tablet")
    print("You have coupon code-DISC")
    d=input("Type your coupon code to get some disconnt:")
    if(d=="DISC"):
        pay=18000-18000*(10/100)
        print(f"You have got 10% discount")
        print(f"Net payable amount is:{pay}")
    else:
        print("You have Enter invalid coupon code")

if(a==5):
    print("Thanks For Selecting Sony Smart Tv")
    print("You have coupon code-DISC")
    d=input("Type your coupon code to get some disconnt:")
    if(d=="DISC"):
        pay=30000-30000*(20/100)
        print(f"You have got 20% discount")
        print(f"Net payable amount is:{pay}")
    else:
        print("You have Enter invalid coupon code")
    
    

   