from partitioner import partition_with_visualization


if __name__ == "__main__":
    # DATA
    original_region = [(98, 136), (179, 323), (321, 313), (493, 142), (506, 23), (98, 58)]
    n_partitions = 5

    partition_with_visualization(original_region, n_partitions)