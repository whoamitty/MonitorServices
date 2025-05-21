import managedb as db


c = db.get_connection()

# les valeurs par défault sont définits à None  ( service_name=None, service_domain=None, service_ip=None )
# db.create_table(c) # Initialiser la table
# db.insert_data(c, "example","example.com")
# db.insert_data(c,service_domain="google.com",service_ip="142.250.217.206") 
db.insert_data(c,service_domain="wikidot.com", service_ip="107.20.139.176")
db.insert_data(c,service_domain="nedbank.co.za")
db.insert_data(c,service_domain="lotro.com")
db.insert_data(c,service_domain="baidu.com")

# db.insert_data( service_name=None, service_domain=None, service_ip=None )

# db.checkNumberFiledTries(c,4) # combien d'essais consécutifs échoués sur l'id 4

# db.modify_data(c, 3, new_numberFiledTries=2)


# db.modify_data(c, service_id=1,new_numberFiledTries=1)

# db.delete_data(c, 123)  # Remplacez 123 par l'identifiant de la ligne à supprimer
