def soe(a,n):
    if n <= 2:
        return []
    sieve = range(3, n+1, 2)
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    if (a<3):
    	return [2] + [el for el in sieve if el]
    if a>2:
    	return [el for el in sieve if el]
a,b=map(int, raw_input().split())
primelist=soe(a,b)
print primelist
