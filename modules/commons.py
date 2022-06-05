from flask import jsonify, make_response

def error404( data ):
   return make_response( jsonify({ "error": [ { "not found" : "%s" % data } ] } ), 404 ) 