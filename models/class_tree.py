from typing import Dict, List
from flask import json
from markupsafe import string
from modules.db import get_db_connection
import sqlite3

class Tree:
    def __init__( self, data ):
        self.id               = data[ "id" ]               if ( "id"               in data ) else None
        self.scientific_name  = data[ "scientific_name" ]  if ( "scientific_name"  in data ) else None 
        self.height_max       = data[ "height_max" ]       if ( "height_max"       in data ) else None 
        self.ecological_class = data[ "ecological_class" ] if ( "ecological_class" in data ) else None 
        self.botanical_family = data[ "botanical_family" ] if ( "botanical_family" in data ) else None   
        self.popular_name     = data[ "popular_name" ]     if ( "popular_name"     in data ) else None   
 
    def get( self ):
        result={
            "id" : self.id,
            "scientific_name" : self.scientific_name,
            "height_max"      : self.height_max,
            "ecological_class": self.ecological_class,
            "botanical_family": self.botanical_family,
            "popular_name"    : self.popular_name       
        }  
        return result
    
    def create( self ):
        conn = get_db_connection()
        query = 'SELECT * FROM tb_botanical_family WHERE botanical_family = "%s";' % self.botanical_family
        result = list( conn.execute( query ).fetchall() )
        if( len( result ) == 0 ):
            cursor = conn.cursor()
            query = 'INSERT INTO tb_botanical_family ( botanical_family ) VALUES( "%s" );' % self.botanical_family
            cursor.execute( query )
            conn.commit()
            family_id = cursor.lastrowid
        else:
            family_id = result[0]["id"]
 
        query = 'SELECT * FROM tb_ecological_class WHERE ecological_class = "%s";' % self.ecological_class
        result = list( conn.execute( query ).fetchall() )
        if( len( result ) == 0 ):
            cursor = conn.cursor()
            query = 'INSERT INTO tb_ecological_class ( ecological_class ) VALUES( "%s" );' % self.ecological_class
            cursor.execute( query )
            conn.commit()
            class_id = cursor.lastrowid
        else:
            class_id = result[0]["id"]
        
        query = 'INSERT INTO tb_trees( scientific_name, popular_name, height_max, ecological_class, botanical_family )VALUES( "{}", "{}", {}, {}, {}  );'.format(
                     self.scientific_name, self.popular_name, self.height_max, class_id, family_id )
        cursor = conn.cursor()
        cursor.execute( query )
        conn.commit()
        tree_id = cursor.lastrowid
        return { "result":tree_id }
                
    def update( self ):
        if( not self.id ):
            return {"error":"sem id"}
        conn = get_db_connection()
        query = 'SELECT * FROM tb_trees WHERE id = "%s";' % self.id
        result = list( conn.execute( query ).fetchall() )
        if( len( result ) == 0 ):
            return {"error":"id não encontrado"}

        conn = get_db_connection()
        query = 'SELECT * FROM tb_botanical_family WHERE botanical_family = "%s";' % self.botanical_family
        result = list( conn.execute( query ).fetchall() )
        if( len( result ) == 0 ):
            cursor = conn.cursor()
            query = 'INSERT INTO tb_botanical_family ( botanical_family ) VALUES( "%s" );' % self.botanical_family
            cursor.execute( query )
            conn.commit()
            family_id = cursor.lastrowid
        else:
            family_id = result[0]["id"]
 
        query = 'SELECT * FROM tb_ecological_class WHERE ecological_class = "%s";' % self.ecological_class
        result = list( conn.execute( query ).fetchall() )
        if( len( result ) == 0 ):
            cursor = conn.cursor()
            query = 'INSERT INTO tb_ecological_class ( ecological_class ) VALUES( "%s" );' % self.ecological_class
            cursor.execute( query )
            conn.commit()
            class_id = cursor.lastrowid
        else:
            class_id = result[0]["id"]
        
        query = 'UPDATE tb_trees SET scientific_name = "{}", popular_name = "{}", height_max = {}, ecological_class = {}, botanical_family = {} WHERE id = {};'.format(
                     self.scientific_name, self.popular_name, self.height_max, class_id, family_id, self.id )
        cursor = conn.cursor()
        cursor.execute( query )
        conn.commit()
        return {"result":'A árvore foi atualizada com sucesso.'}

    def delete( self ):
        if( not self.id ):
            return {"error":"sem id"}
        conn = get_db_connection()
        query = 'SELECT * FROM tb_trees WHERE id = "%s";' % self.id
        result = list( conn.execute( query ).fetchall() )
        if( len( result ) == 0 ):
            return {"error":"id não encontrado"}

        conn = get_db_connection()
        query = 'DELETE FROM tb_trees WHERE id = "%s";' % self.id
        cursor = conn.cursor()
        cursor.execute( query )
        conn.commit()
        return {"result":'A árvore foi deletada com sucesso.'}
