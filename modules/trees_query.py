from flask import Blueprint, jsonify, make_response, abort
from markupsafe import string
from modules.db import get_db_connection
from models.class_tree import Tree

def getTreesBy( data ):
    lut_convet={
        "id"               : "t.id", 
        "scientific_name"  : "t.scientific_name", 
        "ecological_class" : "e.ecological_class", 
        "botanical_family" : "f.botanical_family",
        "popular_name"     : "t.popular_name"
    }
    
    result=[]
    where = ' WHERE '
    flag = False
    conn = get_db_connection()
    query="SELECT t.id, t.scientific_name, t.popular_name, height_max ,e.ecological_class, f.botanical_family\
           FROM tb_trees t\
           LEFT JOIN tb_ecological_class e ON e.id = t.ecological_class\
           LEFT JOIN tb_botanical_family f ON f.id = t.botanical_family"
    
    for atributes in data :
        if( flag == True ) : where += " AND "
        flag = True
        where += lut_convet[ atributes ] + " = '%s'" % data[ atributes ]
    
    if( flag == True ) : query += " %s" % where
    trees = conn.execute( query ).fetchall()
    for tree in trees:
        result.append( Tree( dict( tree ) ) )
    conn.close()
    
    return result