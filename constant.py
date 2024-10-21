PORT="8000"
IPSERVERFLASK="127.0.0.1"
ADRESSE=f"http://{IPSERVERFLASK}"

MAXTRIES=3 #nombre d'éssais consécutifs échoués maximum avant de classer le serveur en indisponible
WAIT=300 # temp d'attente avant chaques essais en secondes
# 300seconds = 5 minutes

TABLE_SERVICE="table_service"
TABLE_ENTERPRISE="table_enterprise"

SERVICE_IP="service_ip"
SERVICE_ID="service_id"
SERVICE_NAME="service_name"
SERVICE_DOMAIN="service_domain"
ENTERPRISE_ID="enterprise_id"
ENTERPRISE_NAME="enterprise_name"
NUMBERFILEDTRIES="numberFiledTries"