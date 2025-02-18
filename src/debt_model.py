import numpy as np
import pandas as pd
from scipy.optimize import minimize

class DebtModel:
    def __init__(self, cash_flows, interest_rates):
        """
        Initialize the debt model with projected cash flows and interest rates for different debt types.

        :param cash_flows: List or array of projected cash flows
        :param interest_rates: Dictionary of interest rates for different debt types
        """
        self.cash_flows = np.array(cash_flows)
        self.interest_rates = interest_rates
        self.debt_structure = {}

    def simulate_debt_service(self, debt_level, debt_type):
        """
        Simulate debt service capability given a debt level and type.

        :param debt_level: Amount of debt to simulate
        :param debt_type: Type of debt (e.g., 'senior', 'mezzanine')
        :return: Interest coverage ratio
        """
        interest_payment = debt_level * self.interest_rates[debt_type]
        interest_coverage = self.cash_flows / interest_payment
        return np.min(interest_coverage)  # Minimum coverage over the period

    def optimize_debt(self, debt_types):
        """
        Optimize debt structure across given debt types.

        :param debt_types: List of debt types to consider
        :return: Dictionary with optimal debt amounts for each type
        """
        def objective(x):
            # Total debt
            total_debt = sum(x)
            # Simulate for each type of debt
            coverage_ratios = [self.simulate_debt_service(x[i], debt_types[i]) for i in range(len(x))]
            # We want to maximize the minimum coverage ratio, but minimize the negative of it for optimization
            return -min(coverage_ratios)

        # Initial guess and bounds for each debt type
        initial_guess = [1e6 for _ in debt_types]  # Starting with 1 million for each type
        bounds = [(0, None) for _ in debt_types]  # Debt can't be negative, no upper limit

        result = minimize(objective, initial_guess, method='SLSQP', bounds=bounds)
        
        return {debt_types[i]: result.x[i] for i in range(len(debt_types))}

    def recommend_debt_structure(self):
        """
        Recommend the optimal debt structure based on current cash flow projections.

        :return: Dictionary with recommended debt structure
        """
        debt_types = list(self.interest_rates.keys())
        return self.optimize_debt(debt_types)

# Example usage
if __name__ == "__main__":
    cash_flows = [100000, 120000, 140000, 160000]  # Example cash flows over 4 years
    interest_rates = {'senior': 0.05, 'mezzanine': 0.10}
    
    model = DebtModel(cash_flows, interest_rates)
    optimal_structure = model.recommend_debt_structure()
    print("Optimal Debt Structure:", optimal_structure)