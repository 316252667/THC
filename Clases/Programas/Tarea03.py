def Diana(x,y) :
    if x<5:
        if y<10:
            return 3
        if y>=10 and y <=30:
            return 5
        if y>30:
            return 3
    if x>=5 and x<=25:
        if y<10:
            return 7
        if y >=10 and y<=30:
            return 10
        if y>30:
            return 7
    if x>25:
        if y<10:
            return 3
        if y>=10 and y<=30:
            return 5
        if y>30:
            return 3


x= Diana(5,3)
print(x)
