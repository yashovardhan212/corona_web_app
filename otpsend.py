import smtplib

def otp_sender(email,age):
	with smtplib.SMTP('smtp.gmail.com',587) as smtp:
		otp_num=age*2935
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login('ajayraja234127@gmail.com','ajayraja@127')
		msg='Subject:Welcome To StaySafe\n\n {} is your one time password to verify your account.'.format(otp_num)
		smtp.sendmail('ajayraja234127@gmail.com',email,msg)

