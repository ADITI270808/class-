from flask import Flask,jsonify, request

app = Flask(__name__)

data = [
    {
        'Contact': '9924129911',
        'Name':'Raju',
        'id': 1,
        'done': False
    },
    {
        'Contact': 9537382129,
        'Name': 'Sara',
        'id': 2, 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'Contact': request.json['Contact'] ,
        'Name': request.json['Name'],
        'id': request.json.get('id', ""),
        'done': False
    }
    data.append(task)
    return jsonify({
        "status":"success",
        "message": "Data added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : data
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)