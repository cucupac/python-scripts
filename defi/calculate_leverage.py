def calculate_max_leverage(initial_collateral, ltv_ratio, initial_debt=0):
    total_collateral = initial_collateral
    total_debt = initial_debt
    cycle = 0

    while True:
        max_borrowable = total_collateral * ltv_ratio - total_debt

        # CONSTRAINT: NOT ALLOWING A BORROW LESS THAN $1
        if max_borrowable <= 1:
            break

        total_debt += max_borrowable
        total_collateral += max_borrowable
        cycle += 1

        print(
            f"Cycle {cycle}: Borrowing ${max_borrowable:.2f}, Total Collateral after: ${total_collateral:.2f}, Total Debt after: ${total_debt:.2f}"
        )

    # Leverage Ratio Calculation: Leverage is a measure of how much your initial investment is magnified.
    # It is calculated as the total collateral controlled by the protocol divided by the initial collateral.
    # This indicates how much the protocol has amplified the initial investment through borrowing.
    leverage_ratio = total_collateral / initial_collateral
    final_ltv_ratio = total_debt / total_collateral
    print(
        f"Maximum leverage reached at cycle {cycle} with total collateral of ${total_collateral:.2f} and total debt of ${total_debt:.2f}."
    )
    print(f"Leverage Ratio: {leverage_ratio:.2f}x")
    print(f"Final LTV Ratio: {final_ltv_ratio:.2f}")


# Example usage
initial_collateral = 100  # Starting with $100 USDC as collateral
ltv_ratio = 0.9  # 80% LTV

calculate_max_leverage(initial_collateral, ltv_ratio)
