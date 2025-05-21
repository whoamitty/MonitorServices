import sqlite3
import ping
from constant import *

def get_connection():
    conn = None
    try:
        conn = sqlite3.connect("./mydata.db")
        print(sqlite3.version)
        return conn
    except sqlite3.Error as e:

        print(e)



def create_table(c):
    cur = c.cursor()
    cur.execute(f"""        
        CREATE TABLE {TABLE_SERVICE}(
            {SERVICE_ID} INTEGER PRIMARY KEY AUTOINCREMENT,
            {SERVICE_NAME} TEXT,
            {SERVICE_DOMAIN} TEXT,
            {SERVICE_IP} TEXT,
            {NUMBERFILEDTRIES} INTEGER);
    """)


def select_data(c):
    cur = c.cursor()
    cur.execute(f"SELECT {SERVICE_ID}, {SERVICE_NAME}, {SERVICE_DOMAIN}, {SERVICE_IP} FROM {TABLE_SERVICE}") # ORDER BY {SERVICE_ID}")
    rows = cur.fetchall()

    # Initialiser le dictionnaire avec des listes vides pour chaque catégorie
    services_data = {
        'IDS': [],
        'NAMES': [],
        'DOMAINS': [],
        'IP': []

    }

    for row in rows:
        service_id, service_name, service_domain, service_ip = row

        # Ajouter les données aux listes respectives, avec gestion des valeurs nulles ou vides
        services_data['IDS'].append(service_id if service_id else None)
        services_data['NAMES'].append(service_name if service_name else None)
        services_data['DOMAINS'].append(service_domain if service_domain else None)
        services_data['IP'].append(service_ip if service_ip else None)
    
    print(services_data)
    return services_data

def checkNumberFiledTries(c,service_id):
    cur = c.cursor()
    
    select_query=f"SELECT  {NUMBERFILEDTRIES} FROM {TABLE_SERVICE} WHERE {SERVICE_ID} = ?"
    cur.execute(select_query, (service_id,))
    numberFiledTries = cur.fetchall()
    print("numberFiledTries[0][0]:",numberFiledTries[0][0],"\n","numberFiledTries:",numberFiledTries,"\n\n")
    return int(numberFiledTries[0][0])


def manage_service_ping_and_retries(IP, numberFiledTries, MAXTRIES, c, service_id, dictServices_data, i, stringHtmlListServices):
    good = True  # Initialiser good à True

    if IP is None:
        domain = dictServices_data['DOMAINS'][i]
        ping_result = ping.ping_address(domain)
    else:
        ping_result = ping.ping_address(IP)

    print("ping_result: ",ping_result)

    if not ping_result:
        if numberFiledTries < MAXTRIES:
            modify_data(c, service_id, new_numberFiledTries=numberFiledTries + 1)
            print("numberFiledTries+1: numberFiledTries<MAXTRIES", f"{numberFiledTries + 1}<{MAXTRIES}")
        elif numberFiledTries == MAXTRIES:
            print("Adding service to stringHtmlListServices: numberFiledTries==MAXTRIES", MAXTRIES)
            good = False
            stringHtmlListServices.append(
                f"{dictServices_data['IDS'][i]} {dictServices_data['NAMES'][i]} {dictServices_data['DOMAINS'][i]} {dictServices_data['IP'][i]}")

    elif numberFiledTries > 0:
        modify_data(c, service_id, new_numberFiledTries=0)

    return  stringHtmlListServices, good

def stringHtmlListServices(c):
    dictServices_data = select_data(c)
    stringHtmlListServices = []
    i = 0
    good = True
 
    for IP in dictServices_data['IP']:
        service_id = dictServices_data['IDS'][i]
        print("service_id:", service_id)
        numberFiledTries = checkNumberFiledTries(c, service_id)

        if good :
            stringHtmlListServices, good = manage_service_ping_and_retries(IP, numberFiledTries, MAXTRIES, c, service_id, dictServices_data, i, stringHtmlListServices)
        
        else :
            manage_service_ping_and_retries(IP, numberFiledTries, MAXTRIES, c, service_id, dictServices_data, i, stringHtmlListServices)

        i += 1

        

    print("print(stringHtmlListServices)", stringHtmlListServices)
    return stringHtmlListServices, good




def insert_data(c, service_name=None, service_domain=None, service_ip=None):
    cur = c.cursor()
    columns=[]
    placeholders = []
    values = []
    numberFiledTries=0

    if service_name is not None:
        columns.append(SERVICE_NAME)
        placeholders.append('?')
        values.append(service_name)

    if service_domain is not None:
        columns.append(SERVICE_DOMAIN)
        placeholders.append('?')
        values.append(service_domain)

    if service_ip is not None:
        columns.append(SERVICE_IP)
        placeholders.append('?')
        values.append(service_ip)

    columns.append(NUMBERFILEDTRIES)
    placeholders.append('?')
    values.append(numberFiledTries)


    columns_str = ', '.join(columns)
    placeholders_str = ', '.join(placeholders)

    insert_query = f"INSERT INTO {TABLE_SERVICE} ({columns_str}) VALUES ({placeholders_str})"
    cur.execute(insert_query, values)
    c.commit()



def modify_data(c, 
                service_id, 
                new_service_name=None, 
                new_service_domain=None, 
                new_service_ip=None, 
                new_numberFiledTries=None):
    print("modify_data")
    cur = c.cursor()
    updates = []
    parameters = []

    if new_service_name is not None:
        updates.append(f"{SERVICE_NAME} = ?")
        parameters.append(new_service_name)

    if new_service_domain is not None:
        updates.append(f"{SERVICE_DOMAIN} = ?")
        parameters.append(new_service_domain)

    if new_service_ip is not None:
        updates.append(f"{SERVICE_IP} = ?")
        parameters.append(new_service_ip)

    if new_numberFiledTries is not None:
        updates.append(f"{NUMBERFILEDTRIES} = ?")
        parameters.append(new_numberFiledTries)


    if not updates:
        print("modify_data")
        raise ValueError("No columns to update were provided.")
    
    updates_str = ', '.join(updates)
    
    parameters.append(service_id)

    update_query = f"UPDATE {TABLE_SERVICE} SET {updates_str} WHERE {SERVICE_ID} = ?"
    cur.execute(update_query, parameters)
    c.commit()



def delete_data(c, service_id):
    cur = c.cursor()
    delete_query = f"DELETE FROM {TABLE_SERVICE} WHERE {SERVICE_ID} = ?"
    cur.execute(delete_query, (service_id,))
    c.commit()

try :

    c = get_connection()

    create_table(c)



except sqlite3.Error as e:
    # except Error as e:
    print(e)