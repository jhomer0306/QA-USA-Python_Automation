import data
import helpers

class TestUrbanRoutes:

# setup_class is used to establish a single connection to Urban Routes server
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")
            exit()
# URL is specified in data.py.
# If the Urban Routes server is reachable, print "Connected...".  Otherwise, print "cannot connect..."
# Check server connection before proceeding with other tests.  Other tests will fail if server has expired.

    def test_set_route(self):
        # placeholder for setting a route; will be expanded in later steps
        # Add in S8
        print("Function created for setting route")
        pass

    def test_select_route(self):
        # placeholder for selecting a route; will be expanded in later steps
        # Add in S8
        print("Function created for selecting route")
        pass

    def test_fill_phone_number(self):
        # placeholder for filling in a phone number; will be expanded in later steps
        # Add in S8
        print("Function created for filling phone number")
        pass

    def test_fill_card(self):
        # placeholder for filling in card details; will be expanded in later steps
        # Add in S8
        print("Function created for filling card details")
        pass

    def test_comment_for_driver(self):
        # placeholder for leaving driver a comment; will be expanded in later steps
        # Add in S8
        print("Function created for leaving driver a comment")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # placeholder for ordering blanket/handkerchief; will be expanded in later steps
        # Add in S8
        print("Function created for ordering blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # placeholder for ordering two ice creams; will be expanded in later steps
        # Add in S8
        number_of_ice_creams = 2
        for test_order in range(number_of_ice_creams):
        # Loop to simulate ordering two ice creams
        #Add in S8
            print(f"Function created for ordering ice cream #{test_order +1}")
        # Prints separately for ice cream #1 and ice cream #2
            pass

    def test_car_search_model_appears(self):
        # placeholder for car search model; will be expanded in later steps
        # Add in S8
        print("Function created for car search model appears")
        pass
