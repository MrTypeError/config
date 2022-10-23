from random import choice
from string import ascii_letters , digits # learn me 

MAX_RAN = ascii_letters + digits

def createRandom(chars = MAX_RAN):
    return "".join([choice(chars) for i in range(7)])

def createShortUrl(model_ins):
    temp = createRandom()
    model_class = model_ins.__class__ # learn me
    if model_class.objects.filter(short_url = temp).exists():
        return createShortUrl(model_ins)
    return temp
    







