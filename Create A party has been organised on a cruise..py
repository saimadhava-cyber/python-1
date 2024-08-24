def max_guests_present(T, E, L):
    max_guests = 0
    current_guests = 0
    for i in range(T):
        current_guests += E[i]  
        current_guests -= L[i] 
        max_guests = max(max_guests, current_guests)
    return max_guests
T = int(input())
E = [int(input()) for _ in range(T)]
L = [int(input()) for _ in range(T)]
print(max_guests_present(T,E,L))
