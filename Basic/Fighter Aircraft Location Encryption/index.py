def encrypt(base,fakeLocation):
    temp = 0
    for i in str(fakeLocation):
        temp += int(i) * (base ** (len(str(fakeLocation)) - (str(fakeLocation).index(i)+1)))
    return temp

print(123,encrypt(6,123))