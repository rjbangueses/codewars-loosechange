def loose_change(cents):

    result = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    #validate input
    try:
        value = int(cents)
        if value <= 0:
            print(result)
            return
        else: 
            total = cents
    except:
        try: 
            value = float(cents)
            if value <= 0:
                print(result)
                return
            else:
                total = int(cents)
        except:
            print(result)
            return
     
    result['Quarters'] = int(total) // 25
    leftover = total % 25
    result['Dimes'] = int(leftover) // 10
    leftover = leftover % 10
    result['Nickels'] = int(leftover) // 5
    leftover = leftover % 5
    result['Pennies'] = int(leftover)
    print(result)
