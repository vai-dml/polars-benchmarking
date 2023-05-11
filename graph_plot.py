import matplotlib.pyplot as plt

def comparison_plot(pd_time, pl_time, title, unit = 'ms'):
    name = ['Pandas', 'Polars']
    values = [pd_time, pl_time]
    
    plt.subplots(figsize=(6,3))
    plt.grid()
    plt.rc('axes', axisbelow=True)
    plt.barh(name, values, color=['#f84a4f','#339e49'], edgecolor='#666', height=.7)
    plt.title(title)
    plt.xlabel(f"Average Time ({unit})")
    plt.show()
    plt.savefig('img/comparison.png')