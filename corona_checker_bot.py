def corona_checker_bot(symptoms):

	list_of_symps_org=['medium temperature(95.9–99.5 °F)','shortness_of_breath',
				'aches_and_pains','sore_throat','diarrhoea','nausea','runny_nose',
				'Persistent_pain or pressure in the chest']


	corona_symptoms=['cough','fever','tiredness','difficulty breathing','Bluish lips or face']
	danger_symps=['I have traveled recently during the last 14 days','I have a travel history in COVID-19 infected area','I have direct contact or is taking care of a positive COVID-19 patient','Sneezing frequency(High)']

	corona_checker=0
	for i in symptoms:
		if i in corona_symptoms:
			corona_checker+=2

	symp_checker=0
	for j in symptoms:
		if j in list_of_symps_org:
			symp_checker+=1


	danger_checker=0
	for k in symptoms:
		if k in danger_symps:
			danger_checker+=3

	final_corona=corona_checker+danger_checker+symp_checker

	return final_corona
















