from partitioner import compute_partitions_recursive
from utils import display_polygons

if __name__ == "__main__":
    # DATA
    original_region = [(98, 136), (179, 323), (321, 313), (493, 142), (506, 23), (98, 58)]
    n_partitions = 5

    partitions = compute_partitions_recursive(original_region, n_partitions)
    display_polygons(partitions)
