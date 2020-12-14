#Used to store information for a single restaurant
class restaurant:
    def __init__(self, name, hours, location, menu, dine_in, to_go, curbside, p_number, website):
        self.name = name
        self.hours = hours
        self.location = location #zip code
        self.menu = menu#link to menu on website
        self.dine_in = dine_in
        self.to_go = to_go
        self.curbside = curbside
        self.p_number = p_number
        self.website = website
    
    def print_all(self):
        print("Name: ", self.name)
        print("Hours: ", self.hours)
        print("Location: ", self.location)
        print("Link to menu: ", self.menu)
        print("Currently offering Dine in service: ", self.dine_in)
        print("Currently offering To-Go ordering:", self.to_go)
        print("Currently offering Curbside pickup: ", self.curbside)
        print("Phone number: ", self.p_number)
        print("Website: ", self.website)
    
    def check_name(self, name):
        if(self.name == name):
            return True
        return False

    def check_loc(self, location):
        if(self.location == location):
            return True
        return False

#will store all restaurants.
rests = [restaurant("Applebees", "12PM-12AM", "95829", "https://www.applebees.com/en/menu", True, True, True, "1 (888) 592-7753", "https://www.applebees.com/en"),
         restaurant("Applebees", "12PM-12AM", "92870", "https://www.applebees.com/en/menu", True, True, True, "1 (888) 592-7753", "https://www.applebees.com/en"),
         restaurant("Red Lobster", "11:30AM-9:30PM", "95829", "https://www.redlobster.com/menu", False, True, True, "(916) 921-6011", "https://www.redlobster.com/"),
         restaurant("Cheesecake Factory", "11AM-9PM", "95829", "https://www.thecheesecakefactory.com/menu/", True, True, True, "916-567-0606", "https://www.thecheesecakefactory.com/"),
         restaurant("Chilis", "11AM-10PM", "92870", "https://www.chilis.com/menu", False, True, True, "(714) 524-8162", "https://www.chilis.com/"),
         restaurant("Chevys", "11AM-10PM", "95829", "https://www.chevys.com/menus/", True, True, True, "(916) 691-3400", "https://www.chevys.com/")]

counties = [
"Alameda" ,
"Alpine" ,
"Amador" ,
"Butte" ,
"Calaveras" ,
"Colusa" ,
"Contra Costa" ,
"Del Norte" ,
"El Dorado" ,
"Fresno" ,
"Glenn" ,
"Humboldt" ,
"Imperial" ,
"Inyo" ,
"Kern" ,
"Kings" ,
"Lake" ,
"Lassen" ,
"Los Angeles" ,
"Madera" ,
"Marin" ,
"Mariposa" ,
"Mendocino" ,
"Merced" ,
"Modoc" ,
"Mono" ,
"Monterey" ,
"Napa" ,
"Nevada" ,
"Orange" ,
"Placer" ,
"Plumas" ,
"Riverside" ,
"Sacramento" ,
"San Benito" ,
"San Bernardino" ,
"San Diego" ,
"San Francisco" ,
"San Joaquin" ,
"San Luis Obispo" ,
"San Mateo" ,
"Santa Barbara" ,
"Santa Clara" ,
"Santa Cruz" ,
"Shasta" ,
"Sierra" ,
"Siskiyou" ,
"Solano" ,
"Sonoma" ,
"Stanislaus" ,
"Sutter" ,
"Tehama" ,
"Trinity" ,
"Tulare" ,
"Tuolumne" ,
"Ventura" ,
"Yolo" ,
"Yuba" ,]

