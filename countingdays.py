# author: cactapus

years = range(1900, 2015)
months = range(1, 13)
count = 0

for year in years:
	for month in months:
		days = range(1, 32)
		if month == 4 or month == 6 or month == 9 or month == 11:
			days = range(1, 31)
		if month == 2:
			if year % 400 == 0:
				days = range(1, 30)
			elif year % 100 == 0:
				days =  range(1, 29)
			elif year % 4 == 0:
				days = range(1, 30)
			else:
				days = range(1, 29)
				
				
				
		
		
		for day in days:
			count = count + 1
			
			
	
print count
	
	