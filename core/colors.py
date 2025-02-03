import numpy as np


# Define color limits for all 18 elements
# HSV (Hue, Saturation, Value): lower bound to upper bound
color_limits = [
    # Aqua Color
    # Urban infrastructure: Street Light Pole
    (np.array([70, 82, 255]), np.array([90, 255, 255])),

    # Aquamarine Color
    # Mobility Devices: Motorized Wheelchair
    (np.array([78, 129, 241]), np.array([79, 145, 246])),

    # Blue Color
    # Urban infrastructure: Street
    (np.array([120, 247, 255]), np.array([120, 255, 255])),

    # Fuchsia Color
    # Street Furniture: Boullard, Signpost, Bench, Public Trash Can, Swing, Parasol, Advertising Panel
    (np.array([150, 255, 255]), np.array([150, 255, 255])),

    # Green Color
    # Nature: Grass
    (np.array([59, 248, 255]), np.array([60, 255, 255])),

    # Light Amber Color
    # Mobility Devices: Wheelchair
    (np.array([19, 91, 241]), np.array([20, 94, 242])),

    # Light Blue Violet Color
    # Urban infrastructure: Speed Sign, Time Limit Parking Sign
    (np.array([115, 117, 235]), np.array([115, 124, 237])),

    # Light Blue Color
    # Nature: Tree, Plants
    (np.array([106, 71, 235]), np.array([107, 73, 236])),

    # Light Coral Color
    # Mobility Devices: Walker
    (np.array([6, 23, 225]), np.array([9, 42, 235])),

    # Light Crimson
    # Mobility Devices: Orthopedic Crutch
    (np.array([158, 97, 247]), np.array([170, 146, 251])),

    # Light Gray Color
    # Transport: Car, Bus
    (np.array([27, 5, 203]), np.array([38, 12, 206])),

    # Light Khaki Color
    # Street Furniture: Fountain, Monument, Tourist Spot
    (np.array([26, 80, 251]), np.array([26, 88, 252])),

    # Light Olive Color
    # Transport: Bike
    (np.array([37, 79, 217]), np.array([47, 130, 235])),

    # Light Orange Color
    # Mobility Devices: Orthopedic Cane
    (np.array([12, 61, 230]), np.array([15, 95, 236])),

    # Light Teal Color
    # Mobility Devices: Crutch
    (np.array([73, 108, 254]), np.array([74, 111, 255])),

    # Medium Purple Color
    # Transport: Motorcycle, Scooter
    (np.array([138, 59, 176]), np.array([139, 81, 187])),

    # Pale Aqua Color
    # Urban infrastructure: Traffic Light Pole
    (np.array([77, 51, 253]), np.array([86, 60, 254])),

    # Red Color
    # Passerby: People
    (np.array([0, 240, 255]), np.array([0, 255, 255])),

    # Ultra Light Blue
    # Mobility Devices: Cane
    (np.array([90, 40, 230]), np.array([105, 60, 245])),

    # Yellow Color
    # Building: Building
    (np.array([30, 242, 255]), np.array([30, 255, 255]))
]
