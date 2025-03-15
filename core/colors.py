from typing import Any
import numpy as np


# The class parameters with detailed configuration for all 22 classes
class_parameters: list[dict[str, Any]] = [
    # Building (#85ff0c): Building
    {
        "color_limits": (np.array([40, 49, 210]), np.array([44, 194, 255])),
        "min_area": 50,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (38, 46),
            "s_range": (45, 200),
            "v_range": (205, 255)
        }
    },
    
    # Mobility Devices (#137f49): Motorized Wheelchair
    {
        "color_limits": (np.array([77, 132, 185]), np.array([79, 151, 188])),
        "min_area": 5,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (75, 81),
            "s_range": (130, 153),
            "v_range": (183, 190)
        }
    },

    # Mobility Devices (#13647f): Crutch
    {
        "color_limits": (np.array([92, 132, 183]), np.array([98, 151, 188])),
        "min_area": 5,
        "kernel_size": (4, 4),
        "growth_conditions": {
            "h_type": "circular",   # Wraparound condition
            "h_range": (151, 18),
            "s_range": (72, 193),
            "v_range": (166, 251)
        }
    },
    
    # Mobility Devices (#64137f): Walker
    {
        "color_limits": (np.array([141, 150, 187]), np.array([145, 173, 221])),
        "min_area": 5,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (141, 147),
            "s_range": (140, 183),
            "v_range": (177, 231)
        }
    },

    # Mobility Devices (#7f7f13): Wheelchair
    {
        "color_limits": (np.array([20, 140, 178]), np.array([31, 151, 198])),
        "min_area": 5,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (12, 33),
            "s_range": (41, 180),
            "v_range": (183, 213)
        }
    },

    # Mobility Devices (#13137f): Orthopedic Cane
    {
        "color_limits": (np.array([120, 150, 187]), np.array([129, 163, 205])),
        "min_area": 2,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (120, 129),
            "s_range": (150, 163),
            "v_range": (187, 205)
        }
    },

    # Mobility Devices (#2e7f13): Cane
    {
        "color_limits": (np.array([32, 77, 163]), np.array([72, 163, 214])),
        "min_area": 20,
        "kernel_size": (3, 3),
        "growth_conditions": {
            "h_type": "circular",   # Wraparound condition
            "h_range": (151, 18),
            "s_range": (72, 193),
            "v_range": (166, 251)
        }
    },

    # Mobility Devices (#7f1349): Orthopedic Crutch
    {
        "color_limits": (np.array([161, 149, 187]), np.array([168, 178, 212])),
        "min_area": 5,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (161, 175),
            "s_range": (149, 221),
            "v_range": (187, 243)
        }
    },

    # Nature (#0cffff): Grass
    {
        "color_limits": (np.array([90, 192, 255]), np.array([90, 194, 255])),
        "min_area": 5,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (90, 90),
            "s_range": (192, 194),
            "v_range": (255, 255)
        }
    },

    # Nature (#0cff49): Tree, Plants
    {
        "color_limits": (np.array([73, 192, 255]), np.array([73, 194, 255])),
        "min_area": 5,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (73, 78),
            "s_range": (192, 194),
            "v_range": (255, 255)
        }
    },

    # Passerby (#ff0c0c): Humans
    {
        "color_limits": (np.array([0, 230, 240]), np.array([176, 255, 255])),
        "min_area": 5,
        "kernel_size": (3, 3),
        "growth_conditions": {
            "h_type": "circular",   # Wraparound condition
            "h_range": (151, 18),
            "s_range": (72, 193),
            "v_range": (166, 251)
        }
    },

    # Passerby (#4c2f13): Dogs
    {
        "color_limits": (np.array([15, 191, 76]), np.array([15, 191, 76])),
        "min_area": 5,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (14, 16),
            "s_range": (189, 193),
            "v_range": (74, 78)
        }
    },

    # Street Furniture (#ff0cc2): Boullard, Signpost, Bench, Public Trash Can, Swing, Parasol, Advertising Panel
    {
        "color_limits": (np.array([154, 193, 255]), np.array([155, 194, 255])),
        "min_area": 5,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (154, 155),
            "s_range": (193, 194),
            "v_range": (255, 255)
        }
    },

    # Street Furniture (#21134c): Fountain, Monuments, Tourist Spots
    {
        "color_limits": (np.array([129, 121, 148]), np.array([130, 123, 149])),
        "min_area": 5,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (129, 130),
            "s_range": (121, 123),
            "v_range": (148, 149)
        }
    },

    # Transport (#ffc20c): Car, Bus, Vehicles
    {
        "color_limits": (np.array([25, 192, 255]), np.array([26, 194, 255])),
        "min_area": 5,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (25, 26),
            "s_range": (192, 194),
            "v_range": (255, 255)
        }
    },

    # Transport (#132f4c): Bike
    {
        "color_limits": (np.array([102, 121, 148]), np.array([103, 123, 149])),
        "min_area": 0,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (75, 109),
            "s_range": (75, 185),
            "v_range": (144, 240)
        }
    },

    # Transport (#3e4c13): Motorcycle, Scooter
    {
        "color_limits": (np.array([35, 121, 148]), np.array([36, 123, 149])),
        "min_area": 0,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (3, 147),
            "s_range": (19, 140),
            "v_range": (142, 220)
        }
    },

    # Urban infrastructure (#7f2f13): Street Light Pole
    {
        "color_limits": (np.array([0, 102, 187]), np.array([24, 157, 188])),
        "min_area": 5,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "circular",   # Wraparound condition
            "h_range": (151, 18),
            "s_range": (72, 193),
            "v_range": (166, 251)
        }
    },

    # Urban infrastructure (#1349ff): Streets
    {
        "color_limits": (np.array([107, 193, 255]), np.array([107, 194, 255])),
        "min_area": 0,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (107, 107),
            "s_range": (193, 194),
            "v_range": (255, 255)
        }
    },

    # Urban infrastructure (#134c3e): Speed Sign, Time Limit Parking Sign
    {
        "color_limits": (np.array([82, 117, 148]), np.array([85, 123, 152])),
        "min_area": 0,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (51, 85),
            "s_range": (88, 123),
            "v_range": (148, 189)
        }
    },

    # Urban infrastructure (#134c13): Traffic Light Pole
    {
        "color_limits": (np.array([59, 122, 148]), np.array([60, 123, 150])),
        "min_area": 0,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (49, 76),
            "s_range": (67, 148),
            "v_range": (140, 178)
        }
    },

    # Urban infrastructure (#8513ff): Sidewalks
    {
        "color_limits": (np.array([140, 193, 255]), np.array([140, 194, 255])),
        "min_area": 0,
        "kernel_size": (2, 2),
        "growth_conditions": {
            "h_type": "normal",
            "h_range": (140, 140),
            "s_range": (193, 194),
            "v_range": (255, 255)
        }
    }
]


# The list of color limits in HSV space color for all 22 classes
# lower_bound = np.array(H, S, V), upper_bound = np.array(H, S, V)
color_limits :list = [params["color_limits"] for params in class_parameters]
