from flask import Blueprint, jsonify, make_response, render_template
from flask_login import login_required

Greetings = Blueprint('greetings', __name__,)

@Greetings.route('/')
@login_required
def greetings():
    data =  {   
            "Authors":{
                "institution":"Fatec Ribeirão Preto",
                "name":["Aline Mizumukai", "Caio Damasceno Pellicani"],
                "about":"Trabalho avaliativo desenvolvido em Python com uso do framework Flask",
            },
            "apiDescription":{
                "name":"Brazilian Trees Api",
                "about":"Api desenvolvida com o objetivo de armazenar e acessar dados de especies arboreas nativas dos diferentes biomas do Brasil",
                "endpoints":[
                    {  
                        "Route":"/trees/id",
                        "methods":["GET", "PUT"],
                        "description":"Retorna/atualiza os dados da arvore com o código enviado",
                        "title": "Busca por código"
                    },
                    {  
                        "Route":"/trees/scientific_name",
                        "methods":["GET"],
                        "description":"Retorna os dados da arvore com o nome cientifico enviado",
                        "title": "Busca por nome científico"
                    },
                    {  
                        "Route":"/trees/botanical_family",
                        "methods":["GET"],
                        "description":"Retorna os dados das arvores da familia enviada",
                        "title": "Busca por família"
                    },
                    {  
                        "Route":"/trees/ecological_class",
                        "methods":["GET"],
                        "description":"Retorna os dados das arvores da classe ecologica enviada",
                        "title": "Busca por classe ecológica"
                    },
                    {  
                        "Route":"/trees/register_tree/0",
                        "methods":["POST"],
                        "description":"Cadastra uma nova árvore",
                        "title": "Cadastrar árvore"
                    },
                    {  
                        "Route":"/trees/importar/0",
                        "methods":["GET"],
                        "description":"Permite importar árvores de um catálogo externo",
                        "title": "Catálogo de árvores"
                    },
                    {  
                        "Route":"/trees/exportar/0",
                        "methods":["GET"],
                        "description":"Exportar árvores cadastradas no formato zip",
                        "title": "Exportar árvores cadastradas"
                    }
                ]
            
            }
        }
    return render_template( "menu.html", data=data )