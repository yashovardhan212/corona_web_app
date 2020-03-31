def regf(name,email,age,country,state,city,password,result):

	with open("data.txt",'a') as g:
		g.write(str(email)+':'+str(password)+':'+str(name)+':'+str(age)+':'+str(country)+':'+str(state)+':'+str(city)+'\n')


	with open("status.txt",'a') as f:
		f.write(str(email)+str(password)+':'+str(result)+'\n')

