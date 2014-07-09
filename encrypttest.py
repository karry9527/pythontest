__author__ = 'kkk'
import encrypt

e = encrypt.Encrypt()
e.setCode()
print()
print(e.getCode())
print(e.toEncode())
print(e.toDecode())
print()