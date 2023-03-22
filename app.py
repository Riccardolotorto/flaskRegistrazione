from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/risultato', methods = ["POST"])
def risultato():
    nome = request.form["nome"]
    cognome = request.form["cognome"]
    dataNascita = request.form["data"]
    nazione = request.form["nazione"]
    username = request.form["username"]
    password = request.form["password"]
    confermaPassword = request.form["confermaPassword"]
    email = request.form["email"]
    lingue = request.form.getlist("lingua")
    scelta = request.form["scelta"]
    if nome == "" or cognome == "" or username == "" or password == "" or confermaPassword == "" or email == "":
        return render_template("errore.html", dato = "non hai inserito tutti i dati obbligatori (le richieste con l'asterisco)")
    elif password != confermaPassword:
        return render_template("errore.html", dato = "La password inserita non è uguale nella conferma")
    else:
        return render_template("risultato.html", nome = nome, cognome = cognome, dataNascita = dataNascita, nazione = nazione, utente = username, password = password, email = email, lingue = lingue, scelta = scelta)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)