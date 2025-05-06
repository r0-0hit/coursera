# def calculate_monthly_payment(
#     principal: float, interest_rate: float, loan_term_years: int
# ) -> float:
#     """
#     Calculates the monthly payment for a fixed-rate loan.

#     Args:
#         principal: The total amount borrowed (float).
#         interest_rate: The annual interest rate (as a decimal, float).
#         loan_term_years: The loan term in years (int).

#     Returns:
#         The monthly payment amount (float).

#     Raises:
#         ValueError: If any of the inputs are negative or zero.

#     Example:
#         >>> calculate_monthly_payment(100000, 0.05, 30)
#         530.33
#     """
#     if principal <= 0 or interest_rate <= 0 or loan_term_years <= 0:
#         raise ValueError("All input values must be positive.")

#     monthly_interest_rate = interest_rate / 12
#     number_of_payments = loan_term_years * 12

#     # Calculation logic for monthly payment (omitted for brevity)

#     return monthly_payment


# * Example of a good function


def calculate_diameter_circle(radius: float) -> float:
    """The function calculates the Diameter.
    Args:
        radius: radius of the circle (float).

    Returns:
        The diameter of the circle (float).

    Raises:
        ValueError: If the input radius is negative the function will return -1.

    Example:
        >>> calculate_diameter_circle(2.5)
        5.0
    """

    """
    Calculate the diameter of a circle given its radius.

    Args:
        radius (float): The radius of the circle. Must be a non-negative number.

    Returns:
        float: The diameter of the circle (radius * 2). 
               Returns -1.0 if the input radius is negative to indicate an error.
    """

    if radius < 0:
        return -1.0

    diameter = radius * 2
    return diameter


print(calculate_diameter_circle(7))
print(calculate_diameter_circle(2.5))
print(calculate_diameter_circle(0))
print(calculate_diameter_circle(-3))
print(calculate_diameter_circle(1000000))
