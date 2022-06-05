from flask import Blueprint, jsonify, make_response, abort
from modules.db import get_db_connection
from models.class_tree import Tree

RootRoute = Blueprint('root', __name__,)

@RootRoute.route('/')
def test():    
    result=[]
    conn = get_db_connection()
    query="SELECT t.id, scientific_name, height_max ,e.ecological_class, f.botanical_family,\
           ( SELECT popular_name FROM tb_popular_names WHERE tree = t.id) AS popular_name\
           FROM tb_trees t\
           LEFT JOIN tb_ecological_class e ON e.id = t.ecological_class\
           LEFT JOIN tb_botanical_family f ON f.id = t.botanical_family"
    trees = conn.execute( query ).fetchall()
    if( len( trees ) == 0 ):
        return make_response( jsonify({'error':'not found'}) ), 404
    for tree in trees:
        obj = Tree( tree )
        result.append( obj.get() )
    conn.close()
    return make_response( jsonify(result))