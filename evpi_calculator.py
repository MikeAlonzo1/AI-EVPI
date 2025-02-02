import matplotlib.pyplot as plt
import pandas as pd

# Function to calculate the expected value of each decision
def calculate_expected_value(probabilities, payoffs):
    return sum(p * payoff for p, payoff in zip(probabilities, payoffs))

# Function to calculate the EVPI
def calculate_evpi(no_ai_probabilities, no_ai_payoffs, ai_probabilities, ai_payoffs):
    expected_value_no_ai = calculate_expected_value(no_ai_probabilities, no_ai_payoffs)
    expected_value_ai = calculate_expected_value(ai_probabilities, ai_payoffs)
    return expected_value_no_ai - expected_value_ai

# Function to perform sensitivity analysis
def sensitivity_analysis(no_ai_probabilities, no_ai_payoffs, ai_probabilities, ai_payoffs, parameter_range):
    evpi_values = []
    for p in parameter_range:
        adjusted_no_ai_probabilities = [p, 1 - p]
        adjusted_ai_probabilities = [p + 0.2, 1 - (p + 0.2)]  # Example adjustment
        evpi = calculate_evpi(adjusted_no_ai_probabilities, no_ai_payoffs, adjusted_ai_probabilities, ai_payoffs)
        evpi_values.append(evpi)
    return evpi_values

# Function to visualize results
def visualize_results(parameter_range, evpi_values):
    plt.plot(parameter_range, evpi_values, marker='o', color='b', label='EVPI')
    plt.axhline(0, color='r', linestyle='--', label='Break-even')
    plt.xlabel('Probability of Success (No AI)')
    plt.ylabel('EVPI ($)')
    plt.title('Sensitivity Analysis of EVPI')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to calculate risk metrics
def calculate_risk_metrics(no_ai_probabilities, no_ai_payoffs, ai_probabilities, ai_payoffs):
    # Worst-case and best-case scenarios
    worst_case_no_ai = min(no_ai_payoffs)
    best_case_no_ai = max(no_ai_payoffs)
    worst_case_ai = min(ai_payoffs)
    best_case_ai = max(ai_payoffs)

    return {
        "Worst Case (No AI)": worst_case_no_ai,
        "Best Case (No AI)": best_case_no_ai,
        "Worst Case (AI)": worst_case_ai,
        "Best Case (AI)": best_case_ai,
    }

# Main function
def main():
    print("Welcome to the Enhanced EVPI Calculator for Tech and Finance Businesses!")
    print("This tool helps you evaluate the value of implementing AI in your operations.\n")

    # User inputs
    no_ai_probabilities = [float(x) for x in input("Enter probabilities for Not Using AI (comma-separated, e.g., 0.6,0.4): ").split(",")]
    no_ai_payoffs = [float(x) for x in input("Enter payoffs for Not Using AI (comma-separated, e.g., 100000,-50000): ").split(",")]
    ai_probabilities = [float(x) for x in input("Enter probabilities for Using AI (comma-separated, e.g., 0.8,0.2): ").split(",")]
    ai_payoffs = [float(x) for x in input("Enter payoffs for Using AI (comma-separated, e.g., 150000,-30000): ").split(",")]

    # Calculate EVPI
    evpi = calculate_evpi(no_ai_probabilities, no_ai_payoffs, ai_probabilities, ai_payoffs)
    print(f"\nEVPI (Expected Value of Perfect Information) of using AI vs not using AI: ${evpi:,.2f}")

    # Risk metrics
    risk_metrics = calculate_risk_metrics(no_ai_probabilities, no_ai_payoffs, ai_probabilities, ai_payoffs)
    print("\nRisk Metrics:")
    for metric, value in risk_metrics.items():
        print(f"{metric}: ${value:,.2f}")

    # Sensitivity analysis
    parameter_range = [i * 0.1 for i in range(6, 10)]  # Vary probability of success from 0.6 to 0.9
    evpi_values = sensitivity_analysis(no_ai_probabilities, no_ai_payoffs, ai_probabilities, ai_payoffs, parameter_range)
    visualize_results(parameter_range, evpi_values)

    # Export results to CSV
    results = {
        "EVPI": evpi,
        **risk_metrics,
    }
    results_df = pd.DataFrame(list(results.items()), columns=["Metric", "Value"])
    results_df.to_csv("evpi_results.csv", index=False)
    print("\nResults exported to 'evpi_results.csv'.")

if __name__ == "__main__":
    main()
