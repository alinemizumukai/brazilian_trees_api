from ctypes import sizeof
import dataclasses
from datetime import datetime
from flask import Blueprint, jsonify, make_response, request, json, render_template
from flask_login import login_required
from itsdangerous import json
from models.class_tree import Tree
from modules.trees_query import getTreesBy
from modules.commons import error404

routeTrees = Blueprint('trees', __name__,)

@routeTrees.route( '/', methods = [ 'GET', 'POST', 'PUT' ] )
@login_required
def trees_root():
    if( request.method == 'GET' ):
        data = {}
        if( request.data ):
            data = json.loads( request.data )
        return getMaker( data )
    if( request.method == 'POST' ):
        data = json.loads( request.data )
        if( type( data ) == list ):
            result = Tree( data[0] )
        else:
            result = Tree( data )
        try:
            return jsonify( id = result.post() )
        except ValueError as x:
            return jsonify( error = f"{x.args[0]}" ) 
    if( request.method == 'PUT' ):
        data = json.loads( request.data )
        if( type( data ) == list ):
            result = Tree( data[0] )
        else:
            result = Tree( data )
        try:
            return jsonify( id = result.put() )
        except ValueError as x:
            return jsonify( error = f"{x.args[0]}" ) 
                     
def getMaker( data ):
    result = {
        "timestamp": datetime.now(), 
        "data":[]
    }
    treeList = []
    if( type( data ) == list ):
        for i in data:          
            result["data"].append( getTreesBy( i ) )
    else:
        result["data"].append( getTreesBy( data ) )
    
    if( len( result["data"] ) == 0 ):
        return error404( data )

    return result

@routeTrees.route('/id' )
@login_required
def trees_id(): 
    busca = "id"
    data = request.args.get('data')
    erro = True if data is not None else False
    result = getMaker( { "id": data } )
    return render_template("grid.html", result=result, erro=erro, busca=busca)

@routeTrees.route('/scientific_name' )
@login_required
def trees_sci_name(): 
    busca = "sci_name"
    data = request.args.get('data')
    erro = True if data is not None else False
    result = getMaker( { "scientific_name": data } )
    return render_template("grid.html", result=result, erro=erro, busca=busca)
    
@routeTrees.route('/popular_name/<data>' )
@login_required
def trees_pop_name(data): 
    return 'TODO'

@routeTrees.route('/ecological_class' )
@login_required
def trees_eco_class():   
    busca = "eco_class"
    data = request.args.get('data')
    erro = True if data is not None else False
    result = getMaker( { "ecological_class": data } )
    return render_template("grid.html", result=result, erro=erro, busca=busca)

@routeTrees.route('/botanical_family' )
@login_required
def trees_botanical_family():   
    busca = "botanical_family"
    data = request.args.get('data')
    erro = True if data is not None else False
    result = getMaker( { "botanical_family": data } )
    return render_template("grid.html", result=result, erro=erro, busca=busca)

@routeTrees.route('/register_tree/<data>')
@login_required
def trees_register_tree(data):
    result = getMaker( { "id": data } )
    if not result['data'][0]:
        return render_template('form.html', result=None, title='Cadastrar')      
    else:         
        return render_template('form.html', result=result, title='Atualizar')

@routeTrees.route('/save_tree', methods = ['POST'])
def trees_save_tree():
    data=request.form
    if data['id'] == '0':
        result = Tree( data ).create()          # {"result":id da arvore}
        return  render_template('message.html', message=f"A ??rvore foi criada com sucesso. Id = {result['result']}.")
    else:
        result = Tree( data ).update()          # {"result":'A ??rvore foi atualizada com sucesso.'} ou {"erro":"msg erro"}
        return  render_template('message.html', message=result['result'])

@routeTrees.route('/delete_tree/<data>')
@login_required
def trees_delete_tree(data):
    result = Tree( { "id": data } ).delete()    # {"result":'A ??rvore foi excluida com sucesso.'} ou {"erro":"msg erro"}
    return render_template('message.html', message=result['result'])

@routeTrees.route('/<string:nome>')
def error(nome):
   return render_template('error.html')