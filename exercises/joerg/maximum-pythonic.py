import sys


# POTSCHERT:
# ----------

# zahlen_strings = sys.argv[1:]
# zahlen = []
# for element in zahlen_strings:
#     zahlen.append(int(element))
# 
# print(max(zahlen))


# BISSL WENIGER POTSCHERT (weil noch immer zu viele zeilen, naemlich DREI!!!):
# ----------------------------------------------------------------------------

# zahlen_strings = sys.argv[1:]
# 
# # zahlen = []
# # for element in zahlen_strings:
# #     zahlen.append(int(element))
# 
# # simpler: list comprehension
# zahlen = [int(element) for element in zahlen_strings]
# 
# print(max(zahlen))


# ULTIMATE PYTHONICITY!!!!!!
# --------------------------

print(max(  [int(element) for element in sys.argv[1:]]  ))
