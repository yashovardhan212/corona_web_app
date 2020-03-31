from flask import Flask
from flask import request

app = Flask(__name__)
app.config["DEBUG"]=True
@app.route('/',methods=["GET","POST"])

def symp_updater():
    if request.method=="POST":
        filename=request.form["userpass"]
        return '''
        <!DOCTYPE html>
<html>
<style>

body {
  font-family: Arial, Helvetica, sans-serif;

}

/* The container */
.container {
  display: block;
  position: relative;
  padding-left: 35px;
  margin-bottom: 12px;
  cursor: pointer;
  font-size: 22px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* Hide the browser's default checkbox */
.container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

/* Create a custom checkbox */
.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 25px;
  width: 25px;
  background-color: #eee;
}

/* On mouse-over, add a grey background color */
.container:hover input ~ .checkmark {
  background-color: #ccc;
}

/* When the checkbox is checked, add a blue background */
.container input:checked ~ .checkmark {
  background-color: #2196F3;
}

/* Create the checkmark/indicator (hidden when not checked) */
.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

/* Show the checkmark when checked */
.container input:checked ~ .checkmark:after {
  display: block;
}

/* Style the checkmark/indicator */
.container .checkmark:after {
  left: 9px;
  top: 5px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 3px 3px 0;

  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}
.registerbtn {
  background-color: Blue;
  color: white;
  padding: 16px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 30%;
  opacity: 0.6;

}
</style>'''+'''
<body >

<h1>Symptomps </h1>
<form action='http://staysafe009.pythonanywhere.com/' method="post">
<label class="container" > cough<input type="checkbox" name="1"><span class="checkmark"></span></label>

  <label class="container" >High temperature(fever >99.5 °F)

  <input type="checkbox" name="2">
  <span class="checkmark"></span>
	</label>
<label class="container" >tiredness
  <input type="checkbox" name="3">
  <span class="checkmark"></span>
</label>
<label class="container" >medium temperature(95.9–99.5 °F)
  <input type="checkbox" name="4">
  <span class="checkmark"></span>
</label>
<label class="container" >low temperature(<95 °F)
  <input type="checkbox" name="5">
  <span class="checkmark"></span>
</label>
<label class="container" >difficulty breathing
  <input type="checkbox" name="6">
  <span class="checkmark"></span>
</label>
<label class="container" >shortness of breath
  <input type="checkbox" name="7">
  <span class="checkmark"></span>
</label>
<label class="container" >aches and pains
  <input type="checkbox" name="8">
  <span class="checkmark"></span>
</label>
<label class="container" >sore throat
  <input type="checkbox" name="9">
  <span class="checkmark"></span>
</label>
<label class="container" >diarrhoea
  <input type="checkbox" name="10">
  <span class="checkmark"></span>
</label>
<label class="container" >nausea
  <input type="checkbox" name="11">
  <span class="checkmark"></span>
</label>
<label class="container" >runny nose
  <input type="checkbox" name="12">
  <span class="checkmark"></span>
</label>
<label class="container" >Persistent pain or pressure in the chest
  <input type="checkbox" name="13">
  <span class="checkmark"></span>
</label>
<label class="container" >Bluish lips or face
  <input type="checkbox" name="14">
  <span class="checkmark"></span>
</label>
<label class="container" >I have traveled recently during the last 14 days.
  <input type="checkbox" name="15">
  <span class="checkmark"></span>
</label>
<label class="container" >I have a travel history in COVID-19 infected area.
  <input type="checkbox" name="16">
  <span class="checkmark"></span>
</label>
<label class="container" >I have direct contact or is taking care of a positive COVID-19 patient.
  <input type="checkbox" name="17">
  <span class="checkmark"></span>
</label>
<label class="container" >Sneezing frequency(High)
  <input type="checkbox" name="18">
  <span class="checkmark"></span>
</label>
<input name="19" value="{filename}" type="hidden">
<button type="submit" class="registerbtn"><b style="text-size:10px;">SUBMIT</b></button>
</form>
</body>
</html>
'''.format(filename=filename)
    return 'permission denied and your ip with your mac has beeen reported to cyber agency'

