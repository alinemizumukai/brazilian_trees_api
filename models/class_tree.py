from typing import Dict, List
from flask import json
from markupsafe import string
from modules.db import get_db_connection

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
        if( self.id != None ):
            conn = get_db_connection()
            query = "SELECT popular_name FROM tb_popular_names WHERE tree = %s" % self.id
    
            for name in conn.execute( query ).fetchall():
                result["popular_name"].append( name["popular_name"] )
    
            conn.close()   
        return result
    
    def post( self ):
        if( self.id == None ): raise ValueError( "id" )    
        return self.id

    def put( self ):
        if( self.id == None ): raise ValueError( "id" )    
        return self.id   
    
    def toJson( self ):
        if( self.id ):
            return {
                "id" : self.id,
                "scientific_name" : self.scientific_name,
                "height_max"      : self.height_max,
                "ecological_class": self.ecological_class,
                "botanical_family": self.botanical_family,
                "popular_name"    : self.popular_name
            }
        else:
            return {}