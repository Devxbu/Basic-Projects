import mouse, keyboard, random, string

letter = list(string.ascii_lowercase)

while True:
    mouse.move(300,300,False,5)
    word = letter[random.randint(0, len(letter)-1)] + letter[random.randint(0, len(letter)-1)] + letter[random.randint(0, len(letter)-1)] + letter[random.randint(0, len(letter)-1)] + letter[random.randint(0, len(letter)-1)] + letter[random.randint(0, len(letter)-1)]
    keyboard.write(word+"\n", 3)

