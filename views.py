from app import app,db
from flask import render_template,request,redirect
from forms import *
from models import  Count_defect_zondes
from datetime import datetime
from sqlalchemy import exc



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/table', methods=['POST','GET'])
def table():
    save=''
    if request.method == 'POST':
        s_n = request.form['s_n']
        date = datetime(*[int(i) for i in request.form['date'].split()])
        type_zondes = request.form['type_zondes']
        svch_5 = request.form['svch_5']
        chastota_6 = request.form['chastota_6']
        chastota_7 = request.form['chastota_7']
        pause_8 = request.form['pause_8']
        impuls_9 = request.form['impuls_9']
        komutaciy_10 = request.form['komutaciy_10']
        telemetriy_11 = request.form['telemetriy_11']
        other_12 = request.form['other_12']
        temper_13 = request.form['temper_13']
        vlaga_14 = request.form['vlaga_14']
        primechanie_15 = request.form['primechanie_15']
        print( request.form)
        try:
            count_defect_zondes = Count_defect_zondes(s_n=s_n,date=date,type_zondes=type_zondes,svch_5=svch_5,
chastota_6=chastota_6,chastota_7=chastota_7,pause_8=pause_8,impuls_9=impuls_9,komutaciy_10=komutaciy_10,
telemetriy_11=telemetriy_11,other_12=other_12,temper_13=temper_13,vlaga_14=vlaga_14,primechanie_15=primechanie_15)
            db.session.add(count_defect_zondes)
            db.session.commit()
            save = 'Данные записаны'
            form = Count_defect_zonds_Form()
        except exc.IntegrityError as we:
            save='Радиозонд с таким номером уже записан в базу'
        except Exception as ex:
            save='Ошибка записи в базу'

    form = Count_defect_zonds_Form()
    return render_template('tables.html',save=save,form=form)


@app.route('/table2',  methods=['POST','GET'])
def table2():
    if request.method == 'POST':
        print(request.form)

    name = [(f'data{i}',i) for i in range(1,101)]
    return render_template('table2.html',names=name)