"""
Step 1: Asks how you would like to search name or location.
Step 2a (loc): Asks for zip code of the location you want. Will display every restaurant in that area and all information about the restaurant
Step 2b (Name): Asks for name of the restaurant you want to find. Will display every restaurant with that name and all information about the restaurant
"""
def search_rest(WB_test, search_type, search_value):
    is_done = False
    exit_flag = False
    is_loc = True #checks to see if we are searching by location or name
    num_rests = 0 #used to see if we have a restaurant in that area or with that name

    s1a_flag = False
    s1b_flag = False
    s2a1_flag = False
    s2a2_flag = False
    s2b1_flag = False
    s2b2_flag = False

    #step 1
    while(is_done == False):
        if(WB_test == False):
            what_search = input("Would you like to search by location or name? Please enter 'location' for location or 'name' for name or 'quit' for main menu: ")
        else:
            what_search = search_type
        if(what_search == "location"):
            is_loc = True
            is_done = True
            s1a_flag = True
        elif(what_search == "name"):
            is_loc = False
            is_done = True
            s1b_flag = True
        elif(what_search == "quit"):
            is_done = True
            exit_flag = True
        else:
            print(what_search, "is an invalid command.")

    #STEP 2a
    if(is_loc == True and exit_flag == False):
        is_done = False
        while(is_done == False):
            if(WB_test == False):
                zip_code = input("Please enter in the zip code of the location you would like to search or type 'quit' to exit to main menu: ")
            else:
                zip_code = search_value
                is_done = True
            if(zip_code == "quit"):
                is_done = True
            else:
                for i in range(len(rests)):
                    if(rests[i].check_loc(zip_code)):
                        if(WB_test == False):
                            print()
                            rests[i].print_all()
                            print()
                        num_rests = num_rests + 1
                    
                if(num_rests == 0):
                    if(WB_test == False):
                        print("I'm sorry. We do not have any restaurants in that area.")
                    s2a2_flag = True
                else:
                    s2a1_flag = True
                num_rests = 0
    #STEP 2b
    elif(is_loc == False and exit_flag == False):
        is_done = False
        while(is_done == False):
            if(WB_test == False):
                name = input("Please enter in the name of the restaurant you would like to search or type 'quit' to exit to main menu: ")
            else:
                name = search_value
                is_done = True
            if(name == "quit"):
                is_done = True
            else:
                for i in range(len(rests)):
                    if(rests[i].check_name(name)):
                        if(WB_test == False):
                            print()
                            rests[i].print_all()
                            print()
                        num_rests = num_rests + 1
                    
                if(num_rests == 0):
                    if(WB_test == False):
                        print("I'm sorry. We do not know of any restaurants with that name.")
                    s2b2_flag = True
                else:
                    s2b1_flag = True
                num_rests = 0

    if(WB_test == True):
        if(what_search == "location"):
            if(s1a_flag == True):
                print("Testing location search:")
            else:
                print("Error in location search")
        elif(what_search == "name"):
            if(s1b_flag == True):
                print("Testing name search:")
            else:
                print("Error in name search")
        
        print("Value given: ", search_value)

        if(s2a1_flag == True):
            print("Location found")
        elif(s2a2_flag == True):
            print("Location not found")
        elif(s2b1_flag == True):
            print("Name found")
        elif(s2b2_flag == True):
            print("Name not found")
        else:
            print("ERROR! Search returned no valid values")
        print()
        print()

"""
Will ask you whether you want to find a restaurant or get COVID19 details in your area.
Only have the find restaurant subprogram completed.
"""
def search_loc(WB_test, search_value):
    is_done = False
    s1a_flag = False
    s1b_flag = False

    while(is_done == False):
        is_county = False
        if(WB_test == False):
            name = input("Please enter in the name of the county you would like to search or type 'quit' to exit to main menu: ")
        else:
            name = search_value
        for i in range(58):
            if(name == counties[i]):
                is_county = True
                break
        if(is_county == True):
            s1a_flag = True
            if(WB_test == False):
                county_name = ""
                for i in range(len(name)):
                    if(name[i] == ' '):
                        county_name = county_name + '-'
                    else:
                        county_name = county_name + name[i]
                print("Use this link to get COVID-19 information: https://usafacts.org/visualizations/coronavirus-covid-19-spread-map/state/california/county/" + county_name + "-county")
            else:
                is_done = True
        elif(name == "quit"):
            is_done = True
        else:
            s1b_flag = True
            if(WB_test == False):
                print("Please enter a valid County")
            else:
                is_done = True
    if(WB_test == True):
        print("Testing finding COVID details")
        print("Value given: ", search_value)
        if(s1a_flag == True):
            print("Found County")
        elif(s1b_flag == True):
            print("County not found")
        print()
        print()



if __name__ == "__main__":
    WB_test = False
    is_done = False
    current_search = ""
    if(WB_test == True):
        print("White Box Testing")
        search_rest(True, "location", "95829")
        search_rest(True, "location", "sdjfdsajfha")
        search_rest(True, "name", "Applebees")
        search_rest(True, "name", "sdjfdsajfha")
        search_loc(True, "Orange")
        search_loc(True, "sdjfdsajfha")
    else:
        print("Hello and welcome to Restaurant Checker.")
        while(is_done == False):
            print("Would you like to search for a restaurant or check COVID-19 information in your area? Please type 'rest' for restaurants or 'C19' for COVID19 details or 'quit' to quit:", end = " ")
            current_search = input()
            if(current_search == "rest"):
                search_rest(False, "", "")
            elif(current_search =="C19"):
                search_loc(False, "")
            elif(current_search == "quit"):
                print("Thank you for using our service")
                is_done = True
            else:
                print(current_search, "is an invalid command.")
