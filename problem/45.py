def calculate_annual_return(initial_investment, final_investment, years):
    annual_return = (final_investment/initial_investment)**(1/years)-1
    percent = annual_return * 100
    return(f"{percent:.2f}")

initial_investment = 1000
final_investment = 1500
years = 5

print(calculate_annual_return(initial_investment, final_investment, years))