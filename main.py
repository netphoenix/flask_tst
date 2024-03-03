from flask import (Flask, request, redirect, render_template, 
                    send_from_directory, url_for) 
from werkzeug.utils import secure_filename
import os
import datetime



BASE_DIR = os.getcwd()

app = Flask(
            __name__, 
            static_folder=os.path.join(BASE_DIR, 'static'), 
            template_folder=os.path.join(BASE_DIR, 'templates'), 
)

app.config['SECRET_KEY'] = 'some_secret_key_some_secret_key'
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'uploads')
users = ['user1','user2','user3','user4', 'user5','user6','user7','user8']

# базовая страница 
@app.route('/')
def index():
    return render_template('index.html', utc_dt=datetime.datetime.now(datetime.UTC))

# базовая страница которая включает в себя разные шаблоны
@app.route('/base/')
def base_index():
    return render_template('base.html', data='', err='')

# модальное окно 
@app.route('/form_modal/')
def openModal():
    return render_template('form_modal.html')

@app.route('/uploads/<name>')
def sendf(name):   
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)

# этот путь загрузит базовую страницу но с формой2 внутри вместо формы1
@app.route('/form2/', methods = ['GET', 'POST'])
def get_data2():
    if request.method == 'GET':
        return render_template('form2.html', data='', err='')

# только форма 1
@app.route('/form1/', methods = ['GET', 'POST'])
def get_data():
    if request.method == 'GET':
        return render_template('form1.html', data='', err='')
    
    #POST    
    fields = {
        'name':{'ru':'имя', 'data':'', 'type':'str', 'max':25,  'min':3},
        'age':{'ru':'возраст', 'data':'', 'type':'int', 'max':16,  'min':6},
        'email':{'ru':'email', 'data':'', 'type':'str', 'max':25, 'min':5},
        'select1':{'ru':'список1', 'data':'', 'type':'list'}
    }   
    
    
    err = check_fields(fields, request)
        
    f = request.files['file1']    
    if f and not err:
        # если есть файл и нет ошибок показываем на него ссылку
        f_name = secure_filename(f.filename)        
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
    else:
        err.append('Вы не выбрали файл')
    
    
    if  not err:
        #return redirect(url_for('get_data'))    
        return f'<a href="/uploads/{f_name}"> Спасибо за файлик {f_name} </a>'
    
    # иначе отправляем обратно на форму и пишем об ошибках
    data = {f:fields[f]['data'] for f in fields if fields[f]['data']}    
    return render_template('base.html', err=err, data = data)
    
    
def check_fields(fields, request):
    # валидатор полей
    # проверяет любое количество полей по описаной схеме
    err = []    
    for f in fields:
        if request.form.get(f):
            if fields[f]['type'] == 'int':
                try:
                    fields[f]['data'] = int(request.form.get(f))
                except:
                    err.append(f'Поле <{fields[f]["ru"]}> не евляется числом')
                else:
                    try:
                        if not fields[f]['min'] < fields[f]['data'] < fields[f]['max']:
                            err.append(f'Поле <{fields[f]["ru"]}> не подходит по значению')        
                    except:
                        raise KeyError ('no min max in fields description')
            elif fields[f]['type'] == 'str':
                fields[f]['data'] = request.form.get(f)
                try:
                    if not fields[f]['min'] < len(fields[f]['data']) < fields[f]['max']:
                        err.append(f'Поле <{fields[f]["ru"]}> не подходит по длине')        
                except:
                    raise KeyError ('no min max in fields description')
            elif fields[f]['type'] == 'list':                
                fields[f]['data'] = request.form.get(f)
        else: 
            err.append(f'Вы не заполнили поле <{fields[f]["ru"]}>')
    
    return err


if __name__ == "__main__":
    app.run(debug=True)
