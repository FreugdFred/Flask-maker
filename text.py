APPTEXT = """import sys
sys.dont_write_bytecode = True
from website import app


if __name__ == '__main__':
    app.run(debug=True)
"""


BASETEXT = """<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]>      <html class="no-js"> <!--<![endif]-->
<head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="{{ url_for('static', filename='styles/Base.css') }}">
        <link rel="stylesheet" href="/static/styles/{{Name}}.css">
        <title>{% block head %}{% endblock %}</title>
    </head>
<body>

    {% block body %}{% endblock %}

    <!--[if lt IE 7]>
        <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="#">upgrade your browser</a> to improve your experience.</p>
    <![endif]-->
    <script src="{{ url_for('static', filename='scripts/Base.js') }}" defer></script>
    <script src="/static/scripts/{{Name}}.js" defer></script>
</body>
</html>
"""



def HTMLTEXT(Name):
    HTMLTEXT = """{% extends "base.html" %}
{% set Name = "REPLACE" %}
{% block head %}REPLACE{% endblock %}
{% block body %}

<h1>REPLACE</h1>

{% endblock %}
"""
    
    return HTMLTEXT.replace("REPLACE", Name)


def PYFILECONTENT(Name):
    NameLower = Name.lower()

    FILECONTENT = """from flask import Blueprint, render_template, session, redirect, url_for
    
    
REPLACELOWER_blueprint = Blueprint('REPLACE', __name__)


@REPLACELOWER_blueprint.route('/REPLACELOWER', methods=['GET'])
def REPLACELOWER():
    return render_template('REPLACE.html')
"""

    FILECONTENTNAMES = FILECONTENT.replace("REPLACELOWER", NameLower)
    return FILECONTENTNAMES.replace("REPLACE", Name)



INITCONTENT = """from flask import Flask
    

app = Flask(__name__)
app.config['SECRET_KEY'] = "YOUR_SECRET_KEY"


"""
    


def MakeWriteFile(FilePath='', FileContents=''):
    with open(FilePath, 'w', encoding="UTF-8") as f:
        f.write(FileContents)
    