from flask_login import login_required, logout_user, login_user, current_user
from flask import abort
from reade import app
from flask import render_template, send_from_directory, request, flash, url_for, redirect, jsonify
import smtplib


@app.route('/')
# @app.route('/home/')
def about():
    
    return render_template('index.html')


@app.route('/img/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/send_gmail/<name>/<number>/<gmail>/', methods=['POST', 'GET'])
def send_gmail(name, number, gmail):

    user = "legalteam.kz@gmail.com"
    passwd = "npwpwryjdnlseokj"
    server = "smtp.gmail.com"
    port = 587
    charset = 'Content-Type: text/plain; charset=utf-8'
    mime = 'MIME-Version: 1.0'
    text = 'Имя :' + str(name), 'Номер: ' + str(number), 'Gmail: ' + str(gmail)
    body = "\r\n".join((f"From: {user}", f"To: {gmail}", f"Subject: {name}", mime, charset, "", str(text)))
    smtp = smtplib.SMTP(server, port)
    smtp.starttls()
    smtp.login(user, passwd)
    smtp.sendmail(user, user, body.encode('utf-8'))
    smtp.quit()
    data = {'send':True}
    return jsonify(data)


@app.before_first_request
def create_tables():
    #app.app_context().push()
    db.create_all()