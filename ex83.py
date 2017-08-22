from screeninfo import get_monitors

for m in get_monitors():
    print(type(str(m)))
    print(str(m)[8:12])
    print(str(m)[13:16])
    
    print("Width: " + str(m)[8:12] + "," + " Height: " + str(m)[13:16])
    
'''

    from screeninfo import get_monitors
     
    width=get_monitors()[0].width
    height=get_monitors()[0].height
     
    print("Width: %s,  Height: %s" % (width, height))
'''
