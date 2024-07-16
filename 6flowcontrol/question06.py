def to_allcaps(word):
    if len(word) > 10:
        return(word.upper())
    else:
        return(word)
        
print(to_allcaps("Hello World!"))
print(to_allcaps("Hello"))