"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 1-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $44B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
"""

#from idlelib.config import InvalidConfigSet

### all your code below ###
#Equation: final = principal * ((1 + (rate)) ** n)

P= 33 * (10 ** 9)
Rten=.0396
Rtwen=.0432
Nten=10
Ntwen=20

ten_year_final=(P * ((1 + Rten) ** Nten))
print("The 10 year investment would be worth "+str(ten_year_final))

twenty_year_final=P*((1+Rtwen)**Ntwen)
print("The 20 year investment would be worth "+str(twenty_year_final))