from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

#이건 시크릿키인데 아무거나해도 되지만, 보안을 위해 어렵게 하는게 좋다.
#이 파이썬 코드는 기본적인걸 다루는거라 좋아하는 그룹인 AOA로 해놨다.
app.config['SECRET_KEY'] = 'AOA'

class InfoForm(FlaskForm):
    
    group_name = StringField("당신은 어떤 그룹을 좋아하시나요?")
    submit = SubmitField('Submit')
    
@app.route('/', methods=['GET','POST'])
def index():

    group_name = False
    form = InfoForm()

    #form.valudate_on_submit은 폼데이터가 제대로 들어왔는지 점검한다.
    #DataRequired() 같은 점검 항목에 이상이 없는지 확인한다.
    #이게 3번 html이 2번
    if form.validate_on_submit():
        group_name = form.group_name.data
        form.group_name.data = ''
    #그리고 다시 초기화    

    #home.html으로 form과 breed를 넘깁니다.
    #이게 1번    
    return render_template('home.html', form=form, group_name=group_name)

    #이 구문을 잘 해석해봅시다.
    #우선 route '/' 이죠? 
    #그렇다는건 local_host 에서 '/' 즉 기본페이지가 home.html 입니다.
    #home.html에 있는 {{form}} 은 여기서의 form이 넘어갑니다.
    #breed 역시 마찬가지 입니다.
    #입력후에 if form.valudate문의 작동합니다.

if __name__ == '__main__':
    app.run(debug=True)
        
    