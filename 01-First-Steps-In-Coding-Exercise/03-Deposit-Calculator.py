deposit_sum = float(input())
deposit_term = int(input())
annual_interest_rate = float(input())

annual_interest_rate_as_percent = annual_interest_rate / 100
final_sum = deposit_sum + deposit_term * ((deposit_sum * annual_interest_rate_as_percent)/12)

print(final_sum)
