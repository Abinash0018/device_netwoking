from flask import Flask,jsonify
import socket
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello NGINX reverse proxy'

@app.route('/ApiNetwork/<string:ip>')
def ApiNetwork(ip):
    
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for n in range(1,3):
        server_ip="192.168.20.{0}".format(n)
        rep = os.system('ping ' + server_ip)
        if rep == 0:
            if ip==server_ip:
                result={
                "device_type":"cisco_ios",
                "ip_adrs":ip,
                "username":"cisco",
                "password":"cisco",
                "server is up":"true"
                }
                #print ("server is up" ,server_ip,rep)
                
                return jsonify(result)
        else:
            if ip==server_ip:
                result={
                "device_type":"cisco_ios",
                "ip_adrs":ip,
                "username":"cisco",
                "password":"cisco",
                "server is up":"false"
                }
                
                
                return jsonify(result) 

             
    return jsonify({"result":"no ip found","ip_adrs":ip})
            
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
