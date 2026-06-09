import math

def calculate_ai_project_cost(complexity, data_size_gb, team_size, development_time_months):
    """Calculates an estimated cost for an AI project based on several factors.

    This is a simplified model to illustrate cost drivers mentioned in the article.
    Actual costs can vary significantly.
    """

    # Base cost per month per team member (simplified average)
    base_developer_cost_per_month = 8000  # USD

    # Complexity multiplier (e.g., simple model vs. complex deep learning)
    # 1.0: Simple, 2.0: Medium, 3.0: Complex, 4.0: Very Complex
    complexity_multiplier = {
        "simple": 1.0,
        "medium": 2.0,
        "complex": 3.0,
        "very_complex": 4.0
    }.get(complexity.lower(), 2.0) # Default to medium if not found

    # Data processing cost factor (per GB, simplified)
    # Higher for messy or large datasets
    data_processing_cost_per_gb = 50 # USD

    # Infrastructure costs (cloud, hardware - simplified as a percentage of dev cost)
    infrastructure_percentage = 0.20 # 20% of development cost

    # --- Cost Calculation --- 

    # 1. Development Labor Cost
    total_developer_cost = team_size * development_time_months * base_developer_cost_per_month

    # 2. Data Processing Cost
    data_processing_cost = data_size_gb * data_processing_cost_per_gb

    # 3. Complexity Impact (applied to labor cost)
    # More complex projects often require more research, experimentation, and specialized skills.
    complexity_adjusted_labor_cost = total_developer_cost * complexity_multiplier

    # 4. Infrastructure Cost
    infrastructure_cost = complexity_adjusted_labor_cost * infrastructure_percentage

    # Total Estimated Cost
    total_estimated_cost = complexity_adjusted_labor_cost + data_processing_cost + infrastructure_cost

    return {
        "development_labor_cost": round(complexity_adjusted_labor_cost, 2),
        "data_processing_cost": round(data_processing_cost, 2),
        "infrastructure_cost": round(infrastructure_cost, 2),
        "total_estimated_cost": round(total_estimated_cost, 2)
    }

if __name__ == "__main__":
    print("--- AI Project Cost Estimator ---")
    print("This is a simplified model based on factors like complexity, data size, team size, and development time.")
    print("\nExample Scenarios:\n")

    # Scenario 1: Small KOBİ, simple project
    cost1 = calculate_ai_project_cost(
        complexity="simple",
        data_size_gb=50,
        team_size=2,
        development_time_months=3
    )
    print("Scenario 1 (KOBİ, Simple Project):")
    print(f"  Complexity: simple, Data: 50GB, Team: 2, Time: 3 months")
    print(f"  Estimated Cost: ${cost1['total_estimated_cost']:,}")
    print("  (Includes: Labor, Data Processing, Infrastructure)")

    # Scenario 2: Medium business, medium complexity
    cost2 = calculate_ai_project_cost(
        complexity="medium",
        data_size_gb=500,
        team_size=4,
        development_time_months=6
    )
    print("\nScenario 2 (Medium Business, Medium Complexity):")
    print(f"  Complexity: medium, Data: 500GB, Team: 4, Time: 6 months")
    print(f"  Estimated Cost: ${cost2['total_estimated_cost']:,}")

    # Scenario 3: Large enterprise, complex project
    cost3 = calculate_ai_project_cost(
        complexity="complex",
        data_size_gb=5000,
        team_size=8,
        development_time_months=12
    )
    print("\nScenario 3 (Large Enterprise, Complex Project):")
    print(f"  Complexity: complex, Data: 5000GB, Team: 8, Time: 12 months")
    print(f"  Estimated Cost: ${cost3['total_estimated_cost']:,}")

    print("\nNote: These are illustrative estimates. Real-world costs depend on many more variables.")
