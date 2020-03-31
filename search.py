def search(name):
	return_string=''

	code_string1='''<!DOCTYPE html>
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
</style>'''
	code_string2 = '''
</head>
<body>

<h2 style="text-align:center">CORONA STATUS</h2>

<div class="card">
  <img src="https://images.pexels.com/photos/3952232/pexels-photo-3952232.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" alt="John" style="width:100%">



  <h1>self.name</h1>
  <p class="title">Age self.age</p>
  <p >self.location</p>

 <p >Corona Status </p><meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">





<div class="w3-light-grey">
  <div class="w3-container w3-blue" style="width:{number_1}%">Status </div>
</div><br>
<p >Score {number_2}</p>
  <p><button>Contact self.email</button></p>
</div>


</body>
</html>'''


	temp_string=''
	with open("data.txt","r") as file:
		for line in file:
			temp_line=line.split(':')
			temp_name=temp_line[2]
			temp_name=temp_name.split(' ')
			if name in temp_name:
				temp_string+=line+'/'


	for user in temp_string.split('/'):
		if len(user) != 0 :
			user=user.split(':')
			user_profile=code_string2.replace('self.name',user[2]).replace('self.email',user[0]).replace('self.age',user[3])
			user_profile=user_profile.replace('self.location',user[4]+' '+user[5]+' '+user[6])

			with open("status.txt","r") as file1:
				for line in file1:
					line=line.split(':')
					if line[0]==str(user[0])+str(user[1]):

		            			user_profile=user_profile.format(number_1=(int(line[1])*100)/30,number_2=int(line[1]))
			user_profile=code_string1+user_profile
			return_string+=user_profile
			user_profile=''

	return return_string
