from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/onko_alkuluku/<luku1>')
def onko_alkuluku(luku1):
    jakaja = 2
    luku = luku1
    alkuluku= "true"

    for i in range(luku):
        if luku % jakaja == 0:
            print("luku ei ole alkuluku")
            alkuluku= "false"
            break

        else:
            jakaja = jakaja + 1
            if luku == jakaja:
                print("luku on alkuluku")
                alkuluku="false"
                break
        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "luku": luku1
            "alkuluku": onko_alkuluku
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen kokonaisluku"
        }

    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhe):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

    #jakaja = 2
    #luku = int(input("Anna kokonaisluku: "))

    #for i in range(luku):
        #if luku % jakaja == 0:
         #   print("false")
          #  break

        #else:
         #   jakaja = jakaja + 1
          #  if luku == jakaja:
           #     print("true")
            #    break