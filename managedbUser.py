import managedb as db


c = db.get_connection()

db.create_table(c) # Initialiser la table
db.insert_data(c, "test","test.com", "19.19.19.102")
db.insert_data(c, "example","example.com", "93.184.215.14")
db.insert_data(c, "example","example.com", "93.184.215.14")

db.insert_data(c,service_domain="google.com",service_ip="142.250.217.206") #si service_name est non défini alors service_name=="None"


# db.checkNumberFiledTries(c,4) # combien d'essais consécutifs échoués sur l'id 4

# db.modify_data(c, 3, new_numberFiledTries=2)


# db.modify_data(c, service_id=1,new_numberFiledTries=1)

# db.delete_data(c, 123)  # Remplacez 123 par l'identifiant de la ligne à supprimer