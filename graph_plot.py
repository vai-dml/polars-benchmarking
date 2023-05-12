import matplotlib.pyplot as plt

def comparison_plot(pd_time, pyarrow_time, pl_time, title, unit = 's'):
    name = ['Pandas 1.0','Pandas 2.0','Polars']
    values = [pd_time, pyarrow_time, pl_time]
    
    plt.subplots(figsize=(8,4))
    plt.grid()
    plt.rc('axes', axisbelow=True)
    plt.barh(name, values, color=['#f84a4f','#339e49', '#006cff'], edgecolor='#666', height=.7)
    plt.title(title)
    plt.xlabel(f"Average Time ({unit})")
    plt.show()
    #plt.savefig('img/comparison.png')