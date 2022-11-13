import numpy as np

TILE_PIXELS = 32

# Map of color names to RGB values
COLORS = {
    "빨간색": np.array([255, 0, 0]),
    "초록색": np.array([0, 255, 0]),
    "파란색": np.array([0, 0, 255]),
    "보라색": np.array([112, 39, 195]),
    "노란색": np.array([255, 255, 0]),
    "회색": np.array([100, 100, 100]),
}

COLOR_NAMES = sorted(list(COLORS.keys()))

# Used to map colors to integers
COLOR_TO_IDX = {"빨간색": 0, "초록색": 1, "파란색": 2, "보라색": 3, "노란색": 4, "회색": 5}

IDX_TO_COLOR = dict(zip(COLOR_TO_IDX.values(), COLOR_TO_IDX.keys()))

# Map of object type to integers
OBJECT_TO_IDX = {
    "unseen": 0,
    "empty": 1,
    "wall": 2,
    "floor": 3,
    "문": 4,
    "열쇠": 5,
    "공": 6,
    "상자": 7,
    "goal": 8,
    "lava": 9,
    "agent": 10,
}

IDX_TO_OBJECT = dict(zip(OBJECT_TO_IDX.values(), OBJECT_TO_IDX.keys()))

# Map of state names to integers
STATE_TO_IDX = {
    "open": 0,
    "closed": 1,
    "locked": 2,
}

# Map of agent direction indices to vectors
DIR_TO_VEC = [
    # Pointing right (positive X)
    np.array((1, 0)),
    # Down (positive Y)
    np.array((0, 1)),
    # Pointing left (negative X)
    np.array((-1, 0)),
    # Up (negative Y)
    np.array((0, -1)),
]
