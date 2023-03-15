from trekpy.Trek import Trek        
path = Trek("nodes.json",'canvas')

#path.graph()
#print(path.locations)
# print(path.estimate_time('A','D',10))
planned =['Honors', 'Engineering', 'Science', 'Nursing', 'Rec','Lib', 'TNorth', 'Tsouth', 'Cen10', 'Legends', 'Legacy']
start = 'Rec'
end='Lib'
best_sol = path.find_optimal_path(planned=planned,start=start,end=end,speed=4.1)
print(best_sol)
# path.visualize_optimal_path(best_sol['path'],best_sol['times'])
# print(best_sol['path'])


# print(path.distance('Centennial','Honors Hall'))
# path.plot_dot_graph()