def somme(nb1, nb2):
    return nb1 + nb2

def moyenne(nb1, nb2):
    return somme(nb1, nb2) / 2

note1 = 10
note2 = 30

moyenne = moyenne(note1, note2)

print("Note 1 : ", note1)
print("Note 2 : ", note2)

print("La moyenne est de", moyenne)

def mean(nb1, nb2, nb3):
    return (nb1 + nb2 + nb3) / 3

print(mean(1,2,3))
