from flask import Flask,render_template
import managedb as db 


app = Flask(__name__)


@app.route("/")
def index():
    c = db.get_connection()
    servicesDown,good=db.stringHtmlListServices(c)
    print("Good=",good)
    if good:
        return render_template("AllRight.html",ADDRESS=db.ADRESSE,PORT=db.PORT,WHAIT=db.WAIT)
    elif not good:
        return render_template("warning.html",servicesDown=servicesDown,ADDRESS=db.ADRESSE,PORT=db.PORT,WAIT=db.WAIT)

@app.route("/about")
def about_page():
    return '<h1>About Page</h1>'

if __name__ == "__main__":
    # app.debug = True # Mode debug pour les phases de testes
    app.run(host=db.IPSERVERFLASK, port=db.PORT) # un peut bizarre le IPSERVERFLASK et PORT dans db




    