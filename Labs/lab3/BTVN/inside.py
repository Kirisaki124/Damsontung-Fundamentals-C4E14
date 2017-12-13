def is_inside(point, rectangle):
        if point[0] <= rectangle[0] + rectangle[2] and point[0] >= rectangle[0]   and point[1] <= rectangle[1] + rectangle[3] and point[1] >= rectangle[1]:
            print("true")
        else:
            print("false")
        return



is_inside([100,120], [140,60,100,200])
