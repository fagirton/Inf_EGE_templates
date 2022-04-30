for x in 0,1:
    for y in 0,1:
        for z in 0,1: #3 цикла for проверяют все комбинации x,y,z
                if ((x or y) <= (z==x))==0: 
                    print (x,y,z) #если условие рядом с if выполняется, print выводит значения x,y,z
