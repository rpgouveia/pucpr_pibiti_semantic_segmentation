import numpy as np


# The color limits in HSV space color for all 22 classes
# lower_bound = np.array(H, S, V) and upper_bound = np.array(H, S, V)
color_limits = [
    # Building (#85ff0c): Building
    (np.array([40, 49, 210]), np.array([44, 194, 255])),
    
    # Mobility Devices (#137f49): Motorized Wheelchair
    (np.array([77, 132, 185]), np.array([79, 151, 188])),

    # Mobility Devices (#13647f): Crutch
    (np.array([92, 132, 183]), np.array([98, 151, 188])),
    
    # Mobility Devices (#64137f): Walker
    (np.array([141, 150, 187]), np.array([145, 173, 221])),

    # Mobility Devices (#7f7f13): Wheelchair
    (np.array([20, 140, 178]), np.array([31, 151, 198])),

    # Mobility Devices (#13137f): Orthopedic Cane
    (np.array([120, 150, 187]), np.array([129, 163, 205])),

    # Mobility Devices (#2e7f13): Cane
    (np.array([32, 77, 163]), np.array([72, 163, 214])),

    # Mobility Devices (#7f1349): Orthopedic Crutch
    (np.array([161, 149, 187]), np.array([168, 178, 212])),

    # Nature (#0cffff): Grass
    (np.array([90, 192, 255]), np.array([90, 194, 255])),

    # Nature (#0cff49): Tree, Plants
    (np.array([73, 192, 255]), np.array([73, 194, 255])),

    # Passerby (#ff0c0c): Humans
    (np.array([0, 230, 240]), np.array([176, 255, 255])),

    # Passerby (#4c2f13): Dogs
    (np.array([15, 191, 76]), np.array([15, 191, 76])),

    # Street Furniture (#ff0cc2): Boullard, Signpost, Bench, Public Trash Can, Swing, Parasol, Advertising Panel
    (np.array([154, 193, 255]), np.array([155, 194, 255])),

    # Street Furniture (#21134c): Fountain, Monuments, Tourist Spots
    (np.array([129, 121, 148]), np.array([130, 123, 149])),

    # Transport (#ffc20c): Car, Bus, Vehicles
    (np.array([25, 192, 255]), np.array([26, 194, 255])),

    # Transport (#132f4c): Bike
    (np.array([102, 121, 148]), np.array([103, 123, 149])),

    # Transport (#3e4c13): Motorcycle, Scooter
    (np.array([35, 121, 148]), np.array([36, 123, 149])),

    # Urban infrastructure (#7f2f13): Street Light Pole
    (np.array([0, 102, 187]), np.array([24, 157, 188])),

    # Urban infrastructure (#1349ff): Streets
    (np.array([107, 193, 255]), np.array([107, 194, 255])),

    # Urban infrastructure (#134c3e): Speed Sign, Time Limit Parking Sign
    (np.array([82, 117, 148]), np.array([85, 123, 152])),

    # Urban infrastructure (#134c13): Traffic Light Pole
    (np.array([59, 122, 148]), np.array([60, 123, 150])),

    # Urban infrastructure (#8513ff): Sidewalks
    (np.array([140, 193, 255]), np.array([140, 194, 255]))
]
