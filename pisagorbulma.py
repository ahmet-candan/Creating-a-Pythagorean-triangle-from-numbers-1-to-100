def pisagor_bulma():
    pisagor= list()
    for i in range(1,1000):
        for j in range(1,1000):

            c = (i**2+j**2)**0.5

            if(c==int(c)):
                pisagor.append((i,j,int(c)))
    return pisagor
print("Özel Üçgenler")
for i in pisagor_bulma():
    print(i)