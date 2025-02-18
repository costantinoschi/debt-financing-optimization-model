# Debt Financing Optimization Model

This project provides a tool to optimize the capital structure for portfolio companies by analyzing various debt instruments and simulating financial outcomes.

## Features
- Analysis of different debt instruments (e.g., senior debt, mezzanine financing)
- Simulation of interest coverage ratios and debt service capabilities
- Recommendations for optimal debt levels based on cash flow projections

## Project Structure
- **src/debt_model.py**: Core Python code for the debt optimization model.
- **data/**: Directory for any data files (if used).
- **README.md**: This documentation file.
- **requirements.txt**: List of Python dependencies.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/costantinoschi/debt-financing-optimization-model.git
   cd debt-financing-optimization

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt


## Usage
Run the model with:

```bash
python src/debt_model.py
```


## Tech Stack
- **Python** for core logic and optimization
- **Numpy** for numerical computations
- **Pandas** for data manipulation
- **Scipy** for optimization algorithms

## Example Output

Upon running the script, you will see an output file like:

Optimal Debt Structure: 
       
     {'senior': 1234567.89, 'mezzanine': 987654.32}

   (The numbers are illustrative and will vary based on your inputs)

## Customization
Modify `cash_flows` and `interest_rate`s in `debt_model.py` to reflect your specific scenario.
Add more debt types or constraints by extending the `DebtModel` class.
