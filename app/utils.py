# this is the app/utils.py file 

def to_usd(my_price): 
    """
    Docstring will display an integer in USD format.
    Invoke like this: to_usd(0.000)
    """
    return '${:,.2f}'.format(my_price)


if __name__ == "__main__":
    price = input("Please choose a price like 10.999:")
    print(to_usd(float(price)))

