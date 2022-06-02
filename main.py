from flask import Flask, flash, redirect, url_for, render_template, request, abort
from flask_bootstrap import Bootstrap



from forms import ClubForm


app = Flask(__name__)
#app.config["EXPLAIN_TEMPLATE_LOADING"] = True
Bootstrap(app)
# WTForms requires you to set a SECRET_KEY:
app.config['SECRET_KEY'] = 'your secret key'
# Setting templates to auto reload just makes it easier to develop:
app.config["TEMPLATES_AUTO_RELOAD"] = True

clubs_list = []

@app.route("/", methods=('GET', 'POST'))
def home():
    # create a form
    form = ClubForm()   

    # get form info if it submitted with no validation issues:
    if form.validate_on_submit():
        clubs_list.append({'name': form.name.data,
                           'description': form.description.data,
                           'spaces_available': form.spaces_available.data,
                           'tipo_persona': form.tipo_persona.data,
                           'is_free': form.is_free.data
                           })
        # redirect to the list clubs page
        return redirect(url_for('clubs'))
    # no form submitted (you just entered the page) - so render the form:
    return render_template('index.html', form=form)

@app.route('/clubs')
def clubs():
    return render_template('clubs.html', clubs_list=clubs_list)
  
app.run(host='0.0.0.0', port=81)