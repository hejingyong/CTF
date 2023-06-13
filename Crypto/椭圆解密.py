# -*- coding: utf-8 -*-
def txt(istr):
	return int(istr.encode("hex"),16)
x1 = txt("Marvin is")
y1 = 71164450240897430648972143714791734771985061339722673162401654668605658194656
y2 = 12951693517100633909800921421096074083332346613461419370069191654560064909824
p = 0xA9FB57DBA1EEA9BC3E660A909D838D726E3BF623D52620282013481D1F6E5377
A = 0x7D5A0975FC2C3057EEF67530417AFFE7FB8055C126DC5C6CE94A4B44F330B5D9
B = 0x26DC5C6CE94A4B44F330B5D9BBD77CBF958416295CF7E1CE6BCCDC18FF8C07B6

# from: http://eli.thegreenplace.net/2009/03/07/computing-modular-square-roots-in-python/
def modular_sqrt(a, p):
	"""
	求解二次同余： x^2 = a (mod p)
    返回解：x、p-x或者为0
	使用的求解算法：Tonelli-Shanks algorithm
	"""
	# 简易情况：
	#
	if legendre_symbol(a, p) != 1:
		return 0
	elif a == 0:
		return 0
	elif p == 2:
		return p
	elif p % 4 == 3:
		return pow(a, (p + 1) / 4, p)

	# Partition p-1 to s * 2^e for an odd s (i.e.
	# reduce all the powers of 2 from p-1)
	#
	s = p - 1
	e = 0
	while s % 2 == 0:
		s /= 2
		e += 1

	# Find some 'n' with a legendre symbol n|p = -1.
	# Shouldn't take long.
	#
	n = 2
	while legendre_symbol(n, p) != -1:
		n += 1

	# information
	#

	# x is a guess of the square root that gets better
	# with each iteration.
	# b is the "fudge factor" - by how much we're off
	# with the guess. The invariant x^2 = ab (mod p)
	# is maintained throughout the loop.
	# g is used for successive powers of n to update
	# both a and b
	# r is the exponent - decreases with each update
	#
	x = pow(a, (s + 1) / 2, p)
	b = pow(a, s, p)
	g = pow(n, s, p)
	r = e

	while True:
		t = b
		m = 0
		for m in xrange(r):
			if t == 1:
				break
			t = pow(t, 2, p)

		if m == 0:
			return x

		gs = pow(g, 2 ** (r - m - 1), p)
		g = (gs * gs) % p
		x = (x * gs) % p
		b = (b * g) % p
		r = m

# from: http://stackoverflow.com/a/9758173
def legendre_symbol(a, p):
	#求（a，p）的勒让德符号
	ls = pow(a, (p - 1) / 2, p)
	return -1 if ls == p - 1 else ls


def egcd(a, b):
    #求解欧几里得算法逆过程：
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

def modinv(a, m):
    #调用欧几里得算法得到逆过程方程参数
	g, x, y = egcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m

def gety(x):
    #求解y、y2
	y = modular_sqrt(x**3 + A * x + B, p) % p
	y2 = -y % p
	return y,y2

def hextotext(nbr):
    #hex转化成string
	s = hex(nbr)[2:-1]
	if len(s) % 2 ==1:
		s = "0"+s
	return s.decode("hex")


x1_inv = modinv(x1, p)
c1 = (y1 * x1_inv) % p
c2_1, c2_2 = gety(c1)

print repr(hextotext(y2*modinv(c2_2, p)  % p))
#https://blog.csdn.net/qq_40737798/article/details/88136230