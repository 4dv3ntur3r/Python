import requests
from datetime import datetime

USERNAME = "username"
TOKEN = "xxxxxxxxxxxxxxx"
GRAPH_ID = "graph1"

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Setting up a user account on Pixela
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# Creating the graph can access the graph by navigating to https://pixe.la/v1/users/<username>/graphs/graph1.html
#
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Reading Graph",
#     "unit": "Pages",
#     "type": "int",
#     "color": "ajisai",
# }
#
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

today = datetime(year=2022, month=5, day=29)
formatted_date = today.strftime("%Y%m%d")

insert_graph_endpoint = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

update_graph = {
    # do the formatting of date using a method inside datetime module
    "date": formatted_date,
    "quantity": "3",
}

# response = requests.post(url=insert_graph_endpoint, json=update_graph, headers=headers)
# print(response.text)

update_graph_endpoint = f"{insert_graph_endpoint}/{formatted_date}"

update_pixel_params = {
    "quantity": "2",
}

# response = requests.put(url=update_graph_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)

delete_endpoint = update_graph_endpoint

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
