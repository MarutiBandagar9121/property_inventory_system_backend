from sqlalchemy.orm import Session
from app.models.properties import Sublocation


def seed_sublocations(db: Session):
    sublocations = [
        # ── Pune ─────────────────────────────────────────────────────────────
        # Hinjewadi (1)
        {"id": 1,  "name": "Phase 1",              "location_id": 1},
        {"id": 2,  "name": "Phase 2",              "location_id": 1},
        {"id": 3,  "name": "Phase 3",              "location_id": 1},
        # Wakad (2)
        {"id": 4,  "name": "Aundh Hinjewadi Road", "location_id": 2},
        {"id": 5,  "name": "Pimple Saudagar",      "location_id": 2},
        {"id": 6,  "name": "Pimple Nilakh",        "location_id": 2},
        {"id": 7,  "name": "Pimple Garav",         "location_id": 2},
        {"id": 8,  "name": "Tathawade",            "location_id": 2},
        {"id": 9,  "name": "Ravet",                "location_id": 2},
        # Bavdhan (3)
        {"id": 10, "name": "Bhugaon",              "location_id": 3},
        {"id": 11, "name": "NDA Pashan Road",      "location_id": 3},
        # Chinchwad (4)
        {"id": 12, "name": "Akurdi",               "location_id": 4},
        {"id": 13, "name": "Nigdi",                "location_id": 4},
        {"id": 14, "name": "Talwade",              "location_id": 4},
        # Balewadi (5)
        {"id": 15, "name": "Cummins India Road",   "location_id": 5},
        {"id": 16, "name": "Mahalunge",            "location_id": 5},
        # Pashan (6)
        {"id": 17, "name": "Pashan Sus Road",      "location_id": 6},
        # Baner (7)
        {"id": 18, "name": "Baner Road",           "location_id": 7},
        {"id": 19, "name": "Mum-Bang Highway",     "location_id": 7},
        # Kothrud (8)
        {"id": 20, "name": "Karve Nagar",          "location_id": 8},
        {"id": 21, "name": "Paud Road",            "location_id": 8},
        {"id": 22, "name": "Chandni Chowk",        "location_id": 8},
        {"id": 23, "name": "Sinhagad Road",        "location_id": 8},
        {"id": 24, "name": "Nanded",               "location_id": 8},
        {"id": 25, "name": "Warje",                "location_id": 8},
        # Pimpri (9)
        {"id": 26, "name": "Kasarwadi",            "location_id": 9},
        {"id": 27, "name": "Bhosari",              "location_id": 9},
        {"id": 28, "name": "Moshi",                "location_id": 9},
        # Aundh (10)
        {"id": 29, "name": "ITI Road",             "location_id": 10},
        {"id": 30, "name": "University Road",      "location_id": 10},
        {"id": 31, "name": "Bapodi",               "location_id": 10},
        # Erandwane (11)
        {"id": 32, "name": "Prabhat Road",         "location_id": 11},
        {"id": 33, "name": "Law College Road",     "location_id": 11},
        # Khadki (12)
        {"id": 34, "name": "Khadki",               "location_id": 12},
        # Shivaji Nagar (13)
        {"id": 35, "name": "Wakdewadi",            "location_id": 13},
        {"id": 36, "name": "S B Road",             "location_id": 13},
        {"id": 37, "name": "Model Colony",         "location_id": 13},
        {"id": 38, "name": "FC Road",              "location_id": 13},
        {"id": 39, "name": "JM Road",              "location_id": 13},
        {"id": 40, "name": "Bhandarkar Road",      "location_id": 13},
        {"id": 41, "name": "Ganeshkhind Road",     "location_id": 13},
        # Peth Area (14)
        {"id": 42, "name": "Sadashiv Peth",        "location_id": 14},
        {"id": 43, "name": "Raviwar Peth",         "location_id": 14},
        {"id": 44, "name": "Mangalwar Peth",       "location_id": 14},
        {"id": 45, "name": "Agarkar Nagar",        "location_id": 14},
        {"id": 46, "name": "Budhwar Peth",         "location_id": 14},
        {"id": 47, "name": "Pune Contonment",      "location_id": 14},
        # Bund Garden (15)
        {"id": 48, "name": "Sangamvadi",           "location_id": 15},
        {"id": 49, "name": "Camp",                 "location_id": 15},
        # Yerawada (16)
        {"id": 50, "name": "Vishrant Wadi",        "location_id": 16},
        {"id": 51, "name": "Tingre Nagar",         "location_id": 16},
        {"id": 52, "name": "Golf Club Road",       "location_id": 16},
        # Koregaon Park (17)
        {"id": 53, "name": "North Main Road",      "location_id": 17},
        {"id": 54, "name": "Mundhwa",              "location_id": 17},
        # Kalyani Nagar (18)
        {"id": 55, "name": "Kalyani Nagar",        "location_id": 18},
        # Viman Nagar (19)
        {"id": 56, "name": "Wadgaon Sheri",        "location_id": 19},
        {"id": 57, "name": "Ramwadi",              "location_id": 19},
        # Wanowrie (20)
        {"id": 58, "name": "Wanowrie",             "location_id": 20},
        # Kharadi (21)
        {"id": 59, "name": "Eon Free Zone",        "location_id": 21},
        {"id": 60, "name": "Grant Road",           "location_id": 21},
        {"id": 61, "name": "Kharadi Mundhwa Road", "location_id": 21},
        # Hadapsar (22)
        {"id": 62, "name": "Magarpatta",           "location_id": 22},
        {"id": 63, "name": "Amanora",              "location_id": 22},
        {"id": 64, "name": "Fursungi",             "location_id": 22},
        {"id": 65, "name": "Solapur Road",         "location_id": 22},
        # Wagholi (23)
        {"id": 66, "name": "Wagholi",              "location_id": 23},
        # Swargate (24)
        {"id": 67, "name": "Gultekdi",             "location_id": 24},
        {"id": 68, "name": "Bibwewadi",            "location_id": 24},
        {"id": 69, "name": "Katraj",               "location_id": 24},
        {"id": 70, "name": "Shankar Sheth Road",   "location_id": 24},
        # Kondhwa (25)
        {"id": 71, "name": "Nimb",                 "location_id": 25},
        {"id": 72, "name": "Undri",                "location_id": 25},
        {"id": 73, "name": "Lulla Nagar",          "location_id": 25},
        # ── Mumbai ───────────────────────────────────────────────────────────
        # Andheri East (26)
        {"id": 134, "name": "Marol",                  "location_id": 26},
        {"id": 135, "name": "MIDC",                   "location_id": 26},
        {"id": 136, "name": "Saki Naka",              "location_id": 26},
        {"id": 137, "name": "Chakala",                "location_id": 26},
        # Andheri West (27)
        {"id": 138, "name": "Versova",                "location_id": 27},
        {"id": 139, "name": "Lokhandwala",            "location_id": 27},
        {"id": 140, "name": "DN Nagar",               "location_id": 27},
        {"id": 141, "name": "Seven Bungalows",        "location_id": 27},
        # Bandra West (28)
        {"id": 142, "name": "Bandra Reclamation",     "location_id": 28},
        {"id": 143, "name": "Pali Hill",              "location_id": 28},
        {"id": 144, "name": "Mount Mary Road",        "location_id": 28},
        {"id": 145, "name": "Hill Road",              "location_id": 28},
        # Borivali East (29)
        {"id": 146, "name": "Kandarpada",             "location_id": 29},
        {"id": 147, "name": "Dahisar East",           "location_id": 29},
        # Borivali West (30)
        {"id": 148, "name": "IC Colony",              "location_id": 30},
        {"id": 149, "name": "Gorai",                  "location_id": 30},
        {"id": 150, "name": "Chikuwadi",              "location_id": 30},
        # Dadar (31)
        {"id": 151, "name": "Dadar East",             "location_id": 31},
        {"id": 152, "name": "Dadar West",             "location_id": 31},
        {"id": 153, "name": "Shivaji Park",           "location_id": 31},
        # Goregaon East (32)
        {"id": 154, "name": "Aarey Colony",           "location_id": 32},
        {"id": 155, "name": "Jogeshwari East",        "location_id": 32},
        # Goregaon West (33)
        {"id": 156, "name": "Bangur Nagar",           "location_id": 33},
        {"id": 157, "name": "Link Road",              "location_id": 33},
        # Juhu (34)
        {"id": 158, "name": "Juhu Tara Road",         "location_id": 34},
        {"id": 159, "name": "Vile Parle West",        "location_id": 34},
        {"id": 160, "name": "Santacruz West",         "location_id": 34},
        # Kandivali East (35)
        {"id": 161, "name": "Thakur Village",         "location_id": 35},
        {"id": 162, "name": "Samta Nagar",            "location_id": 35},
        # Kandivali West (36)
        {"id": 163, "name": "Charkop",                "location_id": 36},
        {"id": 164, "name": "Mahavir Nagar",          "location_id": 36},
        # Lower Parel (37)
        {"id": 165, "name": "Senapati Bapat Marg",    "location_id": 37},
        {"id": 166, "name": "Prabhadevi",             "location_id": 37},
        {"id": 167, "name": "Worli",                  "location_id": 37},
        # Malad East (38)
        {"id": 168, "name": "Dindoshi",               "location_id": 38},
        {"id": 169, "name": "Malvani",                "location_id": 38},
        # Malad West (39)
        {"id": 170, "name": "Marve Road",             "location_id": 39},
        {"id": 171, "name": "Link Road",              "location_id": 39},
        {"id": 172, "name": "Orlem",                  "location_id": 39},
        # Marine Lines (40)
        {"id": 173, "name": "Churchgate",             "location_id": 40},
        {"id": 174, "name": "Charni Road",            "location_id": 40},
        # Navi Mumbai (41)
        {"id": 175, "name": "Vashi",                  "location_id": 41},
        {"id": 176, "name": "Kharghar",               "location_id": 41},
        {"id": 177, "name": "Nerul",                  "location_id": 41},
        {"id": 178, "name": "Seawoods",               "location_id": 41},
        {"id": 179, "name": "CBD Belapur",            "location_id": 41},
        {"id": 180, "name": "Kopar Khairane",         "location_id": 41},
        # Powai (42)
        {"id": 181, "name": "Marol Pipeline",         "location_id": 42},
        {"id": 182, "name": "Chandivali",             "location_id": 42},
        {"id": 183, "name": "Hiranandani Gardens",    "location_id": 42},
        # Santacruz East (43)
        {"id": 184, "name": "Kalina",                 "location_id": 43},
        {"id": 185, "name": "Vakola",                 "location_id": 43},
        # Santacruz West (44)
        {"id": 186, "name": "Juhu Scheme",            "location_id": 44},
        # Thane (45)
        {"id": 187, "name": "Ghodbunder Road",        "location_id": 45},
        {"id": 188, "name": "Manpada",                "location_id": 45},
        {"id": 189, "name": "Kolshet",                "location_id": 45},
        {"id": 190, "name": "Wagle Estate",           "location_id": 45},
        {"id": 191, "name": "Majiwada",               "location_id": 45},
        # Vashi (46)
        {"id": 192, "name": "Sector 17",              "location_id": 46},
        {"id": 193, "name": "Sector 15",              "location_id": 46},
        {"id": 194, "name": "Sector 19",              "location_id": 46},
        # Worli (47)
        {"id": 195, "name": "Lotus Colony",           "location_id": 47},
        {"id": 196, "name": "Bhuleshwar",             "location_id": 47},
        {"id": 197, "name": "Curry Road",             "location_id": 47},
        # ── Nagpur ───────────────────────────────────────────────────────────
        # Besa (48)
        {"id": 198, "name": "Besa Road",                   "location_id": 48},
        {"id": 199, "name": "Beltarodi",                   "location_id": 48},
        # Civil Lines (49)
        {"id": 200, "name": "Sadar",                       "location_id": 49},
        {"id": 201, "name": "Nagpur Club",                 "location_id": 49},
        {"id": 202, "name": "VCA Stadium",                 "location_id": 49},
        # Dharampeth (50)
        {"id": 203, "name": "Ramdaspeth",                  "location_id": 50},
        {"id": 204, "name": "Laxmi Nagar",                 "location_id": 50},
        {"id": 205, "name": "Gandhibagh",                  "location_id": 50},
        # Hingna (51)
        {"id": 206, "name": "MIDC Hingna",                 "location_id": 51},
        {"id": 207, "name": "Wadi",                        "location_id": 51},
        # Jaripatka (52)
        {"id": 208, "name": "Indora",                      "location_id": 52},
        {"id": 209, "name": "Lalganj",                     "location_id": 52},
        # Kalamna (53)
        {"id": 210, "name": "MIDC Kalamna",                "location_id": 53},
        {"id": 211, "name": "Parsodi",                     "location_id": 53},
        # Koradi (54)
        {"id": 212, "name": "Koradi Thermal Plant",        "location_id": 54},
        {"id": 213, "name": "Koradi Lake",                 "location_id": 54},
        # Manewada (55)
        {"id": 214, "name": "Manewada Road",               "location_id": 55},
        {"id": 215, "name": "Vivekanand Nagar",            "location_id": 55},
        # Mankapur (56)
        {"id": 216, "name": "Mankapur Ring Road",          "location_id": 56},
        {"id": 217, "name": "Chhatrapati Nagar",           "location_id": 56},
        # Nandanvan (57)
        {"id": 218, "name": "Jawahar Nagar",               "location_id": 57},
        {"id": 219, "name": "Nara Road",                   "location_id": 57},
        # Pardi (58)
        {"id": 220, "name": "Bhandewadi",                  "location_id": 58},
        {"id": 221, "name": "Bazargaon",                   "location_id": 58},
        # Ramdaspeth (59)
        {"id": 222, "name": "West High Court Road",        "location_id": 59},
        {"id": 223, "name": "Shankar Nagar",               "location_id": 59},
        # Sakkardara (60)
        {"id": 224, "name": "Sakkardara Road",             "location_id": 60},
        {"id": 225, "name": "Bhagwan Nagar",               "location_id": 60},
        # Sitabuldi (61)
        {"id": 226, "name": "Itwari",                      "location_id": 61},
        {"id": 227, "name": "Gandhibagh",                  "location_id": 61},
        {"id": 228, "name": "Cotton Market",               "location_id": 61},
        # Sonegaon (62)
        {"id": 229, "name": "Sonegaon Lake",               "location_id": 62},
        {"id": 230, "name": "Airport Road",                "location_id": 62},
        # Trimurti Nagar (63)
        {"id": 231, "name": "Trimurti Nagar Ring Road",    "location_id": 63},
        {"id": 232, "name": "Pande Layout",                "location_id": 63},
        # Wardha Road (64)
        {"id": 233, "name": "Butibori MIDC",               "location_id": 64},
        {"id": 234, "name": "Ajni",                        "location_id": 64},
        # Yashodhara Nagar (65)
        {"id": 235, "name": "Yashodhara Nagar Main Road",  "location_id": 65},
        {"id": 236, "name": "Ravindra Nagar",              "location_id": 65},
        # ── Bangalore ────────────────────────────────────────────────────────
        # Bellandur (66)
        {"id": 237, "name": "Bellandur Gate",              "location_id": 66},
        {"id": 238, "name": "Green Glen Layout",           "location_id": 66},
        {"id": 239, "name": "Sobha Dream Acres",           "location_id": 66},
        # Bommanahalli (67)
        {"id": 240, "name": "Hosur Road",                  "location_id": 67},
        {"id": 241, "name": "Rupena Agrahara",             "location_id": 67},
        # BTM Layout (68)
        {"id": 242, "name": "BTM 1st Stage",               "location_id": 68},
        {"id": 243, "name": "BTM 2nd Stage",               "location_id": 68},
        {"id": 244, "name": "MICO Layout",                 "location_id": 68},
        # Electronic City (69)
        {"id": 245, "name": "Phase 1",                     "location_id": 69},
        {"id": 246, "name": "Phase 2",                     "location_id": 69},
        {"id": 247, "name": "Neeladri Nagar",              "location_id": 69},
        # Hebbal (70)
        {"id": 248, "name": "Hebbal Ring Road",            "location_id": 70},
        {"id": 249, "name": "Kempapura",                   "location_id": 70},
        {"id": 250, "name": "Manyata Tech Park",           "location_id": 70},
        # Hennur (71)
        {"id": 251, "name": "Hennur Road",                 "location_id": 71},
        {"id": 252, "name": "Banaswadi",                   "location_id": 71},
        # HSR Layout (72)
        {"id": 253, "name": "Sector 1",                    "location_id": 72},
        {"id": 254, "name": "Sector 2",                    "location_id": 72},
        {"id": 255, "name": "Sector 3",                    "location_id": 72},
        {"id": 256, "name": "Sector 4",                    "location_id": 72},
        # Indiranagar (73)
        {"id": 257, "name": "100 Feet Road",               "location_id": 73},
        {"id": 258, "name": "CMH Road",                    "location_id": 73},
        {"id": 259, "name": "Double Road",                 "location_id": 73},
        # Jayanagar (74)
        {"id": 260, "name": "4th Block",                   "location_id": 74},
        {"id": 261, "name": "9th Block",                   "location_id": 74},
        {"id": 262, "name": "Jayanagar Shopping Complex",  "location_id": 74},
        # JP Nagar (75)
        {"id": 263, "name": "JP Nagar 1st Phase",          "location_id": 75},
        {"id": 264, "name": "JP Nagar 2nd Phase",          "location_id": 75},
        {"id": 265, "name": "JP Nagar 3rd Phase",          "location_id": 75},
        # Kalyan Nagar (76)
        {"id": 266, "name": "HRBR Layout",                 "location_id": 76},
        {"id": 267, "name": "Kammanahalli",                "location_id": 76},
        # Koramangala (77)
        {"id": 268, "name": "1st Block",                   "location_id": 77},
        {"id": 269, "name": "3rd Block",                   "location_id": 77},
        {"id": 270, "name": "4th Block",                   "location_id": 77},
        {"id": 271, "name": "5th Block",                   "location_id": 77},
        {"id": 272, "name": "6th Block",                   "location_id": 77},
        # Mahadevapura (78)
        {"id": 273, "name": "Whitefield Road",             "location_id": 78},
        {"id": 274, "name": "Brookefield",                 "location_id": 78},
        {"id": 275, "name": "Hoodi",                       "location_id": 78},
        # Malleshwaram (79)
        {"id": 276, "name": "Sampige Road",                "location_id": 79},
        {"id": 277, "name": "Margosa Road",                "location_id": 79},
        {"id": 278, "name": "8th Cross",                   "location_id": 79},
        # Marathahalli (80)
        {"id": 279, "name": "Marathahalli Bridge",         "location_id": 80},
        {"id": 280, "name": "Munnekollal",                 "location_id": 80},
        {"id": 281, "name": "Kundalahalli",                "location_id": 80},
        # Nagarbhavi (81)
        {"id": 282, "name": "Nagarbhavi Main Road",        "location_id": 81},
        {"id": 283, "name": "Papareddy Layout",            "location_id": 81},
        # Old Airport Road (82)
        {"id": 284, "name": "Embassy Golf Links",          "location_id": 82},
        {"id": 285, "name": "Domlur",                      "location_id": 82},
        # Rajajinagar (83)
        {"id": 286, "name": "Rajajinagar 1st Block",       "location_id": 83},
        {"id": 287, "name": "Rajajinagar 2nd Block",       "location_id": 83},
        {"id": 288, "name": "Basaveshwara Nagar",          "location_id": 83},
        # Ramamurthy Nagar (84)
        {"id": 289, "name": "Ramamurthy Nagar Main Road",  "location_id": 84},
        {"id": 290, "name": "Garudacharpalya",             "location_id": 84},
        # Sahakar Nagar (85)
        {"id": 291, "name": "Sahakar Nagar Main Road",     "location_id": 85},
        {"id": 292, "name": "Ganganagar",                  "location_id": 85},
        # Sarjapur Road (86)
        {"id": 293, "name": "Kaikondrahalli",              "location_id": 86},
        {"id": 294, "name": "Kasavanahalli",               "location_id": 86},
        {"id": 295, "name": "Carmelaram",                  "location_id": 86},
        # Thanisandra (87)
        {"id": 296, "name": "Thanisandra Main Road",       "location_id": 87},
        {"id": 297, "name": "Nagavara",                    "location_id": 87},
        # Ulsoor (88)
        {"id": 298, "name": "Ulsoor Lake Road",            "location_id": 88},
        {"id": 299, "name": "Halasuru",                    "location_id": 88},
        # Whitefield (89)
        {"id": 300, "name": "ITPL",                        "location_id": 89},
        {"id": 301, "name": "Hope Farm",                   "location_id": 89},
        {"id": 302, "name": "Kadugodi",                    "location_id": 89},
        {"id": 303, "name": "Channasandra",                "location_id": 89},
        # Yelahanka (90)
        {"id": 304, "name": "Yelahanka New Town",          "location_id": 90},
        {"id": 305, "name": "Yelahanka Air Force Station", "location_id": 90},
        {"id": 306, "name": "Attur",                       "location_id": 90},
        # ── Hyderabad ─────────────────────────────────────────────────────────
        # Ameerpet (91)
        {"id": 307, "name": "Greenlands",                  "location_id": 91},
        {"id": 308, "name": "S R Nagar",                   "location_id": 91},
        # Banjara Hills (92)
        {"id": 309, "name": "Road No 1",                   "location_id": 92},
        {"id": 310, "name": "Road No 12",                  "location_id": 92},
        {"id": 311, "name": "Film Nagar",                  "location_id": 92},
        # Begumpet (93)
        {"id": 312, "name": "Begumpet Airport Road",       "location_id": 93},
        {"id": 313, "name": "Prakash Nagar",               "location_id": 93},
        # Boduppal (94)
        {"id": 314, "name": "Boduppal Main Road",          "location_id": 94},
        {"id": 315, "name": "Peerzadiguda",                "location_id": 94},
        # Dilsukhnagar (95)
        {"id": 316, "name": "Chaitanyapuri",               "location_id": 95},
        {"id": 317, "name": "Kothapet",                    "location_id": 95},
        {"id": 318, "name": "Gaddiannaram",                "location_id": 95},
        # Gachibowli (96)
        {"id": 319, "name": "Financial District",          "location_id": 96},
        {"id": 320, "name": "DLF",                         "location_id": 96},
        {"id": 321, "name": "Nanakramguda",                "location_id": 96},
        # Hitech City (97)
        {"id": 322, "name": "Cyber Towers",                "location_id": 97},
        {"id": 323, "name": "Mindspace",                   "location_id": 97},
        {"id": 324, "name": "Raheja Mindspace",            "location_id": 97},
        # Jubilee Hills (98)
        {"id": 325, "name": "Road No 36",                  "location_id": 98},
        {"id": 326, "name": "Road No 45",                  "location_id": 98},
        {"id": 327, "name": "Kavuri Hills",                "location_id": 98},
        # Kachiguda (99)
        {"id": 328, "name": "Kachiguda Station Road",      "location_id": 99},
        {"id": 329, "name": "Narayanguda",                 "location_id": 99},
        # Kompally (100)
        {"id": 330, "name": "Kompally Main Road",          "location_id": 100},
        {"id": 331, "name": "Suchitra Circle",             "location_id": 100},
        # Kondapur (101)
        {"id": 332, "name": "Botanical Garden Road",       "location_id": 101},
        {"id": 333, "name": "Masjid Banda",                "location_id": 101},
        # Kukatpally (102)
        {"id": 334, "name": "KPHB Colony",                 "location_id": 102},
        {"id": 335, "name": "JNTU",                        "location_id": 102},
        {"id": 336, "name": "Nizampet",                    "location_id": 102},
        # Madhapur (103)
        {"id": 337, "name": "Cyber Hills",                 "location_id": 103},
        {"id": 338, "name": "Inorbit Mall Road",           "location_id": 103},
        # Manikonda (104)
        {"id": 339, "name": "Puppalaguda",                 "location_id": 104},
        {"id": 340, "name": "Lanco Hills",                 "location_id": 104},
        # Mehdipatnam (105)
        {"id": 341, "name": "Tolichowki",                  "location_id": 105},
        {"id": 342, "name": "Humayun Nagar",               "location_id": 105},
        # Miyapur (106)
        {"id": 343, "name": "Miyapur Main Road",           "location_id": 106},
        {"id": 344, "name": "Bachupally",                  "location_id": 106},
        # Nallagandla (107)
        {"id": 345, "name": "Nallagandla Main Road",       "location_id": 107},
        {"id": 346, "name": "Tellapur",                    "location_id": 107},
        # Secunderabad (108)
        {"id": 347, "name": "Parade Ground",               "location_id": 108},
        {"id": 348, "name": "MG Road",                     "location_id": 108},
        {"id": 349, "name": "Sainikpuri",                  "location_id": 108},
        # Shamshabad (109)
        {"id": 350, "name": "RGIA Airport",                "location_id": 109},
        {"id": 351, "name": "Shamshabad Main Road",        "location_id": 109},
        # Uppal (110)
        {"id": 352, "name": "Uppal Ring Road",             "location_id": 110},
        {"id": 353, "name": "Ramanthapur",                 "location_id": 110},
        # Vanastalipuram (111)
        {"id": 354, "name": "Vanastalipuram Main Road",    "location_id": 111},
        {"id": 355, "name": "Hayathnagar",                 "location_id": 111},
        # Yapral (112)
        {"id": 356, "name": "Yapral Main Road",            "location_id": 112},
        {"id": 357, "name": "Jawahar Nagar",               "location_id": 112},
        # Zoo Park (113)
        {"id": 358, "name": "Nehru Zoological Park Road",  "location_id": 113},
        {"id": 359, "name": "Bahadurpura",                 "location_id": 113},
        # ── Chennai ───────────────────────────────────────────────────────────
        # Adyar (114)
        {"id": 360, "name": "Gandhi Nagar",                "location_id": 114},
        {"id": 361, "name": "Indira Nagar",                "location_id": 114},
        {"id": 362, "name": "Kasturba Nagar",              "location_id": 114},
        # Ambattur (115)
        {"id": 363, "name": "Ambattur Industrial Estate",  "location_id": 115},
        {"id": 364, "name": "Venkatapuram",                "location_id": 115},
        # Anna Nagar (116)
        {"id": 365, "name": "Anna Nagar East",             "location_id": 116},
        {"id": 366, "name": "Anna Nagar West",             "location_id": 116},
        {"id": 367, "name": "Shenoy Nagar",                "location_id": 116},
        # Besant Nagar (117)
        {"id": 368, "name": "Elliot Beach Road",           "location_id": 117},
        {"id": 369, "name": "Kalakshetra Colony",          "location_id": 117},
        # Chromepet (118)
        {"id": 370, "name": "Chromepet Main Road",         "location_id": 118},
        {"id": 371, "name": "Radha Nagar",                 "location_id": 118},
        # Egmore (119)
        {"id": 372, "name": "Egmore Railway Station",      "location_id": 119},
        {"id": 373, "name": "Poonamallee High Road",       "location_id": 119},
        # Guindy (120)
        {"id": 374, "name": "Guindy Industrial Estate",    "location_id": 120},
        {"id": 375, "name": "Guindy Race Course",          "location_id": 120},
        # Kilpauk (121)
        {"id": 376, "name": "Kilpauk Garden",              "location_id": 121},
        {"id": 377, "name": "Kellys",                      "location_id": 121},
        # KK Nagar (122)
        {"id": 378, "name": "KK Nagar Main Road",          "location_id": 122},
        {"id": 379, "name": "Alwarthiru Nagar",            "location_id": 122},
        # Mogappair (123)
        {"id": 380, "name": "Mogappair East",              "location_id": 123},
        {"id": 381, "name": "Mogappair West",              "location_id": 123},
        # Mylapore (124)
        {"id": 382, "name": "Kapaleeswarar Temple",        "location_id": 124},
        {"id": 383, "name": "Luz Church Road",             "location_id": 124},
        {"id": 384, "name": "Alwarpet",                    "location_id": 124},
        # Nungambakkam (125)
        {"id": 385, "name": "Nungambakkam High Road",      "location_id": 125},
        {"id": 386, "name": "College Road",                "location_id": 125},
        {"id": 387, "name": "Kodambakkam",                 "location_id": 125},
        # OMR (126)
        {"id": 388, "name": "Perungudi",                   "location_id": 126},
        {"id": 389, "name": "Sholinganallur",              "location_id": 126},
        {"id": 390, "name": "Navalur",                     "location_id": 126},
        {"id": 391, "name": "Siruseri",                    "location_id": 126},
        # Perambur (127)
        {"id": 392, "name": "Perambur High Road",          "location_id": 127},
        {"id": 393, "name": "Jawahar Nagar",               "location_id": 127},
        # Porur (128)
        {"id": 394, "name": "Porur Main Road",             "location_id": 128},
        {"id": 395, "name": "Ramapuram",                   "location_id": 128},
        # Purasawalkam (129)
        {"id": 396, "name": "Purasawalkam High Road",      "location_id": 129},
        {"id": 397, "name": "Vepery",                      "location_id": 129},
        # Tambaram (130)
        {"id": 398, "name": "Tambaram East",               "location_id": 130},
        {"id": 399, "name": "Tambaram West",               "location_id": 130},
        {"id": 400, "name": "Selaiyur",                    "location_id": 130},
        # T Nagar (131)
        {"id": 401, "name": "Thyagaraya Road",             "location_id": 131},
        {"id": 402, "name": "Usman Road",                  "location_id": 131},
        {"id": 403, "name": "Pondy Bazaar",                "location_id": 131},
        # Velachery (132)
        {"id": 404, "name": "Vijaya Nagar",                "location_id": 132},
        {"id": 405, "name": "Taramani",                    "location_id": 132},
        {"id": 406, "name": "Pallikaranai",                "location_id": 132},
        # Villivakkam (133)
        {"id": 407, "name": "Villivakkam Main Road",       "location_id": 133},
        {"id": 408, "name": "Kolathur",                    "location_id": 133},
    ]
    existing_ids = {row.id for row in db.query(Sublocation.id).all()}
    for s in sublocations:
        if s["id"] not in existing_ids:
            db.add(Sublocation(**s))
    db.commit()
    print(f"  Sublocations seeded.")
