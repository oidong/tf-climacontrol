from flask import render_template, Blueprint, redirect, url_for, request, flash, session, jsonify, current_app
from app.models import db, Ambientvalues

main_blueprint = Blueprint('main', __name__, template_folder='../templates')

@main_blueprint.route('/')
@main_blueprint.route('/index')
def index():
    title = "Dashboard"
    template = "dashboard.html"
    index_state = "active"
#    scripts = ["dashboard.js"]

    ambientvalues = Ambientvalues.query.order_by(Ambientvalues.timestamp.desc()).limit(10).all()
    
    return render_template(template,
                           title=title,
                           index_state=index_state,
                           ambientvalues=ambientvalues)

@main_blueprint.route('/datenbank')
@main_blueprint.route('/datenbank/<int:page>')
def datenbank(page=1):
    title = "Datenbank"
    template = "datenbank.html"
    datenbank_state = "active"

    ambientvalues = Ambientvalues.query.order_by(Ambientvalues.timestamp.desc()).with_entities(Ambientvalues.id, Ambientvalues.humidity, Ambientvalues.objtemp, Ambientvalues.ambtemp, Ambientvalues.illuminance, Ambientvalues.timestamp).paginate(page, current_app.config['POSTS_PER_PAGE'], False)
    
    return render_template(template,
                           title=title,
                           datenbank_state=datenbank_state,
                           ambientvalues=ambientvalues)

@main_blueprint.route('/diagramme')
def diagramme():
    title = "Diagramme"
    template = "diagramme.html"
    scripts = ["Chart.bundle.min.js", "diagramme.js"]
    diabgrammme_state = "active"

    return render_template(template,
                           title=title,
                           scripts=scripts,
                           diabgrammme_state=diabgrammme_state)

@main_blueprint.route('/api/byproperty/all')
@main_blueprint.route('/api/byproperty/all/')
@main_blueprint.route('/api/byproperty/all/<int:number>')
def ambientvalues(number=10):
    ambientvalues = list()

    ambientvalues_objects = Ambientvalues.query.order_by(Ambientvalues.timestamp.desc()).limit(number).all()

    for valueset in  ambientvalues_objects:
        result = valueset.__dict__
        del result["_sa_instance_state"]
        ambientvalues.append(result)
        
    return jsonify(ambientvalues)

@main_blueprint.route('/api/byproperty/<column>')
@main_blueprint.route('/api/byproperty/<column>/')
@main_blueprint.route('/api/byproperty/<column>/<int:number>')
def byproperty(column="", number=10):
    properties = list()

    if column == "humidity":
      result = Ambientvalues.query.order_by(Ambientvalues.timestamp.desc()).with_entities(Ambientvalues.humidity, Ambientvalues.timestamp).limit(number).all()
    elif column == "illuminance":
      result = Ambientvalues.query.order_by(Ambientvalues.timestamp.desc()).with_entities(Ambientvalues.illuminance, Ambientvalues.timestamp).limit(number).all()
    elif column == "ambtemp":
      result = Ambientvalues.query.order_by(Ambientvalues.timestamp.desc()).with_entities(Ambientvalues.ambtemp, Ambientvalues.timestamp).limit(number).all()
    elif column == "objtemp":
      result = Ambientvalues.query.order_by(Ambientvalues.timestamp.desc()).with_entities(Ambientvalues.objtemp, Ambientvalues.timestamp).limit(number).all()
    #else:
    #  return 404
    
    for item in result:
        values = dict()
        values[column] = item[0]
        values['timestamp'] = item[1]
        properties.append(values)
        
    return jsonify(properties)

@main_blueprint.route('/api/bydate')
@main_blueprint.route('/api/bydate/')
@main_blueprint.route('/api/bydate/<year>/<month>/<day>')
def day(year="2014", month="06", day="14"):
    ambientvalues = list()
    date = year+'-'+month+'-'+day+'%'
    
    ambientvalues_objects = Ambientvalues.query.order_by(Ambientvalues.timestamp.desc()).with_entities(Ambientvalues.humidity, Ambientvalues.objtemp, Ambientvalues.ambtemp, Ambientvalues.illuminance, Ambientvalues.timestamp).filter(Ambientvalues.timestamp.like(date)).all()

    for item in ambientvalues_objects:
        values = dict()
        values['humidity'] = item[0]
        values['objtemp'] = item[1]
        values['ambtemp'] = item[2]
        values['illuminance'] = item[3]
        values['timestamp'] = item[4]
        ambientvalues.append(values)
        
    return jsonify(ambientvalues)

@main_blueprint.route('/api/bydate/<year>/<month>/<day>/<hour>')
def hour(year="", month="", day="", hour=""):
    ambientvalues = list()
    date = year+'-'+month+'-'+day+' '+hour+'%'
    ambientvalues_objects = Ambientvalues.query.order_by(Ambientvalues.timestamp.desc()).with_entities(Ambientvalues.humidity, Ambientvalues.objtemp, Ambientvalues.ambtemp, Ambientvalues.illuminance, Ambientvalues.timestamp).filter(Ambientvalues.timestamp.like(date)).all()

    for item in ambientvalues_objects:
        values = dict()
        values['humidity'] = item[0]
        values['objtemp'] = item[1]
        values['ambtemp'] = item[2]
        values['illuminance'] = item[3]
        values['timestamp'] = item[4]
        ambientvalues.append(values)
        
    return jsonify(ambientvalues)

@main_blueprint.route('/javascript-testwiese/D3-Tabelle')
def d3js():
    title = "D3-Tabelle"
    template = "D3-Tabelle.html"
    scripts = ["d3.min.js", "tabelle.js"]
    
    return render_template(template,
                           title=title)

@main_blueprint.route('/javascript-testwiese/jQuery')
def jquery():
    title = "jQuery"
    template = "jQuery.html"
    scripts = []
    
    return render_template(template,
                           title=title)
