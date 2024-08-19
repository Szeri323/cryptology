#!/usr/bin/python3
def reversable_elements(ring):
    field_items = {}
    for item in ring:
        for item2 in ring:
            if(item * item2 % len(ring) == 1):
                field_items[item] = item2
    print(field_items)
    return field_items

def is_field(Z):
    pass

def create_ring(Z):
    ring = []
    for i in range(Z):
        ring.append(i)
    return ring

def is_number_reversable(num, Z):
    ring = create_ring(Z)
    rev_elem = reversable_elements(ring)
    if num in rev_elem:
        return True
    else:
        return False

def main():
    
    rev_elem = is_number_reversable(7, 26)
    print(rev_elem)
    
if __name__=="__main__":
    main()