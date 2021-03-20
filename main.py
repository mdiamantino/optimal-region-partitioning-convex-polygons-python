from partitioner import partition_with_visualization

if __name__ == "__main__":
    coordinates = list(eval(str(input("Input polygon's coordiantes in the format [(x,y),(x',y')...] : "))))
    num_of_partitions = int(input("Input the number of partitions: "))
    partition_with_visualization(coordinates, num_of_partitions)
