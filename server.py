from flask import Flask,jsonify
app=Flask(__name__)
contacts={
    "mohamed basheer":{
        "phone":"9898992791",
        "instagram":"md_bash",
        "github":"md007",
    },
    "sudhir":{
        "phone":"9453245677",
        "instagram":"chudhir_99",
        "github":"sudhireh-00",
    },
        "bharath":{
        "phone":"9453242467",
        "instagram":"barath09",
        "github":"barathroshan",
    },
        "raju":{
        "phone":"9097245677",
        "instagram":"raju_bhai",
        "github":"rajeshh",
    },
        "arul":{
        "phone":"9457826527",
        "instagram":"arulbalan",
        "github":"arulball",
    },

}
@app.route('/',methods=['GET'])
def send():
    return jsonify({'contacts':contacts})
@app.route('/<name>',methods=['GET'])
def sendname(name):
    name=name.lower()
    try:
        return jsonify({'contacts':contacts[name]})
    except:
        return jsonify({'contacts':None})

if __name__ == '__main__':
    app.run(debug=True)