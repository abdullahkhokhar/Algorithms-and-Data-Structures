# A self-dividing number is a number that is divisible by every digit it contains.
#
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
#
# Also, a self-dividing number is not allowed to contain the digit zero.
#
# Given a lower and upper number bound, output a list of every possible self
#  dividing number, including the bounds if possible.

class Solution:
	def selfDividingNumbers(self, left: int, right: int) -> List[int]:
		result = []
		for i in range(left, right + 1):
			count = 0
			string_num = str(i)     #get all digits
			length = len(string_num)
			for digit in string_num:
				if int(digit) != 0 and i % int(digit) == 0:     # verify digit
					count += 1
				else:
					break       # not self dividing

			if count == length:
				result.append(i)        #  all digits where checked

		return result
