def division(a, b):
    try:
        return round(float(b) / float(a), 7)
    except:
        print('Dividend cannot be zero.')
