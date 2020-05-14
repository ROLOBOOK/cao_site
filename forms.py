from wtforms import Form, StringField, TextAreaField


class Count_defect_zonds_Form(Form):

    s_n = StringField('Номер радиозонда')
    date = StringField('Дата изготовления радиозонда')
    type_zondes = StringField('Тип радиозонда')
    svch_5 = StringField('Нет генерации СВЧ')
    chastota_6 = StringField('Несущая частота')
    chastota_7 = StringField('Частота суперизации')
    pause_8 = StringField('Отсутствие ответной паузы')
    impuls_9 = StringField('Нарушены длительности периодов импульсов в телеметрическом, опорном каналах')
    komutaciy_10 = StringField('Нарушена очередность коммутации')
    telemetriy_11 = StringField('Отказ телеметрического канала')
    other_12 = StringField('Другие причины')
    temper_13 = StringField('Разность ΔТ показаний измерений температуры абсолютным прибором и радиозондом >1,8 °С')
    vlaga_14 = StringField('Разность ΔU показаний измерений влажности абсолютным прибором и радиозондом > 15%')
    primechanie_15 = StringField('Примечание (указать частоту забракованного радиозонда)')
