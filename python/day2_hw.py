amount = 24000

limitAmount = 25000

note500 = 500
note500Count = 0

note1000 = 1000
note1000Count = 0

note5000 = 5000
note5000Count = 0

if amount > 0 and amount <= limitAmount:
    validation = amount % note500
    if validation == 0:
        if amount >= note5000:
            note5000Count = amount//note5000
            amount = amount % note5000
        if amount >= note1000:
            note1000Count = amount//note1000
            amount = amount % note1000
        if amount >= note500:
            note500Count = amount//note500
            amount = amount % note500
        print(f'{note5000} * {note5000Count} + {note1000} * {note1000Count} + {note500} * {note500Count}')
    else:
        print('You can withdraw minimum 500 note')
else:
    print('Amount should be greater than zero and less than equal to 25000')