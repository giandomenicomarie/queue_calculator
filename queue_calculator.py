import math

def mm1_queue(lmbda, mu):
    rho = lmbda / mu
    L = rho / (1 - rho)
    Lq = rho**2 / (1 - rho)
    W = 1 / (mu - lmbda)
    Wq = rho / (mu - lmbda)
    P0 = 1 - rho
    return {
        "Utilization Rate (ρ)": rho,
        "Average Number in System (L)": L,
        "Average Number in Queue (Lq)": Lq,
        "Average Time in System (W)": W,
        "Average Time in Queue (Wq)": Wq,
        "Probability of 0 in System (P0)": P0
    }
