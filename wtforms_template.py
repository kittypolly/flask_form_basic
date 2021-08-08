from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'AOA'

class InfoForm(FlaskForm):
    
    group_name = StringField("당신은 어떤 그룹을 좋아하시나요?")
    submit = SubmitField('Submit')
    
@app.route('/', methods=['GET','POST'])
def index():

    group_name = False
    form = InfoForm()


    if form.validate_on_submit():
        group_name = form.group_name.data
        form.group_name.data = ''

    return render_template('home.html', form=form, group_name=group_name)

if __name__ == '__main__':
    app.run(debug=True)