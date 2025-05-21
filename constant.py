PORT="8000"
IPSERVERFLASK="127.0.0.1"
ADRESSE=f"http://{IPSERVERFLASK}"

#nombre d'éssais consécutifs échoués maximum avant de classer le serveur en indisponible
MAXTRIES=3 

WAIT=120 # temps d'attente avant chaques essais en secondes
# 120seconds = 2 minutes
# 300seconds = 5 minutes

TABLE_SERVICE="table_service"

SERVICE_ID="service_id"
SERVICE_NAME="service_name"
SERVICE_DOMAIN="service_domain"
SERVICE_IP="service_ip"
NUMBERFILEDTRIES="numberFiledTries"

# Des constantes qui ne sont finalement pas utilisés
# TABLE_ENTERPRISE="table_enterprise"
# ENTERPRISE_ID="enterprise_id"
# ENTERPRISE_NAME="enterprise_name"

