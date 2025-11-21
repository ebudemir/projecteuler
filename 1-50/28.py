# We are asked: find the sum of the numbers on the diagonals in a 1001 by 1001 spiral.
#
# Let the side length be 1001 (odd). Then
#
# M = (1001 - 1) / 2 = 500
#
# Each “layer” of the spiral contributes four corner numbers. For layer m, the corners are:
#
# (2m+1)², (2m+1)² - 2m, (2m+1)² - 4m, (2m+1)² - 6m
#
# Sum of corners = 4(2m+1)² - 12m
#
# Expanding:
#
# 4(4m² + 4m + 1) - 12m = 16m² + 4m + 4
#
# The total sum of diagonals is:
#
# S(1001) = 1 + sum_{m=1}^{500} (16m² + 4m + 4)
#
# Here, 1 is the center of the spiral.
#
# Split the sum:
#
# sum_{m=1}^{500} (16m² + 4m + 4) = 16 * sum_{m=1}^{500} m² + 4 * sum_{m=1}^{500} m + 4 * sum_{m=1}^{500} 1
#
# Use formulas:
#
# sum_{m=1}^{M} m² = M(M+1)(2M+1)/6 = 500 * 501 * 1001 / 6 = 41858500
# sum_{m=1}^{M} m = M(M+1)/2 = 500 * 501 / 2 = 125250
# sum_{m=1}^{M} 1 = 500
#
# Multiply coefficients:
#
# 16 * 41858500 = 669736000
# 4 * 125250 = 501000
# 4 * 500 = 2000
#
# Add center 1:
#
# S(1001) = 1 + 669736000 + 501000 + 2000 = 669171001
#
# Answer: 669171001
