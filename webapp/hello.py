from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Hepsiburada from Ali Murat"
    
if __name__ == '__main__':
    #app.run() 
    app.run(debug=True, host='0.0.0.0',port='11130')
