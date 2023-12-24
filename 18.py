def compound_interest(principal, rate, time):
    # Calculates compound interest
    amount = principal * (1 + rate / 100) ** time
    ci = amount - principal
    return ci

# Example usage
principal = 10000
rate = 10.25
time = 5
result = compound_interest(principal, rate, time)
print("Compound interest is", result)
