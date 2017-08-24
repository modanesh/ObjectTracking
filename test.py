import re



a = re.findall(r'\d+', 'he1llo1 42 I\'m a 32 string 30')

print(a)

aa = [int(s) for s in re.findall(r'\d+', 'array[(98')]

print(aa)
