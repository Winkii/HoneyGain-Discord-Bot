import configparser

#init config file
def init():
    config = configparser.ConfigParser()
    config.sections()
    config.read('./Ressources/code/save.ini')
    return config


#set new value
def set_value(category,key,value):
    config=init()
    config.set(category,key, str(value))
    with open('./Ressources/code/save.ini', 'w') as configfile:
        config.write(configfile)

#get old value
def get_value(category,key):
    config=init()
    return config[category][key]


#difference between the old and the new value
def difference(key,new_total_today):
    old_total_today=get_value('today',key)
    diff=round(float(new_total_today), 2)-round(float(old_total_today), 2)
    set_value('today',key,float(new_total_today))
    if key=="balance":
        set_value('all','lifetime',round(float(get_value('all','lifetime'))+float(diff), 2))
    if diff>0:
        return "+"+"{0:.2f}".format(diff)
    elif diff==0:
        return "0"


