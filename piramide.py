# Pyramid
print("\nNormal Pyramid")
for i in range(5):
    k='* '
    k=k*i
    print(f'{k: ^10}')
# Invert Pyramid
print("\nInvert Pyramid")
for i in range(5):
    x='* '
    x = x*(5-i)
    print(f'{x: ^10}')
# Left sided Pyramid
print("\nLeft sided Pyramid")
for i in range(5):
    a='* '
    a=a*i
    print(f'{a: <10}')
# Right sided Pyramid
print("\nRight sided Pyramid")
for i in range(5):
    s='* '
    s=s*i
    print(f'{s: >10}')