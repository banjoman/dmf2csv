headers = 'first_name,last_name,middle_initial,birth_month,birth_day,birth_year,death_month,death_day,death_year,social_security_number,verified_or_proven'

ingest = ['ssdm1', 'ssdm2', 'ssdm3']

with open('dmf.csv', 'w') as outfile:

	outfile.writelines(headers)
	outfile.writelines('\n')

	for file in ingest:
		print('Currently processing:', file)
		with open(file, 'r', encoding = "ISO-8859-1") as infile:
			line = infile.readline()
			while line:
				outfile.writelines(line[34:49].strip()) # first name
				outfile.writelines(',')
				outfile.writelines((' ').join(line[10:34].split())) # last name
				outfile.writelines(',')
				outfile.writelines(line[50:64].strip()) # middle initial
				outfile.writelines(',')
				outfile.writelines(line[73:75]) # birth_month
				outfile.writelines(',')
				outfile.writelines(line[75:77]) # birth_day
				outfile.writelines(',')
				outfile.writelines(line[77:81]) # birth year
				outfile.writelines(',')
				outfile.writelines(line[65:67]) # death_month
				outfile.writelines(',')
				if line[67:69] != '00':
					outfile.writelines(line[67:69]) # death_day
				outfile.writelines(',')
				outfile.writelines(line[69:73]) # death_year
				outfile.writelines(',')
				outfile.writelines(line[1:10]) # ssn
				outfile.writelines(',')
				outfile.writelines(line[64]) # verified or proven
				outfile.writelines('\n')

				line = infile.readline()	