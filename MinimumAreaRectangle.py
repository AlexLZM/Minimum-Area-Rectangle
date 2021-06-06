def minAreaRect(points) -> int: 
    '''
    points is a list of [x, y] points
    '''
    n = len(points)

    mappingx = collections.defaultdict(set)
    mappingy = collections.defaultdict(set)
    
    for x, y in points:
        mappingx[x].add(y)
        mappingy[y].add(x)

    nx = len(mappingx)
    ny = len(mappingy)
    if nx == n or ny == n:
        return 0

    mapping = mappingx if ny > nx else mappingy

    keys = list(mapping.keys())
    area = float('inf')
    for i, x in enumerate(keys):
        for x1 in keys[i+1:]:
            yset, yset1 = mapping[x], mapping[x1]
            interset = sorted(yset.intersection(yset1))
            if len(interset) > 1:
                min_ydiff = min(interset[i+1]-interset[i]
                                for i in range(len(interset)-1))
                area = min(area, min_ydiff * abs(x1-x))


    return 0 if area == float('inf') else area
