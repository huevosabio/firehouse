import requests
import json
from flask import jsonify
from app import app

URL = 'http://127.0.0.1:6680/mopidy/rpc'

@app.route('/play')
def play():
	payload = {'jsonrpc':'2.0', 'id':1,'method':'core.playback.play'}
	headers = {'content-type':'application.json'}

	r=requests.post(URL,data=json.dumps(payload),headers=headers)
	return jsonify(r)

@app.route('/pause')
def pause():
	payload = {'jsonrpc':'2.0', 'id':1,'method':'core.playback.pause'}
	headers = {'content-type':'application.json'}

	r=requests.post(URL,data=json.dumps(payload),headers=headers)
	return jsonify(r)

@app.route('/stop')
def stop():
	payload = {'jsonrpc':'2.0', 'id':1,'method':'core.playback.stop'}
	headers = {'content-type':'application.json'}

	r=requests.post(URL,data=json.dumps(payload),headers=headers)
	return jsonify(r)	

@app.route('/resume')
def resume():
	payload = {'jsonrpc':'2.0', 'id':1,'method':'core.playback.resume'}
	headers = {'content-type':'application.json'}

	r=requests.post(URL,data=json.dumps(payload),headers=headers)
	return jsonify(r)

@app.route('/add_track')
def add_track(uri=None):
	if not uri: uri = request.json['uri']
	params = {'uri':uri}
	payload = {'jsonrpc':'2.0', 'id':1,'method':'core.tracklist.add','params':params}
	headers = {'content-type':'application.json'}

	r=requests.post(URL,data=json.dumps(payload),headers=headers)
	return jsonify(r)

@app.route('/arrived')
def arrival():
	add_track(request.json['uri'])
	play()
	return jsonify({'message':'Welcome Home: '+str(request.json['username'])})