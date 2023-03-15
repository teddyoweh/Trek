# Trek - Optimal Path Optimization on Geospatial Map

Trek is a Python package that provides functionality for optimizing paths and travel times between nodes on a geospatial map, using graph theory algorithms and simulations. This package can be used to identify the best possible route between two or more points, based on factors such as distance, speed, and other constraints.


### Installation
To install Trek, you can use pip:
```sh
$ python3 pip install trek
```

### Usage
To use Trek, you must first create an instance of the Trek class, which takes a JSON file as input containing the geospatial map data. Once you have initialized a Trek object, you can use its methods to visualize the graph representation of the map, and to find the optimal path between two points.
 
### Data File
Trek uses a JSON file to store the geospatial map data. The file is stored in the same directory as the Python script that uses Trek. The file name is the same as the name of the Python script.

The Location/Node Name is the keys, a hash map of latitude and longitude points are the values

- map.json
```json
{
    "Engineering Buiding":{
        "latitude":32.214256505009985,
        "longitude": -98.21779723918512
    },
     "Library":{
         "latitude":32.215730969726785,
         "longitude": -98.21730569278304
     },
     "Nursing Building":{
         "latitude":32.21664588196621,
         "longitude": -98.22043371534166
     },
     "Centennial":{
        "latitude":32.217553223855305,
        "longitude": -98.2217742964382
    },
     "Rec":{
         "latitude":32.21630562642345,
         "longitude":  -98.2224535241938
     },
      "Science Building":{
         "latitude":     32.216883861659866, 
         "longitude": -98.21972368519181
     },
}
```
### Quickstark
```py
from trek import Trek

# Initialize a Trek object
t = Trek(filename='map.json',env='earth')

# Visualize the graph representation of the map
t.graph()

# Find the optimal path between two points
planned = ['A', 'B', 'C', 'D', 'E']
start = 'A'
end = 'E'
speed = 3.1
best_sol = t.find_optimal_path(planned=planned, start=start, end=end, speed=speed)

# Visualize the optimal path on the map
t.visualize_optimal_path(best_sol['path'], best_sol['times'])

```