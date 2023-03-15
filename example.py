from Trek import Trek        
path = Trek("data.json")

path.graph()
print(path.locations)
print(path.estimate_time('Honors Hall','Centennial'))
planned =['Engineering Buiding',
'Library',
'Nursing Building',
'Centennial',
'Rec',
'Dining Hall',
'Science Building',
'Student Center']
start = 'Dining Hall'
end='Rec'
best_sol = path.find_optimal_path(planned=planned,start=start,end=end,speed=4.1)
print(best_sol)
path.visualize_optimal_path(best_sol['path'],best_sol['times'])
print(best_sol['path'])


print(path.distance('Centennial','Honors Hall'))
path.plot_dot_graph()