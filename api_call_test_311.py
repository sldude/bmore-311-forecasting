import requests
api_url = "https://services1.arcgis.com/UWYHeuuJISiGmgXx/ArcGIS/rest/services/311_Customer_Service_Requests_current/FeatureServer/0/query"

params = {
    "where": "1=1", # no sql filtering
    "outFields": "*", # all output columns
    "resultRecordCount": 1, # 1 record
    "orderByFields": "RowID ASC", # order by rowID column
    "returnGeometry": "false", # no geometry fields in output
    "f": "json" # response format
}

response = requests.get(api_url, params = params, timeout = 30)
print(response.status_code)
print(response.json())
