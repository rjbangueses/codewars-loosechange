def loose_change(quantity):
    result = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    if quantity == 0:
        print(result)
        return
    try:
        cents = int(quantity)
    except:
        cents = float(quantity)   
     
    result['Quarters'] = cents // 25
    leftover = cents % 25
    result['Dimes'] = leftover // 10
    leftover = leftover % 10
    result['Nickels'] = leftover // 5
    leftover = leftover % 5
    result['Pennies'] = leftover
    print(result)

def validateInput(value):
    try:
        value = int(value)
        if value > 0:
            loose_change(value)
        else:
            loose_change(0)
    except:
        try: 
            value = float(value)
            if value > 0:
                loose_change(value)
            else:
                loose_change(0)
        except:
            loose_change(0)
    
while True:
    inp = input("Type quantity in cents: ") 
    validateInput(inp)