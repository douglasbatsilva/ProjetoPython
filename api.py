from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])
def home():
    if(request.method == "GET"):
        return render_template("index.html")
    else:
        if (request.form["num1"] != "" or request.form["num2"] != ""):
            num1 = request.form["num1"]
            num2 = request.form["num2"]
            if (request.form["opc"] == "soma"):
                return {
                    "Resultado": str(int(num1) + int(num2))
                }

            elif (request.form["opc"] == "subt"):
                return {
                    "Resultado": str(int(num1) - int(num2))
                }

            elif (request.form["opc"] == "mult"):
                return {
                    "Resultado": str(int(num1) * int(num2))
                }

            elif (request.form["opc"] == "divi"):
                return {
                    "Resultado": str(int(num1) // int(num2))
                }

        else:
            return "Informe um Valor Válido"


@app.route("/juros", methods=["GET", "POST"])
def juros():
    if(request.method == "GET"):
        return render_template("juros.html")
    else:
        if (request.form["num1"] != "" or request.form["num2"] != ""):
            num1 = request.form["num1"]
            num2 = request.form["num2"]
            num3 = request.form["num3"]
            if (request.form["opc"] == "juro"):
                return {
                    "Resultado": str(float(num1) * (1 + (float(num2)/100)) ** int(num3))
                }
            elif (request.form["opc"] == "jusi"):
                return {
                    "Resultado": str( float(num1) + (float(num1) * ((float(num2)/100)) * int(num3)))
                }
        else:
            return "Informe um Valor Válido"

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")


app.run(port=8080, debug=True)