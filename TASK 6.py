a=['$876,001', '$543,903', '$2453,896']
l1=len(a)
print(a)
for i in range(0,l1):
    l = len(a[i])
    a[i] = a[i].lstrip('$')
    a[i] = a[i].replace(',', '')
print(a)