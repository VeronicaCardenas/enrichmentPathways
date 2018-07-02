from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Pathways import Pathways, GetImagePathway
from resources.Compound import CompoundsDataPathways, CompoundsInfo, CompoundsForPathways
from resources.Protein import ProteinsOfCompound, GenesForPathways

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/Hello')
api.add_resource(Pathways, '/Pathways')
api.add_resource(CompoundsDataPathways, '/CompoundsDataPathways')
api.add_resource(CompoundsInfo, '/CompoundsInfo')
api.add_resource(CompoundsForPathways, '/CompoundsForPathways/<pathway>')
api.add_resource(ProteinsOfCompound, '/ProteinsOfCompound/<compound>')
api.add_resource(GetImagePathway, '/GetImagePathway/<pathway>')
api.add_resource(GenesForPathways, '/GenesForPathways/<pathway>')



    


