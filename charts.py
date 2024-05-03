
import re
import matplotlib.pyplot as plt
#import matplotlib
import sys


def generate_bar_chart():
    labels = ['a', 'b', 'c']
    values = [100, 300 , 344]
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.show()

def generate_bar_chart(labels, values, country):
    # Tamaño en pulgadas = píxeles / dpi, aquí usamos 1080 píxeles y 100 dpi como ejemplo
    # dpi = 100
    # fig_size = 1080 / dpi  # 1080 píxeles / 100 dpi = 10.8 pulgadas
    # fig, ax = plt.subplots(figsize=(fig_size, fig_size), dpi=dpi)
    fig, ax = plt.subplots()
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'pink', 'cyan', 'gold']
    bars = ax.bar(labels, values, color = colors)
    ax.bar_label(bars)
    ax.set_title('Population of:  '+ country)
    ax.set_xlabel('Years')  
    ax.set_ylabel('Populations in Millions') 
    plt.savefig(country+'.png')
    plt.show()
    #plt.savefig(country+'.png', dpi=dpi)  # Asegura que la resolución sea suficiente para 1080x1080
    

 
def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels) 
    ax.axis('equal')
    plt.show()
       
if __name__ == '__main__':
   labels = ['a', 'b', 'c', 'r']
   values = [100, 1000 ,34 , 33]
   generate_bar_chart(labels,values)
   generate_pie_chart(labels,values)
   #print(sys.path)


