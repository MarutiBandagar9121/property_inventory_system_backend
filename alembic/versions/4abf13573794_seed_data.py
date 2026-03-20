"""seed data

Revision ID: 4abf13573794
Revises: 85382ac6354d
Create Date: 2026-03-20 12:54:49.607650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4abf13573794'
down_revision: Union[str, Sequence[str], None] = '85382ac6354d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ── Cities ────────────────────────────────────────────────────────────────
    op.execute("""
        INSERT INTO cities (id, name, state, short_name) VALUES
        (1, 'Pune', 'Maharashtra', 'Pune'),
        (2, 'Mumbai', 'Maharashtra', 'Mumbai'),
        (3, 'Nagpur', 'Maharashtra', 'Nagpur'),
        (4, 'Banglore', 'Karnataka', 'Banglore'),
        (5, 'Hyderabad', 'Telangana', 'Hyderabad'),
        (6, 'Chennai', 'Tamil Nadu', 'Chennai')
        ON CONFLICT DO NOTHING
    """)

    # ── Locations ─────────────────────────────────────────────────────────────
    op.execute("""
        INSERT INTO locations (id, name, city_id, city_division_name, location_type_business) VALUES
        -- Pune
        (1,  'Hinjewadi',     1, 'West Pune', 'Peripheral'),
        (2,  'Wakad',         1, 'West Pune', 'Secondary'),
        (3,  'Bavdhan',       1, 'West Pune', 'Peripheral'),
        (4,  'Chinchwad',     1, 'West Pune', 'Peripheral'),
        (5,  'Balewadi',      1, 'West Pune', 'Secondary'),
        (6,  'Pashan',        1, 'West Pune', 'Secondary'),
        (7,  'Baner',         1, 'West Pune', 'Secondary'),
        (8,  'Kothrud',       1, 'West Pune', 'Secondary'),
        (9,  'Pimpri',        1, 'West Pune', 'Peripheral'),
        (10, 'Aundh',         1, 'West Pune', 'Secondary'),
        (11, 'Erandwane',     1, 'West Pune', 'Secondary'),
        (12, 'Khadki',        1, 'West Pune', 'Secondary'),
        (13, 'Shivaji Nagar', 1, 'West Pune', 'Secondary'),
        (14, 'Peth Area',     1, 'West Pune', 'Secondary'),
        (15, 'Bund Garden',   1, 'West Pune', 'Secondary'),
        (16, 'Yerawada',      1, 'West Pune', 'Secondary'),
        (17, 'Koregaon Park', 1, 'West Pune', 'Secondary'),
        (18, 'Kalyani Nagar', 1, 'West Pune', 'Secondary'),
        (19, 'Viman Nagar',   1, 'West Pune', 'Secondary'),
        (20, 'Wanowrie',      1, 'West Pune', 'Secondary'),
        (21, 'Kharadi',       1, 'West Pune', 'Secondary'),
        (22, 'Hadapsar',      1, 'West Pune', 'Secondary'),
        (23, 'Wagholi',       1, 'West Pune', 'Secondary'),
        (24, 'Swargate',      1, 'West Pune', 'Secondary'),
        (25, 'Kondhwa',       1, 'West Pune', 'Secondary'),
        
        -- Mumbai
        (26, 'Andheri East', 2, 'Western Suburbs', 'Commercial'),
        (27, 'Andheri West', 2, 'Western Suburbs', 'Commercial'),
        (28, 'Bandra West', 2, 'Western Suburbs', 'Premium'),
        (29, 'Borivali East', 2, 'Northern Suburbs', 'Residential'),
        (30, 'Borivali West', 2, 'Northern Suburbs', 'Residential'),
        (31, 'Dadar', 2, 'Central Mumbai', 'Commercial'),
        (32, 'Goregaon East', 2, 'Western Suburbs', 'Residential'),
        (33, 'Goregaon West', 2, 'Western Suburbs', 'Residential'),
        (34, 'Juhu', 2, 'Western Suburbs', 'Premium'),
        (35, 'Kandivali East', 2, 'Northern Suburbs', 'Residential'),
        (36, 'Kandivali West', 2, 'Northern Suburbs', 'Residential'),
        (37, 'Lower Parel', 2, 'Central Mumbai', 'Commercial'),
        (38, 'Malad East', 2, 'Northern Suburbs', 'Residential'),
        (39, 'Malad West', 2, 'Northern Suburbs', 'Residential'),
        (40, 'Marine Lines', 2, 'South Mumbai', 'Premium'),
        (41, 'Navi Mumbai', 2, 'Harbour Region', 'Peripheral'),
        (42, 'Powai', 2, 'Eastern Suburbs', 'Commercial'),
        (43, 'Santacruz East', 2, 'Western Suburbs', 'Residential'),
        (44, 'Santacruz West', 2, 'Western Suburbs', 'Residential'),
        (45, 'Thane', 2, 'Thane District', 'Peripheral'),
        (46, 'Vashi', 2, 'Harbour Region', 'Commercial'),
        (47, 'Worli', 2, 'South Mumbai', 'Premium'),
        (48, 'Besa', 3, 'West Nagpur', 'Residential'),
               
        -- Nagpur
        (49, 'Civil Lines', 3, 'Central Nagpur', 'Commercial'),
        (50, 'Dharampeth', 3, 'Central Nagpur', 'Commercial'),
        (51, 'Hingna', 3, 'West Nagpur', 'Peripheral'),
        (52, 'Jaripatka', 3, 'North Nagpur', 'Residential'),
        (53, 'Kalamna', 3, 'North Nagpur', 'Industrial'),
        (54, 'Koradi', 3, 'North Nagpur', 'Peripheral'),
        (55, 'Manewada', 3, 'East Nagpur', 'Residential'),
        (56, 'Mankapur', 3, 'East Nagpur', 'Residential'),
        (57, 'Nandanvan', 3, 'South Nagpur', 'Residential'),
        (58, 'Pardi', 3, 'South Nagpur', 'Industrial'),
        (59, 'Ramdaspeth', 3, 'Central Nagpur', 'Premium'),
        (60, 'Sakkardara', 3, 'South Nagpur', 'Residential'),
        (61, 'Sitabuldi', 3, 'Central Nagpur', 'Commercial'),
        (62, 'Sonegaon', 3, 'South Nagpur', 'Residential'),
        (63, 'Trimurti Nagar', 3, 'West Nagpur', 'Residential'),
        (64, 'Wardha Road', 3, 'East Nagpur', 'Commercial'),
        (65, 'Yashodhara Nagar', 3, 'West Nagpur', 'Residential'),
               
        -- Banglore
        (66, 'Bellandur', 4, 'East Bangalore', 'Commercial'),
        (67, 'Bommanahalli', 4, 'South Bangalore', 'Commercial'),
        (68, 'BTM Layout', 4, 'South Bangalore', 'Commercial'),
        (69, 'Electronic City', 4, 'South Bangalore', 'Commercial'),
        (70, 'Hebbal', 4, 'North Bangalore', 'Residential'),
        (71, 'Hennur', 4, 'North Bangalore', 'Residential'),
        (72, 'HSR Layout', 4, 'South Bangalore', 'Commercial'),
        (73, 'Indiranagar', 4, 'East Bangalore', 'Premium'),
        (74, 'Jayanagar', 4, 'South Bangalore', 'Commercial'),
        (75, 'JP Nagar', 4, 'South Bangalore', 'Residential'),
        (76, 'Kalyan Nagar', 4, 'East Bangalore', 'Residential'),
        (77, 'Koramangala', 4, 'South Bangalore', 'Premium'),
        (78, 'Mahadevapura', 4, 'East Bangalore', 'Industrial'),
        (79, 'Malleshwaram', 4, 'West Bangalore', 'Commercial'),
        (80, 'Marathahalli', 4, 'East Bangalore', 'Commercial'),
        (81, 'Nagarbhavi', 4, 'West Bangalore', 'Residential'),
        (82, 'Old Airport Road', 4, 'East Bangalore', 'Commercial'),
        (83, 'Rajajinagar', 4, 'West Bangalore', 'Commercial'),
        (84, 'Ramamurthy Nagar', 4, 'East Bangalore', 'Residential'),
        (85, 'Sahakar Nagar', 4, 'North Bangalore', 'Residential'),
        (86, 'Sarjapur Road', 4, 'South Bangalore', 'Commercial'),
        (87, 'Thanisandra', 4, 'North Bangalore', 'Residential'),
        (88, 'Ulsoor', 4, 'Central Bangalore', 'Premium'),
        (89, 'Whitefield', 4, 'East Bangalore', 'Commercial'),
        (90, 'Yelahanka', 4, 'North Bangalore', 'Peripheral'),
               
        -- Hydrabad
        (91, 'Ameerpet', 5, 'Central Hyderabad', 'Commercial'),
        (92, 'Banjara Hills', 5, 'Central Hyderabad', 'Premium'),
        (93, 'Begumpet', 5, 'Central Hyderabad', 'Commercial'),
        (94, 'Boduppal', 5, 'East Hyderabad', 'Residential'),
        (95, 'Dilsukhnagar', 5, 'South Hyderabad', 'Commercial'),
        (96, 'Gachibowli', 5, 'West Hyderabad', 'Commercial'),
        (97, 'Hitech City', 5, 'West Hyderabad', 'Commercial'),
        (98, 'Jubilee Hills', 5, 'West Hyderabad', 'Premium'),
        (99, 'Kachiguda', 5, 'Central Hyderabad', 'Commercial'),
        (100, 'Kompally', 5, 'North Hyderabad', 'Residential'),
        (101, 'Kondapur', 5, 'West Hyderabad', 'Commercial'),
        (102, 'Kukatpally', 5, 'North Hyderabad', 'Residential'),
        (103, 'Madhapur', 5, 'West Hyderabad', 'Commercial'),
        (104, 'Manikonda', 5, 'West Hyderabad', 'Residential'),
        (105, 'Mehdipatnam', 5, 'South Hyderabad', 'Commercial'),
        (106, 'Miyapur', 5, 'North Hyderabad', 'Residential'),
        (107, 'Nallagandla', 5, 'West Hyderabad', 'Peripheral'),
        (108, 'Secunderabad', 5, 'North Hyderabad', 'Commercial'),
        (109, 'Shamshabad', 5, 'South Hyderabad', 'Peripheral'),
        (110, 'Uppal', 5, 'East Hyderabad', 'Residential'),
        (111, 'Vanastalipuram', 5, 'East Hyderabad', 'Residential'),
        (112, 'Yapral', 5, 'North Hyderabad', 'Residential'),
        (113, 'Zoo Park', 5, 'South Hyderabad', 'Residential'),
               
        -- Chennai
        (114, 'Adyar', 6, 'South Chennai', 'Premium'),
        (115, 'Ambattur', 6, 'West Chennai', 'Industrial'),
        (116, 'Anna Nagar', 6, 'Central Chennai', 'Commercial'),
        (117, 'Besant Nagar', 6, 'South Chennai', 'Premium'),
        (118, 'Chromepet', 6, 'South Chennai', 'Residential'),
        (119, 'Egmore', 6, 'Central Chennai', 'Commercial'),
        (120, 'Guindy', 6, 'South Chennai', 'Commercial'),
        (121, 'Kilpauk', 6, 'Central Chennai', 'Residential'),
        (122, 'KK Nagar', 6, 'West Chennai', 'Residential'),
        (123, 'Mogappair', 6, 'West Chennai', 'Residential'),
        (124, 'Mylapore', 6, 'Central Chennai', 'Premium'),
        (125, 'Nungambakkam', 6, 'Central Chennai', 'Commercial'),
        (126, 'OMR', 6, 'South Chennai', 'Commercial'),
        (127, 'Perambur', 6, 'North Chennai', 'Industrial'),
        (128, 'Porur', 6, 'West Chennai', 'Residential'),
        (129, 'Purasawalkam', 6, 'Central Chennai', 'Commercial'),
        (130, 'Tambaram', 6, 'South Chennai', 'Peripheral'),
        (131, 'T Nagar', 6, 'Central Chennai', 'Commercial'),
        (132, 'Velachery', 6, 'South Chennai', 'Commercial'),
        (133, 'Villivakkam', 6, 'West Chennai', 'Residential')
        ON CONFLICT DO NOTHING
    """)

    # ── Sublocations ──────────────────────────────────────────────────────────
    op.execute("""
        INSERT INTO sublocations (id, name, location_id) VALUES
        -- Hinjewadi (1)
        (1,  'Phase 1',              1),
        (2,  'Phase 2',              1),
        (3,  'Phase 3',              1),
        -- Wakad (2)
        (4,  'Aundh Hinjewadi Road', 2),
        (5,  'Pimple Saudagar',      2),
        (6,  'Pimple Nilakh',        2),
        (7,  'Pimple Garav',         2),
        (8,  'Tathawade',            2),
        (9,  'Ravet',                2),
        -- Bavdhan (3)
        (10, 'Bhugaon',              3),
        (11, 'NDA Pashan Road',      3),
        -- Chinchwad (4)
        (12, 'Akurdi',               4),
        (13, 'Nigdi',                4),
        (14, 'Talwade',              4),
        -- Balewadi (5)
        (15, 'Cummins India Road',   5),
        (16, 'Mahalunge',            5),
        -- Pashan (6)
        (17, 'Pashan Sus Road',      6),
        -- Baner (7)
        (18, 'Baner Road',           7),
        (19, 'Mum-Bang Highway',     7),
        -- Kothrud (8)
        (20, 'Karve Nagar',          8),
        (21, 'Paud Road',            8),
        (22, 'Chandni Chowk',        8),
        (23, 'Sinhagad Road',        8),
        (24, 'Nanded',               8),
        (25, 'Warje',                8),
        -- Pimpri (9)
        (26, 'Kasarwadi',            9),
        (27, 'Bhosari',              9),
        (28, 'Moshi',                9),
        -- Aundh (10)
        (29, 'ITI Road',             10),
        (30, 'University Road',      10),
        (31, 'Bapodi',               10),
        -- Erandwane (11)
        (32, 'Prabhat Road',         11),
        (33, 'Law College Road',     11),
        -- Khadki (12)
        (34, 'Khadki',               12),
        -- Shivaji Nagar (13)
        (35, 'Wakdewadi',            13),
        (36, 'S B Road',             13),
        (37, 'Model Colony',         13),
        (38, 'FC Road',              13),
        (39, 'JM Road',              13),
        (40, 'Bhandarkar Road',      13),
        (41, 'Ganeshkhind Road',     13),
        -- Peth Area (14)
        (42, 'Sadashiv Peth',        14),
        (43, 'Raviwar Peth',         14),
        (44, 'Mangalwar Peth',       14),
        (45, 'Agarkar Nagar',        14),
        (46, 'Budhwar Peth',         14),
        (47, 'Pune Contonment',      14),
        -- Bund Garden (15)
        (48, 'Sangamvadi',           15),
        (49, 'Camp',                 15),
        -- Yerawada (16)
        (50, 'Vishrant Wadi',        16),
        (51, 'Tingre Nagar',         16),
        (52, 'Golf Club Road',       16),
        -- Koregaon Park (17)
        (53, 'North Main Road',      17),
        (54, 'Mundhwa',              17),
        -- Kalyani Nagar (18)
        (55, 'Kalyani Nagar',        18),
        -- Viman Nagar (19)
        (56, 'Wadgaon Sheri',        19),
        (57, 'Ramwadi',              19),
        -- Wanowrie (20)
        (58, 'Wanowrie',             20),
        -- Kharadi (21)
        (59, 'Eon Free Zone',        21),
        (60, 'Grant Road',           21),
        (61, 'Kharadi Mundhwa Road', 21),
        -- Hadapsar (22)
        (62, 'Magarpatta',           22),
        (63, 'Amanora',              22),
        (64, 'Fursungi',             22),
        (65, 'Solapur Road',         22),
        -- Wagholi (23)
        (66, 'Wagholi',              23),
        -- Swargate (24)
        (67, 'Gultekdi',             24),
        (68, 'Bibwewadi',            24),
        (69, 'Katraj',               24),
        (70, 'Shankar Sheth Road',   24),
        -- Kondhwa (25)
        (71, 'Nimb',                 25),
        (72, 'Undri',                25),
        (73, 'Lulla Nagar',          25)
        ON CONFLICT DO NOTHING
    """)

    # ── Mumbai Sublocations ──────────────────────────────────────────────────────────
    op.execute("""
        INSERT INTO sublocations (id, name, location_id) VALUES
        -- Andheri East (26)
        (134, 'Marol', 26),
        (135, 'MIDC', 26),
        (136, 'Saki Naka', 26),
        (137, 'Chakala', 26),
        -- Andheri West (27)
        (138, 'Versova', 27),
        (139, 'Lokhandwala', 27),
        (140, 'DN Nagar', 27),
        (141, 'Seven Bungalows', 27),
        -- Bandra West (28)
        (142, 'Bandra Reclamation', 28),
        (143, 'Pali Hill', 28),
        (144, 'Mount Mary Road', 28),
        (145, 'Hill Road', 28),
        -- Borivali East (29)
        (146, 'Kandarpada', 29),
        (147, 'Dahisar East', 29),
        -- Borivali West (30)
        (148, 'IC Colony', 30),
        (149, 'Gorai', 30),
        (150, 'Chikuwadi', 30),
        -- Dadar (31)
        (151, 'Dadar East', 31),
        (152, 'Dadar West', 31),
        (153, 'Shivaji Park', 31),
        -- Goregaon East (32)
        (154, 'Aarey Colony', 32),
        (155, 'Jogeshwari East', 32),
        -- Goregaon West (33)
        (156, 'Bangur Nagar', 33),
        (157, 'Link Road', 33),
        -- Juhu (34)
        (158, 'Juhu Tara Road', 34),
        (159, 'Vile Parle West', 34),
        (160, 'Santacruz West', 34),
        -- Kandivali East (35)
        (161, 'Thakur Village', 35),
        (162, 'Samta Nagar', 35),
        -- Kandivali West (36)
        (163, 'Charkop', 36),
        (164, 'Mahavir Nagar', 36),
        -- Lower Parel (37)
        (165, 'Senapati Bapat Marg', 37),
        (166, 'Prabhadevi', 37),
        (167, 'Worli', 37),
        -- Malad East (38)
        (168, 'Dindoshi', 38),
        (169, 'Malvani', 38),
        -- Malad West (39)
        (170, 'Marve Road', 39),
        (171, 'Link Road', 39),
        (172, 'Orlem', 39),
        -- Marine Lines (40)
        (173, 'Churchgate', 40),
        (174, 'Charni Road', 40),
        -- Navi Mumbai (41)
        (175, 'Vashi', 41),
        (176, 'Kharghar', 41),
        (177, 'Nerul', 41),
        (178, 'Seawoods', 41),
        (179, 'CBD Belapur', 41),
        (180, 'Kopar Khairane', 41),
        -- Powai (42)
        (181, 'Marol Pipeline', 42),
        (182, 'Chandivali', 42),
        (183, 'Hiranandani Gardens', 42),
        -- Santacruz East (43)
        (184, 'Kalina', 43),
        (185, 'Vakola', 43),
        -- Santacruz West (44)
        (186, 'Juhu Scheme', 44),
        -- Thane (45)
        (187, 'Ghodbunder Road', 45),
        (188, 'Manpada', 45),
        (189, 'Kolshet', 45),
        (190, 'Wagle Estate', 45),
        (191, 'Majiwada', 45),
        -- Vashi (46)
        (192, 'Sector 17', 46),
        (193, 'Sector 15', 46),
        (194, 'Sector 19', 46),
        -- Worli (47)
        (195, 'Lotus Colony', 47),
        (196, 'Bhuleshwar', 47),
        (197, 'Curry Road', 47)
        ON CONFLICT DO NOTHING
    """)

    # ── Nagpur Sublocations ──────────────────────────────────────────────────────────
    op.execute("""
        INSERT INTO sublocations (id, name, location_id) VALUES
        -- Besa (48)
        (198, 'Besa Road', 48),
        (199, 'Beltarodi', 48),
        -- Civil Lines (49)
        (200, 'Sadar', 49),
        (201, 'Nagpur Club', 49),
        (202, 'VCA Stadium', 49),
        -- Dharampeth (50)
        (203, 'Ramdaspeth', 50),
        (204, 'Laxmi Nagar', 50),
        (205, 'Gandhibagh', 50),
        -- Hingna (51)
        (206, 'MIDC Hingna', 51),
        (207, 'Wadi', 51),
        -- Jaripatka (52)
        (208, 'Indora', 52),
        (209, 'Lalganj', 52),
        -- Kalamna (53)
        (210, 'MIDC Kalamna', 53),
        (211, 'Parsodi', 53),
        -- Koradi (54)
        (212, 'Koradi Thermal Plant', 54),
        (213, 'Koradi Lake', 54),
        -- Manewada (55)
        (214, 'Manewada Road', 55),
        (215, 'Vivekanand Nagar', 55),
        -- Mankapur (56)
        (216, 'Mankapur Ring Road', 56),
        (217, 'Chhatrapati Nagar', 56),
        -- Nandanvan (57)
        (218, 'Jawahar Nagar', 57),
        (219, 'Nara Road', 57),
        -- Pardi (58)
        (220, 'Bhandewadi', 58),
        (221, 'Bazargaon', 58),
        -- Ramdaspeth (59)
        (222, 'West High Court Road', 59),
        (223, 'Shankar Nagar', 59),
        -- Sakkardara (60)
        (224, 'Sakkardara Road', 60),
        (225, 'Bhagwan Nagar', 60),
        -- Sitabuldi (61)
        (226, 'Itwari', 61),
        (227, 'Gandhibagh', 61),
        (228, 'Cotton Market', 61),
        -- Sonegaon (62)
        (229, 'Sonegaon Lake', 62),
        (230, 'Airport Road', 62),
        -- Trimurti Nagar (63)
        (231, 'Trimurti Nagar Ring Road', 63),
        (232, 'Pande Layout', 63),
        -- Wardha Road (64)
        (233, 'Butibori MIDC', 64),
        (234, 'Ajni', 64),
        -- Yashodhara Nagar (65)
        (235, 'Yashodhara Nagar Main Road', 65),
        (236, 'Ravindra Nagar', 65)
        ON CONFLICT DO NOTHING
    """)

    # ── Bangalore Sublocations ──────────────────────────────────────────────────────────
    op.execute("""
        INSERT INTO sublocations (id, name, location_id) VALUES
        -- Bellandur (66)
        (237, 'Bellandur Gate', 66),
        (238, 'Green Glen Layout', 66),
        (239, 'Sobha Dream Acres', 66),
        -- Bommanahalli (67)
        (240, 'Hosur Road', 67),
        (241, 'Rupena Agrahara', 67),
        -- BTM Layout (68)
        (242, 'BTM 1st Stage', 68),
        (243, 'BTM 2nd Stage', 68),
        (244, 'MICO Layout', 68),
        -- Electronic City (69)
        (245, 'Phase 1', 69),
        (246, 'Phase 2', 69),
        (247, 'Neeladri Nagar', 69),
        -- Hebbal (70)
        (248, 'Hebbal Ring Road', 70),
        (249, 'Kempapura', 70),
        (250, 'Manyata Tech Park', 70),
        -- Hennur (71)
        (251, 'Hennur Road', 71),
        (252, 'Banaswadi', 71),
        -- HSR Layout (72)
        (253, 'Sector 1', 72),
        (254, 'Sector 2', 72),
        (255, 'Sector 3', 72),
        (256, 'Sector 4', 72),
        -- Indiranagar (73)
        (257, '100 Feet Road', 73),
        (258, 'CMH Road', 73),
        (259, 'Double Road', 73),
        -- Jayanagar (74)
        (260, '4th Block', 74),
        (261, '9th Block', 74),
        (262, 'Jayanagar Shopping Complex', 74),
        -- JP Nagar (75)
        (263, 'JP Nagar 1st Phase', 75),
        (264, 'JP Nagar 2nd Phase', 75),
        (265, 'JP Nagar 3rd Phase', 75),
        -- Kalyan Nagar (76)
        (266, 'HRBR Layout', 76),
        (267, 'Kammanahalli', 76),
        -- Koramangala (77)
        (268, '1st Block', 77),
        (269, '3rd Block', 77),
        (270, '4th Block', 77),
        (271, '5th Block', 77),
        (272, '6th Block', 77),
        -- Mahadevapura (78)
        (273, 'Whitefield Road', 78),
        (274, 'Brookefield', 78),
        (275, 'Hoodi', 78),
        -- Malleshwaram (79)
        (276, 'Sampige Road', 79),
        (277, 'Margosa Road', 79),
        (278, '8th Cross', 79),
        -- Marathahalli (80)
        (279, 'Marathahalli Bridge', 80),
        (280, 'Munnekollal', 80),
        (281, 'Kundalahalli', 80),
        -- Nagarbhavi (81)
        (282, 'Nagarbhavi Main Road', 81),
        (283, 'Papareddy Layout', 81),
        -- Old Airport Road (82)
        (284, 'Embassy Golf Links', 82),
        (285, 'Domlur', 82),
        -- Rajajinagar (83)
        (286, 'Rajajinagar 1st Block', 83),
        (287, 'Rajajinagar 2nd Block', 83),
        (288, 'Basaveshwara Nagar', 83),
        -- Ramamurthy Nagar (84)
        (289, 'Ramamurthy Nagar Main Road', 84),
        (290, 'Garudacharpalya', 84),
        -- Sahakar Nagar (85)
        (291, 'Sahakar Nagar Main Road', 85),
        (292, 'Ganganagar', 85),
        -- Sarjapur Road (86)
        (293, 'Kaikondrahalli', 86),
        (294, 'Kasavanahalli', 86),
        (295, 'Carmelaram', 86),
        -- Thanisandra (87)
        (296, 'Thanisandra Main Road', 87),
        (297, 'Nagavara', 87),
        -- Ulsoor (88)
        (298, 'Ulsoor Lake Road', 88),
        (299, 'Halasuru', 88),
        -- Whitefield (89)
        (300, 'ITPL', 89),
        (301, 'Hope Farm', 89),
        (302, 'Kadugodi', 89),
        (303, 'Channasandra', 89),
        -- Yelahanka (90)
        (304, 'Yelahanka New Town', 90),
        (305, 'Yelahanka Air Force Station', 90),
        (306, 'Attur', 90)
        ON CONFLICT DO NOTHING
    """)

    # ── Hyderabad Sublocations ──────────────────────────────────────────────────────────
    op.execute("""
        INSERT INTO sublocations (id, name, location_id) VALUES
        -- Ameerpet (91)
        (307, 'Greenlands', 91),
        (308, 'S R Nagar', 91),
        -- Banjara Hills (92)
        (309, 'Road No 1', 92),
        (310, 'Road No 12', 92),
        (311, 'Film Nagar', 92),
        -- Begumpet (93)
        (312, 'Begumpet Airport Road', 93),
        (313, 'Prakash Nagar', 93),
        -- Boduppal (94)
        (314, 'Boduppal Main Road', 94),
        (315, 'Peerzadiguda', 94),
        -- Dilsukhnagar (95)
        (316, 'Chaitanyapuri', 95),
        (317, 'Kothapet', 95),
        (318, 'Gaddiannaram', 95),
        -- Gachibowli (96)
        (319, 'Financial District', 96),
        (320, 'DLF', 96),
        (321, 'Nanakramguda', 96),
        -- Hitech City (97)
        (322, 'Cyber Towers', 97),
        (323, 'Mindspace', 97),
        (324, 'Raheja Mindspace', 97),
        -- Jubilee Hills (98)
        (325, 'Road No 36', 98),
        (326, 'Road No 45', 98),
        (327, 'Kavuri Hills', 98),
        -- Kachiguda (99)
        (328, 'Kachiguda Station Road', 99),
        (329, 'Narayanguda', 99),
        -- Kompally (100)
        (330, 'Kompally Main Road', 100),
        (331, 'Suchitra Circle', 100),
        -- Kondapur (101)
        (332, 'Botanical Garden Road', 101),
        (333, 'Masjid Banda', 101),
        -- Kukatpally (102)
        (334, 'KPHB Colony', 102),
        (335, 'JNTU', 102),
        (336, 'Nizampet', 102),
        -- Madhapur (103)
        (337, 'Cyber Hills', 103),
        (338, 'Inorbit Mall Road', 103),
        -- Manikonda (104)
        (339, 'Puppalaguda', 104),
        (340, 'Lanco Hills', 104),
        -- Mehdipatnam (105)
        (341, 'Tolichowki', 105),
        (342, 'Humayun Nagar', 105),
        -- Miyapur (106)
        (343, 'Miyapur Main Road', 106),
        (344, 'Bachupally', 106),
        -- Nallagandla (107)
        (345, 'Nallagandla Main Road', 107),
        (346, 'Tellapur', 107),
        -- Secunderabad (108)
        (347, 'Parade Ground', 108),
        (348, 'MG Road', 108),
        (349, 'Sainikpuri', 108),
        -- Shamshabad (109)
        (350, 'RGIA Airport', 109),
        (351, 'Shamshabad Main Road', 109),
        -- Uppal (110)
        (352, 'Uppal Ring Road', 110),
        (353, 'Ramanthapur', 110),
        -- Vanastalipuram (111)
        (354, 'Vanastalipuram Main Road', 111),
        (355, 'Hayathnagar', 111),
        -- Yapral (112)
        (356, 'Yapral Main Road', 112),
        (357, 'Jawahar Nagar', 112),
        -- Zoo Park (113)
        (358, 'Nehru Zoological Park Road', 113),
        (359, 'Bahadurpura', 113)
        ON CONFLICT DO NOTHING
    """)

    # ── Chennai Sublocations ──────────────────────────────────────────────────────────
    op.execute("""
        INSERT INTO sublocations (id, name, location_id) VALUES
        -- Adyar (114)
        (360, 'Gandhi Nagar', 114),
        (361, 'Indira Nagar', 114),
        (362, 'Kasturba Nagar', 114),
        -- Ambattur (115)
        (363, 'Ambattur Industrial Estate', 115),
        (364, 'Venkatapuram', 115),
        -- Anna Nagar (116)
        (365, 'Anna Nagar East', 116),
        (366, 'Anna Nagar West', 116),
        (367, 'Shenoy Nagar', 116),
        -- Besant Nagar (117)
        (368, 'Elliot Beach Road', 117),
        (369, 'Kalakshetra Colony', 117),
        -- Chromepet (118)
        (370, 'Chromepet Main Road', 118),
        (371, 'Radha Nagar', 118),
        -- Egmore (119)
        (372, 'Egmore Railway Station', 119),
        (373, 'Poonamallee High Road', 119),
        -- Guindy (120)
        (374, 'Guindy Industrial Estate', 120),
        (375, 'Guindy Race Course', 120),
        -- Kilpauk (121)
        (376, 'Kilpauk Garden', 121),
        (377, 'Kellys', 121),
        -- KK Nagar (122)
        (378, 'KK Nagar Main Road', 122),
        (379, 'Alwarthiru Nagar', 122),
        -- Mogappair (123)
        (380, 'Mogappair East', 123),
        (381, 'Mogappair West', 123),
        -- Mylapore (124)
        (382, 'Kapaleeswarar Temple', 124),
        (383, 'Luz Church Road', 124),
        (384, 'Alwarpet', 124),
        -- Nungambakkam (125)
        (385, 'Nungambakkam High Road', 125),
        (386, 'College Road', 125),
        (387, 'Kodambakkam', 125),
        -- OMR (126)
        (388, 'Perungudi', 126),
        (389, 'Sholinganallur', 126),
        (390, 'Navalur', 126),
        (391, 'Siruseri', 126),
        -- Perambur (127)
        (392, 'Perambur High Road', 127),
        (393, 'Jawahar Nagar', 127),
        -- Porur (128)
        (394, 'Porur Main Road', 128),
        (395, 'Ramapuram', 128),
        -- Purasawalkam (129)
        (396, 'Purasawalkam High Road', 129),
        (397, 'Vepery', 129),
        -- Tambaram (130)
        (398, 'Tambaram East', 130),
        (399, 'Tambaram West', 130),
        (400, 'Selaiyur', 130),
        -- T Nagar (131)
        (401, 'Thyagaraya Road', 131),
        (402, 'Usman Road', 131),
        (403, 'Pondy Bazaar', 131),
        -- Velachery (132)
        (404, 'Vijaya Nagar', 132),
        (405, 'Taramani', 132),
        (406, 'Pallikaranai', 132),
        -- Villivakkam (133)
        (407, 'Villivakkam Main Road', 133),
        (408, 'Kolathur', 133)
        ON CONFLICT DO NOTHING
    """)

    # ── Property Types ────────────────────────────────────────────────────────
    op.execute("""
        INSERT INTO property_types (id, name) VALUES
        (1, 'Office_Commercial_Space'),
        (2, 'Standalone_Retail'),
        (3, 'Mall'),
        (4, 'Land'),
        (5, 'Logistics'),
        (6, 'Industrial')
        ON CONFLICT DO NOTHING
    """)

    # ── Node Types ────────────────────────────────────────────────────────────
    op.execute("""
        INSERT INTO node_types (id, name) VALUES
        (1, 'BUILDING'),
        (2, 'WING'),
        (3, 'FLOOR'),
        (4, 'UNIT'),
        (5, 'LAND'),
        (6, 'INDUSTRIAL'),
        (7, 'LOGISTICS'),
        (8, 'RETAIL_UNIT'),
        (9, 'SHARED_OFFICE')
        ON CONFLICT DO NOTHING
    """)


def downgrade() -> None:
    # Delete in reverse FK order to respect constraints
    op.execute("DELETE FROM sublocations WHERE id BETWEEN 1 AND 408")
    op.execute("DELETE FROM locations WHERE id BETWEEN 1 AND 133")
    op.execute("DELETE FROM cities WHERE id BETWEEN 1 AND 6")
    op.execute("DELETE FROM property_types WHERE id BETWEEN 1 AND 6")
    op.execute("DELETE FROM node_types WHERE id BETWEEN 1 AND 9")
