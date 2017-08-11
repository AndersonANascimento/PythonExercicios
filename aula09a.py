#        012345678901234567890
frase = 'Curso em Video Python'

print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print(frase.lower().find('python'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.split())
print('-'.join(frase.split()))

frase = '   Aprenda Python  '
print(frase)
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

print('''
asfalfçlaaldfa
dfalfdasdf
adsflkalsdkf
adlfkasdkfl lakf laksdfl kasldf kalsdk fas
''')