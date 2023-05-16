V_pool_litres = int(input())
P1_per_h = int(input())
P2_per_h = int(input())
worker_missed_h = float(input())


P1_litres = P1_per_h * worker_missed_h
P2_litres = P2_per_h * worker_missed_h

pipes_total = P1_litres + P2_litres

total_pipes_percent = (pipes_total / V_pool_litres) * 100

P1_percent = (P1_litres / pipes_total) * 100
P2_percent = (P2_litres / pipes_total) * 100

if pipes_total <= V_pool_litres:
    print(f"The pool is {total_pipes_percent:.2f}% full. Pipe 1: {P1_percent:.2f}%. Pipe 2: {P2_percent:.2f}%.")
else:
     overflow = abs(pipes_total - V_pool_litres)
     print(f"For {worker_missed_h:.2f} hours the pool overflows with {overflow:.2f} liters.")

