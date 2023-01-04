import requests

# Parameters for the API call.
lang = "en-GB"
sort_by = "Relevance"
sector = "7845"
page = "1"
page_size = "5"
data_type = "json"

url = (
    f"https://api1-ratings.food.gov.uk/enhanced-search/"
    f"{lang}/%5E/%5E/{sort_by}/{sector}/%5E/%5E/0/{page}/"
    f"{page_size}/{data_type}"
)

# Fetch the data using the API.
r = requests.get(url)
j_data = r.json()

# Extract the establishments data from the raw data.
estab_data = j_data["FHRSEstablishment"]["EstablishmentCollection"][
    "EstablishmentDetail"
]

# Filter the data to only the first locality.
local_data = [
    estab
    for estab in estab_data
    if estab["LocalAuthorityName"] == estab_data[0]["LocalAuthorityName"]
]
