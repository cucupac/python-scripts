def calculate_max_leverage(
    initial_collateral, comfortable_ltv, liquidation_ltv, initial_debt=0
):
    total_collateral = initial_collateral
    total_debt = initial_debt
    cycle = 0

    while True:
        max_borrowable = total_collateral * comfortable_ltv - total_debt

        # CONSTRAINT: NOT ALLOWING A BORROW LESS THAN $1
        if max_borrowable <= 1:
            break

        total_debt += max_borrowable
        total_collateral += max_borrowable
        cycle += 1

        print(
            f"Cycle {cycle}: Borrowing ${max_borrowable:.2f}, Total Collateral after: ${total_collateral:.2f}, Total Debt after: ${total_debt:.2f}"
        )

    leverage_ratio = total_collateral / initial_collateral
    final_ltv_ratio = total_debt / total_collateral
    debt_liquidation = total_collateral * liquidation_ltv
    debt_rise_percent = ((debt_liquidation - total_debt) / total_debt) * 100

    print(
        f"Maximum leverage reached at cycle {cycle} with total collateral of ${total_collateral:.2f} and total debt of ${total_debt:.2f}."
    )
    print(f"Leverage Ratio: {leverage_ratio:.2f}x")
    print(f"Final LTV Ratio: {final_ltv_ratio:.2f}")
    print(f"Debt Liquidation at: ${debt_liquidation:.2f}")
    print(f"Debt must rise by: {debt_rise_percent:.2f}% to reach liquidation.")


# Example usage
initial_collateral = 100  # Starting with $100 USDC as collateral
comfortable_ltv = 0.5  # Comfortable LTV
liquidation_ltv = 0.78  # Liquidation LTV

calculate_max_leverage(initial_collateral, comfortable_ltv, liquidation_ltv)
