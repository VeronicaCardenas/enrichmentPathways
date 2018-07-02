from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()




class Pathway(db.Model):
    __tablename__ = 'kegg'
    id = db.Column(db.String, primary_key=True)
    idGene = db.Column(db.String(150), unique=True, nullable=False)
    idPathways = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, idGene):
        self.idGene = idGene


class PathwaySchema(ma.Schema):
    id = fields.String()
    idGene = fields.String(required=True)
    idPathways = fields.String(required=True)


class CompoundPathway:
    def __init__(self, idKegg, pathway, graphic):
        self.id = id
        self.idKegg = idKegg
        self.pathway = pathway
        self.graphic = graphic
        
class Graphic:
    def __init__(self, graphicsType, x, y, width, height, idKegg):
        self.graphicsType = graphicsType
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.idKegg = idKegg

class GraphicSchema(ma.Schema):
    graphicsType = fields.String(attribute="graphicsType")
    x = fields.String(attribute="x")
    y = fields.String(attribute="y")
    width = fields.String(attribute="width")
    height = fields.String(attribute="height")
    idKegg = fields.String(attribute="idKegg")

class CompoundPathwaySchema(ma.Schema):
    idKegg = fields.String(attribute="idKegg")
    pathway = fields.String(attribute="pathway")
    graphic = fields.Nested(GraphicSchema)

class CompoundInfo:
    def __init__(self, idKegg, chemblid, smile):
        self.idKegg = idKegg
        self.chemblid = chemblid
        self.smile = smile


class CompoundInfoSchema(ma.Schema):
    idKegg = fields.String(attribute="idKegg")
    chemblid = fields.String(attribute="chemblid")
    smile = fields.String(attribute="smile")

class ValueTargetFishing:
    def __init__(self, value, type):
        self.value = value
        self.type = type
        
class ValueTargetFishingSchema(ma.Schema):
    value = fields.String(attribute="value")
    type = fields.String(attribute="type")

class Protein:
    def __init__(self, proteinId, valueTargetFishing):
        self.proteinId = proteinId
        self.valueTargetFishing = valueTargetFishing
        
class ProteinSchema(ma.Schema):
    proteinId = fields.String(attribute="proteinId")
    valueTargetFishing = fields.Nested(ValueTargetFishingSchema)



class GenePathway:
    def __init__(self, idKegg,nameKegg, pathway, graphic):
        self.id = id
        self.idKegg = idKegg
        self.nameKegg = nameKegg
        self.pathway = pathway
        self.graphic = graphic

class GenePathwaySchema(ma.Schema):
    idKegg = fields.String(attribute="idKegg")
    nameKegg = fields.String(attribute="nameKegg")
    pathway = fields.String(attribute="pathway")
    graphic = fields.Nested(GraphicSchema)
