def find_leaving_customer(total_computers, occurrences):
    occupied = set()
    leaving = 0
    
    for i in range(len(occurrences)):
        customer = occurrences[i]
        
        if customer not in occupied:
            if len(occupied) < total_computers:
                occupied.add(customer)
            else:
                leaving += 1 
                occupied.add(customer)
        else:
            occupied.remove(customer)
    
    return leaving

N = 2
S = "GACCBDDBAGEE"
print(find_leaving_customer(N, S))

N = 1
S = 'ABCBAC'
print(find_leaving_customer(N, S))
