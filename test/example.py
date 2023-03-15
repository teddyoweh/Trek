from trekpy.Trek import Trek        
path = Trek("data.json",'canvas')

# path.graph()
# print(path.locations)
print(path.estimate_time('A','D',10))
planned =['A','B','C','D']
start = 'A'
end='C'
best_sol = path.find_optimal_path(planned=planned,start=start,end=end,speed=4.1)
print(best_sol)
# path.visualize_optimal_path(best_sol['path'],best_sol['times'])
# print(best_sol['path'])


# print(path.distance('Centennial','Honors Hall'))
# path.plot_dot_graph()