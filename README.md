<!-- ABOUT THE PROJECT -->
## About The Project

Please, read the following medium [article](https://medium.com/codex/optimal-region-partitioning-for-uavs-and-drones-in-cooperative-flight-settings-c0764a6450f9) to learn more about the implemented partitioning algorithm.

![for drones](https://miro.medium.com/max/1000/1*8Jps5SCEbakugsHMC_8tPQ.png)
![zigzag partitioning](https://miro.medium.com/max/700/1*yU5HS58sK6K41dwyAs9Ttw.png)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Install tkinter
```sh
sudo apt-get install python3-tk
```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mdiamantino/optimal-region-partitioning-convex-polygons-python.git
   ```
2. Enter the cloned directory and create a virtual environment
   ```sh
   cd optimal-region-partitioning-convex-polygons-python/
   ```
   ```sh
   python3 -m venv venv
   ```
3. Activate the virtual environment
   ```sh
   . venv/bin/activate
   ```
4. Install requirements
   ```sh
   pip3 install -r requirements.txt
   ```


<!-- USAGE EXAMPLES -->
## Usage
* Run demo.py to execute the partitioning of [(98, 136), (179, 323), (321, 313), (493, 142), (506, 23), (98, 58)] into 5 sub-regions.
   ```sh
   python3 demo.py
   ```
* Using your own polygon's coordinates and number of partitions (with graphical visualization):   
   ```sh
   python3 main.py
   ```

* Using your own polygon's coordinates and number of partitions (without graphical visualization):
  
  1.
   ```sh
   python3
   ```
  2. 
   ```sh
   >>> from partitioner import compute_partitions_recursive
   ```
  3. compute_partitions_recursive(YOUR COORDINATES HERE, YOUR NUMBER OF PARTITIONS HERE)
  Example:
   ```sh
   >>> compute_partitions_recursive([(0,0),(0,5),(7,7),(4,0)],3)
   ```
* Input your own polygon's coordinates and number of partitions (without visualization):


<!-- CONTACT -->
## Contact

Mark Diamantino Caribé - Mark.Diamantinocaribe@student.kulevuen.be - [LinkedIn](https://be.linkedin.com/in/markdiamantinocaribe)

Project Link: [https://github.com/mdiamantino/optimal-region-partitioning-convex-polygons-python](https://github.com/mdiamantino/optimal-region-partitioning-convex-polygons-python)
