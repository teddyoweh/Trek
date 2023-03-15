import json
import time
from decorators import timemycode
import networkx as nx
import matplotlib.pyplot as plt
from math import sin, cos, sqrt, atan2, radians
import math

class Trek(object):
    def __init__(self,filename:str,env:str) -> None:
        """
        :param filename:

        
        """
        if(env.lower()!='earth' or env.lower()!='canvas' ):
            raise ValueError('Invalid environment, use either [earth - lat,log ] or [ canvas -x,y ] ')
        self.env =env.lower()
        self.map = None
        self.map_graph=None

    
        lat_miles_per_degree = 69
        lon_miles_per_degree = 69.172
        with open(filename, 'r') as f:
            self.map = json.load(f)
            
        with open(filename, 'r') as f:
            #self.map = json.load(f)
            self.map_graph=json.load(f)
            if(self.env =='earth'):
                for location in self.map_graph:
                    self.map_graph[location]['latitude'] *= lat_miles_per_degree
                    self.map_graph[location]['longitude'] *= lon_miles_per_degree

    def graph(self):
        """
        Represent the Map from the Data as network graph using nodes to represent positions
        """
        lat_miles_per_degree = 69
        lon_miles_per_degree = 69.172
        if(self.env=='earth'):
            for location in self.map_graph:
                self.map_graph[location]['latitude'] *= lat_miles_per_degree
                self.map_graph[location]['longitude'] *= lon_miles_per_degree
            G = nx.Graph()
            for location in self.map_graph:
                latitude = self.map_graph[location]['latitude']
                longitude = self.map_graph[location]['longitude']
                G.add_node(location, pos=(longitude, latitude))
        elif(self.env=='canvas'):
            G = nx.Graph()
            for location in self.map:
                x = self.map[location]['x']
                y = self.map[location]['y']
                G.add_node(location, pos=(x, y))

        pos = nx.get_node_attributes(G, 'pos')
        nx.draw(G, pos, with_labels=True ,node_color='lightblue', node_size=500, font_size=8)
        plt.show()
    def find_optimal_path(self,planned:list[str], start:str, end:str,speed:float=3.1):
        """
        ### Find the optimal path from the start to the end
        :param planned:
        :param start:
        :param end:
        :param speed:

        ```py
        self.find_optimal_path(planned=planned,start=start,end=end,speed=4.1)
        ```

        """
        if(self.env =='earth'):
            varx,vary = 'latitude','longitude'
        elif(self.env=='canvas'):
                 varx,vary = 'x','y'
        distances = []
        times = []
        for i in range(len(planned) - 1):
            start_lat = self.map_graph[planned[i]][varx]
            start_lon = self.map_graph[planned[i]][vary]
            end_lat = self.map_graph[planned[i+1]][varx]
            end_lon = self.map_graph[planned[i+1]][vary]
            distance = ((end_lat - start_lat)**2 + (end_lon - start_lon)**2)**0.5
            time = self.estimate_time( planned[i], planned[i+1],speed)
            distances.append(distance)
            times.append(time)
        best_path = planned
        best_distance = sum(distances)
        from itertools import permutations
        for path in permutations(planned):
            new_distances = []
            new_times = []
            for i in range(len(path) - 1):
                start_lat = self.map_graph[path[i]][varx]
                start_lon = self.map_graph[path[i]][vary]
                end_lat = self.map_graph[path[i+1]][varx]
                end_lon = self.map_graph[path[i+1]][vary]
                distance = ((end_lat - start_lat)**2 + (end_lon - start_lon)**2)**0.5
                time = self.estimate_time(path[i], path[i+1],speed)
                new_distances.append(distance)
                new_times.append(time)
            new_distance = sum(new_distances)
            new_time = sum(new_times)
            if new_distance < best_distance:
                best_path = path
                best_distance = new_distance
                best_times = new_times
        start_index = best_path.index(start)
        end_index = best_path.index(end)

        if start_index < end_index:
            times_arr = []

            for _ in range(len(best_path[start_index:end_index+1])):
                try:
                    times_arr.append({
                        'start':best_path[start_index:end_index+1][_],
                        'end':best_path[start_index:end_index+1][_+1],
                        'time': best_times[start_index:end_index]
                    })
                except:
                    pass

            return {'path':best_path[start_index:end_index+1], 'detail':times_arr,'times':best_times[start_index:end_index]}
        else:
            times_arr=[]
            for _ in range(len(best_path[start_index:end_index+1])):
                try:
                    times_arr.append({
                        'start':best_path[end_index:start_index+1][::-1][_],
                        'end':best_path[end_index:start_index+1][::-1][_+1],
                        'time':best_times[end_index:start_index][::-1][_]
                })
                except:
                    pass
            return  {'path':best_path[end_index:start_index+1][::-1],'detail':times_arr,'times':best_times[end_index:start_index][::-1]}


 

    def visualize_optimal_path(self, best_path, best_times):
        """
        ### Visualize the routes from path given
        ```py
        best_sol = self.find_optimal_path(planned=planned,start=start,end=end,speed=4.1)
        self.visualize_optimal_path(best_sol['path'],best_sol['times'])
        ```
        """
        if(self.env =='earth'):
            varx,vary = 'latitude','longitude'
        elif(self.env=='canvas'):
                 varx,vary = 'x','y'
        G = nx.Graph()
        node_positions = {}
        node_labels = {}

        for node, data in self.map_graph.items():
            G.add_node(node)
            node_positions[node] = (data[vary], data[varx])
            node_labels[node] = node

        start_node = best_path[0]
        end_node = best_path[-1]

        for i in range(len(best_path)-1):
            G.add_edge(best_path[i], best_path[i+1])

        edge_labels = {}
        for i, edge in enumerate(G.edges()):
            try:
                edge_labels[edge] = f"{best_times[i]:.2f} s"
            except:
                pass

        fig, ax = plt.subplots(figsize=(10, 10))
        nodes_in_order = [node for node in G.nodes() if node in best_path]
        node_colors = ['green' if node == start_node else 'red' if node == end_node else 'blue' for node in nodes_in_order]
        nx.draw(G, pos=node_positions, labels=node_labels, ax=ax, nodelist=nodes_in_order, node_color=node_colors, edge_color='gray', width=1)
        nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels=edge_labels, ax=ax)

        plt.show()
    def estimate_time(self, start:str, end:str,speed:float=3.1)->float:
        """
        ```txt
        :param start: <start_location> 
        :param end: <end_location
        :return <time> minutes
        ```
        
        """
        if(self.env =='earth'):
            varx,vary = 'latitude','longitude'
        elif(self.env=='canvas'):
                    varx,vary = 'x','y'
        lat1, lon1 =self.map_graph[start][varx], self.map_graph[start][vary]
        lat2, lon2 =self.map_graph[end][varx], self.map_graph[end][vary]
        lat_diff = radians(lat2 - lat1)
        lon_diff = radians(lon2 - lon1)
        a = sin(lat_diff / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(lon_diff / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = 3959 * c # 3959  
        # Estimate time based on distance
        #walking_speed = 3.1 # miles per hour

        time = distance / speed
        return time
    @property
    def locations(self)->list[str]:
        """
        ```txt

        Returns an array of Locations for the Map Data
        :return list[str]
        ```
        """
        return list(self.map.keys())
    def distance(self,pos1:str, pos2:str):
        """
        ```txt

        Calculate the distance between two points
        :param pos1 <location_name1>:
        :param pos2 <location_name2>:
        :return: <miles> float
        ```
        
        
        """
        if(self.env =='earth'):
            varx,vary = 'latitude','longitude'
        elif(self.env=='canvas'):
                 varx,vary = 'x','y'
        lat1 = math.radians(self.map[pos1][varx])
        lon1 = math.radians(self.map[pos1][vary])

        lat2 = math.radians(self.map[pos2][varx])
        lon2 = math.radians(self.map[pos2][vary])
        print(self.map[pos1][varx],self.map[pos1][vary])

    
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = 3961 * c  

        return round(distance,1)
    def plot_dot_graph(self):
        if(self.env =='earth'):
            varx,vary = 'latitude','longitude'
        elif(self.env=='canvas'):
                 varx,vary = 'x','y'
        xr=[]
        yr=[]
        for pos1 in self.map:
 
            x = round((self.map[pos1][vary] + 180) / 360 * 10,10)
            y = round((self.map[pos1][varx]+90) / 180 * 10,10)
            xr.append(x)
            yr.append(y)
        fig, ax = plt.subplots()
        ax.plot(xr, yr,'o')
        ax.set_xlabel(f'X - {varx.capitalize()}')
        ax.set_ylabel(f'Y - {vary.capitalize()}')
        ax.set_title('Map')
        plt.show()
    def plot_line_graph(self):
        if(self.env =='earth'):
            varx,vary = 'latitude','longitude'
        elif(self.env=='canvas'):
                 varx,vary = 'x','y'
        xr=[]
        yr=[]
        for pos1 in self.map:
 
            x = round((self.map[pos1][vary] + 180) / 360 * 10,10)
            y = round((self.map[pos1][varx]+90) / 180 * 10,10)
            xr.append(x)
            yr.append(y)
        fig, ax = plt.subplots()
        ax.plot(xr, yr)
        ax.set_xlabel(f'X - {varx.capitalize()}')
        ax.set_ylabel(f'Y - {vary.capitalize()}')
        ax.set_title('Map')
        plt.show()


 
