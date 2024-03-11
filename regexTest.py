import re

def extract_sap_and_host_from_config(config_file_path, partner_name):
    with open(config_file_path, 'r') as file:
        config_content = file.read()

    pattern = re.compile(fr'CFTPART\s+ID\s*=\s*\'{partner_name}\'.*?SAP\s*=\s*\(\s*\'(\d+)\'\).*?HOST\s*=\s*\(\s*\'([\d\.]+)\'\)', re.DOTALL)
    match = pattern.search(config_content)

    if match:
        sap = match.group(1)
        host = match.group(2)
        return sap, host
    else:
        return None, None

# Chemin vers le fichier de configuration
config_file_path = r'C:\Users\takwa\OneDrive\Bureau\regex\cft.conf'

# Nom du partenaire à rechercher
partner_name = 'NEWYORK'

# Extraire le port SAP et l'hôte en fonction du nom du partenaire à partir du fichier de configuration
sap, host = extract_sap_and_host_from_config(config_file_path, partner_name)

if sap and host:
    print(f"Pour le partenaire '{partner_name}' - Port SAP : {sap}, Hôte : {host}")
else:
    print(f"Le partenaire '{partner_name}' n'a pas de port SAP ou d'hôte associé dans le fichier de configuration.")