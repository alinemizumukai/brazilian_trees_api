from flask import Blueprint, jsonify, make_response, abort
from itsdangerous import json
from modules.db import get_db_connection
from modules.trees_query import getTreesBy
from models.class_tree import Tree

importExport = Blueprint('importExport', __name__,)

@importExport.route('/exportar')
def export():   
    return make_response( jsonify(getTreesBy("")))

@importExport.route('/importar')
def importar():
    return make_response( jsonify( {"":""} ) )
