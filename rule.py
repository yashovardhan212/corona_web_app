def rule(score):

	if score==0:
		string="Stay home from work, school and public areas if you're sick unless you're going to get medical care:Avoid contact with live animals and surfaces they may have touched if you're visiting live markets in areas that have recently had new coronavirus cases:Avoid eating raw or undercooked meat or animal organs:Avoid taking public transportation:Avoid large events and mass gatherings."
	if score in range(1,3):
		string="May be stress related and Observe:Stay home from work, school and public areas if you're sick unless you're going to get medical care:Avoid contact with live animals and surfaces they may have touched if you're visiting live markets in areas that have recently had new coronavirus cases:Avoid eating raw or undercooked meat or animal organs:Avoid taking public transportation:Avoid large events and mass gatherings."

	if score in range(3,5):
		string="Hydrate properly and proper personal hygiene:Consult with a Doctor if you want.:Stay home from work, school and public areas if you're sick, unless you're going to get medical care:Avoid contact with live animals and surfaces they may have touched if you're visiting live markets in areas that have recently had new coronavirus cases.:Avoid eating raw or undercooked meat or animal organs:Avoid taking public transportation:Avoid large events and mass gatherings."

	if score in range(5,11):
		string="You should consult with a doctor:Avoid large events and mass gatherings.:Avoid close contact (about 6 feet) with everyone:Wash your hands often with soap and water for at least 20 seconds, or use an alcohol-based hand sanitizer that contains at least 60% alcohol.:Avoid touching your eyes, nose and mouth if your hands aren't clean.:Avoid taking public transportation:Avoid eating raw or undercooked meat or animal organs:Avoid contact with live animals and surfaces they may have touched if you're visiting live markets in areas that have recently had new coronavirus cases.:Stay home from work, school and public areas if you're sick, unless you're going to get medical care"

	if score in range(11,31):
		string="Call the DOH Hotline 02-8-651-7800:Avoid large events and mass gatherings.:Avoid close contact (about 6 feet) with everyone:Wash your hands often with soap and water for at least 20 seconds, or use an alcohol-based hand sanitizer that contains at least 60% alcohol.:Avoid touching your eyes, nose and mouth if your hands aren't clean.:Avoid taking public transportation:Avoid eating raw or undercooked meat or animal organs:Avoid contact with live animals and surfaces they may have touched if you're visiting live markets in areas that have recently had new coronavirus cases.:Stay home from work, school and public areas if you're sick, unless you're going to get medical care"


	return string
