from flask import Flask, render_template, request, redirect, url_for
import smtplib
import os

app = Flask(__name__, template_folder='templates', static_folder='static')


EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587


@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        send_email(name=name, email=email, message=message)
        return redirect(url_for('home'))
    else:
        return render_template('index.html')


def send_email(name, email, message):
    email_message = f"Subject:WEBSITE EMAIL\n\nName: {name}\nEmail: {email}\n{message}"
    with smtplib.SMTP(host=EMAIL_HOST, port=EMAIL_PORT) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            EMAIL,
            EMAIL,
            email_message
        )


if __name__ == "__main__":
    app.run(debug=False)
