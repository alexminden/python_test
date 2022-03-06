def convert(number):
    conditions = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong',
    }
    sound = ''.join([v for k, v in conditions.items() if number % k == 0])
    return sound or str(number)