"""Given an integer x, return true if x is palindrome integer."""

def palindrome(x:int):
	if x <= 0: return False

	div = 1
	while (x >= 10 * div):
		div *= 10
		
	while x != 0:
		if x // div != x % 10: return False
		x = int((x % div) // 10)
		div = div / 100
	return True

x = 122221
if palindrome(x) == True:
	print("Palendrome")
else:
	print("Not a Palindrome")


 def isPalindrome(self, x: int) -> bool:
        if x <= 0: return False

        div = 1
        while x >= 10 * div:
            div *= 10

        while x:
            if x // div != x % 10: return False
            x = int((x % div) // 10)
            div = div / 100
        return True

		


def isPalindrome(x):
		rev = 0
		init_n = x
		if( x < 0):
			return False
		while x != 0:
				rev = (rev*10) +  x % 10
				x = x // 10

		if(rev == init_n):
			return True
		return False

v=12231
print(isPalindrome(v))
