# -*- coding: utf-8 -*-
from fileinput import filename
from flask import Blueprint, jsonify, make_response, render_template, send_file
from itsdangerous import json
import requests
from modules.db import get_db_connection
from modules.trees_query import getTreesBy, importTrees, exportTrees
from models.class_tree import Tree
import tempfile
import zipfile
import datetime

importExport = Blueprint('importExport', __name__,)

@importExport.route('/exportar/<option>')
def export(option):  
    if option == '0':
        return render_template( "exportar.html")
    else:
        return exportTrees()

@importExport.route('/importar/<option>')
def importar(option):
    link = "https://leafy-puppy-17562a.netlify.app/"
    data = requests.get( link ).content
    elements = json.loads( data )
    if option == '0':
        return render_template( "grid_catalogo.html", result=elements ) 
    else:
        importTrees( link )
        return render_template( "message.html", message="Importação realizada com sucesso!")
