import json
import os
from flask import Flask, render_template, request
from sightengine.client import SightengineClient

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
client = SightengineClient('1981380944', 'HkswnexsudY5qP6iQJim')


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')


@app.route('/detect', methods=['GET', 'POST'])
def detect():
    try:
        target = os.path.join(APP_ROOT, 'images/')
        print(target)
        nude = " "
        drug = " "
        weapons = " "
        alcohol = " "
        offensive = " "
        face = " "

        if not os.path.isdir(target):
            os.mkdir(target)

        for file in request.files.getlist("imagefile"):
            print(file)
            filename = file.filename
            destination = "/".join([target, filename])
            print(destination)
            file.save(destination)

        output = client.check('nudity', 'wad', 'offensive','face-attributes').set_file(destination)
        

        if output['nudity']['safe'] <= output['nudity']['partial'] and output['nudity']['safe'] <= output['nudity']['raw']:
            nude = "True"
        else:
            nude = "False"

        if output['weapon'] > 0.2:
            weapons = "True"
        else:
            weapons = "False"

        if output['alcohol'] > 0.2:
            alcohol = "True"
        else:
            alcohol = "False"

        if output['drugs'] > 0.2:
            drug = "True"
        else:
            drug = "False"
        if output['offensive']['prob'] > 0.2:
            offensive = output['offensive']['boxes'][0]['label']
            # offensive = "True"
        else:
            offensive = "False"

        if output['faces'][0]['attributes']['female'] > 0.2:
            face = "Female"
        elif output['faces'][0]['attributes']['male'] > 0.2:
            face = "Male"
        elif output['faces'][0]['attributes']['minor'] > 0.2:
            face = "Minor"
        elif output['faces'][0]['attributes']['sunglasses'] > 0.2:
            face = "Sunglasses"
        else:
            face = "False"

        myfile = open('data.json', 'w')
        myfile.write(json.dumps(output, indent=5))
        myfile.close()

        return render_template("complete.html", weapons=weapons, nude=nude, drug=drug, alcohol=alcohol, offensive=offensive,face=face)

    except ConnectionError as identifier:
        return (identifier)


if __name__ == '__main__':
    app.run(debug=True)
