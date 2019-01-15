#Program for string count
s="Nanna ooru mysuru nimma ooru yavudhu"
l=s.split(' ')
d={k:l.count(k) for k in l }
print(d)