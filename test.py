from helpers import is_url_reachable
from data import URBAN_ROUTES_URL
#To check whether the Urban Routes server is connected and running
if is_url_reachable(URBAN_ROUTES_URL):
    print("Connected to the Urban Routes server")
else:
    print("Cannot connect to Urban Routes.  Check the server is on and still running")