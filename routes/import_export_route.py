# -*- coding: utf-8 -*-
from fileinput import filename
from flask import Blueprint, jsonify, make_response, send_file
from itsdangerous import json
from modules.db import get_db_connection
from modules.trees_query import getTreesBy, importTrees, exportTrees
from models.class_tree import Tree
import tempfile
import zipfile
import datetime

importExport = Blueprint('importExport', __name__,)

@importExport.route('/exportar')
def export():  
    return exportTrees()

@importExport.route('/importar')
def importar():
    trees = importTrees( "https://leafy-puppy-17562a.netlify.app/" )
    return make_response( jsonify( trees ) )
