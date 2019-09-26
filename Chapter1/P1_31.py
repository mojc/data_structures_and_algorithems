def make_change(price, given, bills = [1,2,5,10,20,50,100]):
    assert given>=price
    to_return = given-price
    change = {}
    for bill in reversed(bills):
        x = to_return//bill
        to_return = to_return - x*bill
        if x > 0:
            change[bill]=x
    # could order by bill
    return change

print(make_change(21, 150))