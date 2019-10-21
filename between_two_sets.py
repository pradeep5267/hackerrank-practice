def getTotalX(a, b):
    def isValid(a, b, candidate):
        for a_ele in a:
            if candidate % a_ele != 0:
                return False
        for b_ele in b:
            if b_ele % candidate != 0:
                return False
        return True

    cnt = 0
    for candidate in range(max(a), min(b)+1):
        if isValid(a, b, candidate):
            cnt += 1
    
    return cnt