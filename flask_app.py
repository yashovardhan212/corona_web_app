from reg import regf
from flask import Flask
from flask import request
from corona_checker_bot import corona_checker_bot
from rule import rule
from search import search
from otpsend import otp_sender


app = Flask(__name__)
app.config["DEBUG"]=True
@app.route('/',methods=["GET","POST"])

def login():

	errors=""
	if request.method=="POST":
		name=None
		age=None
		email=None
		country=None
		state=None
		city=None
		password=None
		cough=None
		fever=None

		try:
			name = str(request.form["name"])
		except:
			name=None
		try:
			age = int(request.form["age"])
		except:
			age=None
		try:
			email = str(request.form["email"])
		except:
			email=None
		try:
			country = str(request.form["country"])
		except:
			country=None
		try:
			state = str(request.form["state"])
		except:
			state=None
		try:
			city = str(request.form["city"])
		except:
			city=None
		try:
			password=str(request.form["password"])
		except:
			password=None
		try:
			cough=request.form["1"]
		except:
			cough=None
		try:
			fever=request.form["2"]
		except:
			fever=None
		try:
			tiredness=request.form["3"]
		except:
			tiredness=None
		try:
			medium_temperature=request.form["4"]
		except:
			medium_temperature=None
		try:
			low_temperature=request.form["5"]
		except:
			low_temperature=None
		try:
			difficulty_breathing=request.form["6"]
		except:
			difficulty_breathing=None
		try:
			shortness_of_breath=request.form["7"]
		except:
			shortness_of_breath=None
		try:
			aches_and_pains=request.form["8"]
		except:
			aches_and_pains=None
		try:
			sore_throat=request.form["9"]
		except:
			sore_throat=None
		try:
			diarrhoea=request.form["10"]
		except:
			diarrhoea=None
		try:
			nausea=request.form["11"]
		except:
			nausea=None
		try:
			runny_nose=request.form["12"]
		except:
			runny_nose=None
		try:
			Persistent_pain_or_pressure_in_the_chest=request.form["13"]
		except:
			Persistent_pain_or_pressure_in_the_chest=None
		try:
			Bluish_lips_or_face=request.form["14"]

		except:
			Bluish_lips_or_face=None
		try:
			a=request.form["15"]

		except:
			a=None
		try:
			b=request.form["16"]

		except:
			b=None
		try:
			c=request.form["17"]

		except:
			c=None
		try:
			d=request.form["18"]

		except:
			d=None
		try:
			flnm=request.form["19"]
		except:
			flnm=None

		try:
			result=int(request.form["result"])
		except:
			result=0
		try:
			sea=request.form["search"]
		except:
			sea=None
		try:
			otp=int(request.form["otp"])
		except:
			otp=None
		try:
			magik_string=request.form["magik_string"]
		except:
			magik_string=None


		if name is not None and age is not None and email is not None and country is not None and state is not None and city is not None and password is not None and result is not None:




			otp_sender(email,age)
			email=email.replace(' ','_')
			name=name.replace(' ','_')
			country=country.replace(' ','_')
			state=state.replace(' ','_')
			city=city.replace(' ','_')
			password=password.replace(' ','_')


			magik_string='{name}:{age}:{email}:{country}:{state}:{city}:{password}:{result}'.format(name=name,age=age,email=email,country=country,state=state,city=city,password=password,result=result)





			return  '''
                <!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>

input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
}


input[type=submit] {
  background-color: #4CAF50;
  color: white;
}


.container {
  background-color: #f1f1f1;
  padding: 20px;
}


#message {
  display:none;
  background: #f1f1f1;
  color: #000;
  position: relative;
  padding: 20px;
  margin-top: 10px;
}

#message p {
  padding: 10px 35px;
  font-size: 18px;
}

</style>'''+'''
</head>
<body>

<h3>OTP VERIFICATION</h3>


<div class="container">
  <form action="." method="post">

    <label for="usrname">OTP</label>
    <input type="text" id="usrname" name="otp" required>


    <input name="magik_string" type="hidden" value={magik}>
    <input type="submit" value="Submit">
  </form>
</div>




</body>
</html>
            '''.format(magik=magik_string)



		elif otp is not None and magik_string is not None:
			magik_list=magik_string.split(':')
			if len(magik_list)==8:
				if int(otp)==int(int(magik_list[1])*2935):
					regf(str(magik_list[0].replace('_',' ')),str(magik_list[2].replace('_',' ')),magik_list[1],str(magik_list[3].replace('_',' ')),str(magik_list[4].replace('_',' ')),str(magik_list[5].replace('_',' ')),str(magik_list[6].replace('_',' ')),magik_list[7])
					magik_string=None
					return'''

<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: Arial, Helvetica, sans-serif;
  background-color: black;
}

* {
  box-sizing: border-box;
}

/* Add padding to containers */
.container {
  padding: 16px;
  background-color: white;
}

/* Full-width input fields */
input[type=text], input[type=password] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type=text]:focus, input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}

/* Overwrite default styles of hr */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

/* Set a style for the submit button */
.registerbtn {
  background-color: #4CAF50;
  color: white;
  padding: 16px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.5;
}

.registerbtn:hover {
  opacity: 1;
}

/* Add a blue text color to links */
a {
  color: dodgerblue;
}

/* Set a grey background color and center the text of the "sign in" section */
.signin {
  background-color: #f1f1f1;
  text-align: center;
}
</style>
</head>
<body>
<h2 STYLE="color:blue;text-align:center;opacity:20.9;">YOU ARE REGISTERED</h2>
<form method="post" action=".">
  <div class="container">
    <h1>Login</h1>

    <hr>
	<label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email" name="email" required>
    <label for="Password"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="password" required>

    <hr>

    <button type="submit" class="registerbtn">Login</button>
  </div>

  <div class="container signin">
    <p><a href="#">Forget Your Password</a></p>
  </div>
</form>




<form method="post" action=".">
  <div class="container">
    <h1>Register</h1>
    <p>Please fill in this form to create an account.</p>
    <hr>
	<label for="name"><b>Name</b></label>
    <input type="text" placeholder="Enter Name" name="name" required>
    <label for="Age"><b>Age</b></label>
    <input type="text" placeholder="Enter Age" name="age" required>
    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email" name="email" required>
	<label for="country"><b>Country</b></label>
    <input type="text" placeholder="Enter Your Country" name="country" required>
    <label for="State"><b>State</b></label>
    <input type="text" placeholder="Enter Your State" name="state" required>
    <label for="city"><b>City</b></label>
    <input type="text" placeholder="Enter Your City" name="city" required>
    <label for="password"><b>Password</b></label>
    <input type="password" placeholder="Enter Your Password" name="password" required>
    <input type="hidden" name="result" value="0">
    <hr>
    <p>By creating an account you agree to our <a href="#">Terms & Privacy</a>.</p>

    <button type="submit" class="registerbtn">Register</button>
  </div>


</form>



</body>
</html>









'''

				else:
					return'''<!DOCTYPE html>
<html>
<body>

<h2 style="text-align:center;">OTP IS INCORRECT</h2>
<img src="data:image/png;base64,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" alt="Trulli" width="100%" height="333">

</body>
</html>
'''


			else:
				return'''len of mk lt is {x} {y} '''.format(x=len(magik_list),y=magik_list[0])



		elif email is not None and password is not None:

			with open('data.txt','r') as f:
				for l in f:
					l=l.split(':')

					if email==l[0] and password==l[1]:
							data_base=l





							name=data_base[2]
							age=data_base[3]
							email=data_base[0]
							location=data_base[4]+' '+data_base[5]+' '+data_base[6]
							password=data_base[1]
							try:
								with open('status.txt','r') as ff:
									for ll in ff:
										ll=ll.split(':')
										if ll[0]==str(email)+str(password):
											status=int(ll[1])
							except:
								status=0
							rules=rule(status)
							rules=rules.split(':')
							try:
								rule0=rules[0]
							except:
								rule0=None
							try:
								rule1=rules[1]
							except:
								rule1=None
							try:
								rule2=rules[2]

							except:
								rule2=None
							try:
								rule3=rules[3]
							except:
								rule3=None
							try:
								rule4=rules[4]
							except:
								rule4=None
							try:
								rule5=rules[5]
							except:
								rule5=None
							try:
								rule6=rules[6]
							except:
								rule6=None
							try:
								rule7=rules[7]
							except:
								rule7=None
							return '''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<style>
* {box-sizing: border-box;}


}

.topnav {
  overflow: hidden;
  background-color: #e9e9e9;
}

.topnav a {
  float: left;
  display: block;
  color: black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #2196F3;
  color: white;
}

.topnav .search-container {
  float: right;
}

.topnav input[type=text] {
  padding: 6px;
  margin-top: 8px;
  font-size: 17px;
  border: none;
}

.topnav .search-container button {
  float: right;
  padding: 6px 10px;
  margin-top: 4px;
  margin-right: 12px;
  background: #ddd;
  font-size: 17px;
  border: none;
  cursor: pointer;
  width:10px;
}

.topnav .search-container button:hover {
  background: #ccc;
}

@media screen and (max-width: 500px) {
  .topnav .search-container {
    float: none;
  }
  .topnav a, .topnav input[type=text], .topnav .search-container button {
    float: none;

    text-align: left;
    width: 90%;
    margin: 0;
    padding: 14px;
  }
  .topnav input[type=text] {
    border: 1px solid #ccc;
  }
}



.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 100%;
  margin: auto;
  text-align: center;
  font-family: Georgia;
  background-image:url('https://cdn.pixabay.com/photo/2016/09/13/19/31/texture-1668079_960_720.jpg');
  width:100%;
  height:100%;
}

.title {
  color: grey;
  font-size: 18px;
}

button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 50px;
}
.buttonn {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 20px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
}
.button2 {
  background-color: #008CBA;
  color: black;
  border: 2px solid #008CBA;
  opacity: 0.7;
}

.button2:hover {
  background-color: #008CBA;
  color: white;
}



.but{
width:32px;
height:33px;
margin-top:7px;
}
.ccc{
width:85%;
}
a {
  text-decoration: none;
  font-size: 22px;
  color: white;
}

button:hover, a:hover {
  opacity: 0.7;
}
</style>





'''+'''
</head>
<body>




<form action="." method="post">
      <input type="text" placeholder="Search.." name="search" class="ccc">
      <button type="submit" class="but"><i class="fa fa-search"></i></button>
    </form>





<h2 style="text-align:center">CORONA STATUS</h2>

<div class="card">
  <img src="https://images.pexels.com/photos/3952232/pexels-photo-3952232.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" alt="John" style="width:100%;height:500px;">
  <h1>{name}</h1>
  <p class="title">Age {age}</p>
  <p> {location}</p>

 <p>Corona Status </p><meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">





<div class="w3-light-grey">
  <div class="w3-container w3-blue" style="width:{perct}%">Status </div>
</div><br>
<p>Score {perc}</p>
  <p><button>Contact {email}</button></p>
</div>
<form action="http://staysafe008.pythonanywhere.com/" method="post"><input name=userpass value="{email}:{password}" type="hidden"><button class="buttonn button2" type="submit">UPDATE STATUS</button></form>

<form action="." method="post" ><input type="hidden" name="email" value={email}>
<input type="hidden" name="password" value={password}>
<button  type="submit">Reload</button></form>
<div class="card">

<p >Score  0-2  Best</p>
<p >Score  3-5  Good</p>
<p >Score  6-10 Follow the rules</p>
<p >Score  11-30  Danger</p>

  <p >{rule1}</p><br>
  <p >{rule2}</p><br>
  <p >{rule3}</p><br>
  <p >{rule4}</p><br>
  <p >{rule5}</p><br>
  <p >{rule6}</p><br>
  <p >{rule7}</p><br>
    <p >{rule8}</p><br>
<p><button></button></p>
<script src='https://kit.fontawesome.com/a076d05399.js'></script>
<form action="#">

<button type="submit" style='font-size:24px;width:100%;'>Donate <i class='fas fa-dollar-sign'></i></button>

</form>
</div>



</body>
</html>'''.format(name=name,age=age,location=location,status=status,email=email,password=password,perc=status,rule1=rule0,rule2=rule1,rule3=rule2,rule4=rule3,rule5=rule4,rule6=rule5,rule7=rule6,rule8=rule7,perct=(status*100)/30)


		elif flnm is not None:

			list_of_symps=[cough,fever,tiredness,medium_temperature,low_temperature,difficulty_breathing,shortness_of_breath,
				aches_and_pains,sore_throat,diarrhoea,nausea,runny_nose,
				Persistent_pain_or_pressure_in_the_chest,Bluish_lips_or_face,a,b,c,d]
			list_of_symps_org=['cough','fever','tiredness','medium temperature(95.9–99.5 °F)','low temperature(<95 °F)','difficulty breathing','shortness_of_breath',
				'aches and pains','sore throat','diarrhoea','nausea','runny_nose',
				'Persistent pain or pressure in the chest','Bluish lips or face','I have traveled recently during the last 14 days'
					,'I have a travel history in COVID-19 infected area','I have direct contact or is taking care of a positive COVID-19 patient'
					,'Sneezing frequency(High)']
			tempstring=''
			for i in range(len(list_of_symps)):
				if list_of_symps[i] is not None:
					tempstring+=str(list_of_symps_org[i])+':'
				else:
					continue
			tempstring=tempstring.split(':')
			result=corona_checker_bot(tempstring)
			with open("status.txt","r") as gile:
				user_data=gile.readlines()
				for i in range(len(user_data)):
					if user_data[i].split(':')[0]==str(flnm).replace(':',''):
						user_data[i]=str(flnm).replace(':','')+':'+str(result)+'\n'
			with open("status.txt","w") as writeg:
			    for line in user_data:
			        writeg.write(line)
			flnm=flnm.split(':')
			email=flnm[0]
			password=flnm[1]
			return '''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body, html {
  height: 100%;
  font-family: Arial, Helvetica, sans-serif;
}

* {
  box-sizing: border-box;
}

.bg-img {
  /* The image used */
  background-image: url("https://images.unsplash.com/photo-1558591710-4b4a1ae0f04d?ixlib=rb-1.2.1&w=1000&q=80");

  height: 100%;
  width:100%;

  /* Center and scale the image nicely */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative;
}

/* Add styles to the form container */
.container {
  position:absolute;
  right: 0;

  margin-top:50px;
  width: 100%;
  padding: 16px;
  height:220px;
  background-color: white;

}
/* Full-width input fields */
input[type=text], input[type=password] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  border: none;
  background: #f1f1f1;
}

input[type=text]:focus, input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}

/* Set a style for the submit button */
.btn {
  background-color: red;
  color: white;
  padding: 16px 20px;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.8;
}

.btn:hover {
  opacity: 1;
}
</style>'''+'''
</head>
<body>


<div class="bg-img">
  <form action="." method="post"class="container">
    <h1 style="text-align:center;color:dark;">YOUR STATUS HAS BEEN UPDATED</h1>


    <input type="hidden"  name="email" value={email}>


    <input type="hidden"  name="password" value={password}>

    <button type="submit" class="btn">home</button>
  </form>
</div>



</body>
</html>
'''.format(email=email,password=password)


		elif sea is not None:
			magik_string=search(sea)

			if magik_string:
				return magik_string
			else:
				return '''<!DOCTYPE html>
<html>
<body>


<figure>
  <img src="https://cdn.dribbble.com/users/283708/screenshots/7084440/media/6cd8b29540bcfb6a7693c27f58db7b56.png" alt="Trulli" style="width:100%">
  <figcaption><b style="text-align:center;">OUR SEARCH RESULTS ARE CASE SENSITIVE.</b></figcaption>
</figure>

</body>
</html>
'''






		errors+="Login Failed"
	return '''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: Arial, Helvetica, sans-serif;
  background-image: url('https://cdn.pixabay.com/photo/2016/09/13/19/31/texture-1668079_960_720.jpg');
}

* {
  box-sizing: border-box;
}

/* Add padding to containers */
.container {
  padding: 16px;
  background-color: white;
}

/* Full-width input fields */
input[type=text], input[type=password] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type=text]:focus, input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}

/* Overwrite default styles of hr */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

/* Set a style for the submit button */
.registerbtn {
  background-color: red;
  color: white;
  padding: 16px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.5;
}

.registerbtn:hover {
  opacity: 1;
}

/* Add a blue text color to links */
a {
  color: dodgerblue;
}

/* Set a grey background color and center the text of the "sign in" section */
.signin {
  background-color: #f1f1f1;
  text-align: center;
}
</style>
</head>
<body>

<form method="post" action=".">
  <div class="container">
    <h1>Login</h1>

    <hr>
	<label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email" name="email" required>
    <label for="Password"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="password" required>

    <hr>

    <button type="submit" class="registerbtn">Login</button>
  </div>

  <div class="container signin">

  </div>
</form>




<form method="post" action=".">
  <div class="container">
    <h1>Register</h1>
    <p>Please fill in this form to create an account.</p>
    <hr>
	<label for="name"><b>Name</b></label>
    <input type="text" placeholder="Enter Name" name="name" required>
    <label for="Age"><b>Age</b></label>
    <input type="text" placeholder="Enter Age" name="age" required>
    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email" name="email" required>
	<label for="country"><b>Country</b></label>
    <input type="text" placeholder="Enter Your Country" name="country" required>
    <label for="State"><b>State</b></label>
    <input type="text" placeholder="Enter Your State" name="state" required>
    <label for="city"><b>City</b></label>
    <input type="text" placeholder="Enter Your City" name="city" required>
    <label for="password"><b>Password</b></label>
    <input type="password" placeholder="Enter Your Password" name="password" required>
    <input type="hidden" name="result" value="0">
    <hr>
    <p>By creating an account you agree to our <a href="#">Terms & Privacy</a>.</p>

    <button type="submit" class="registerbtn">Register</button>
  </div>


</form>



</body>
</html>'''




