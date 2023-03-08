# Treure una cadena des d'uns separadors
def substring(caracter_in, caracter_out, text):
    index_in = text.index(caracter_in)
    index_out = text.index(caracter_out) 
    subcadena = text[index_in+1:index_out]
    return subcadena
