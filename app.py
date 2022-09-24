import numpy as np #manipulaciones numericas
import pandas as pd #manipular bases de datos
import matplotlib.pyplot as plt #crear bases de datos

inputs = {
    'ruta': './data/',
    'archivo ingresos': 'ingresos.csv',
    'archivo gastos': 'gastos.csv'
}

#construccion de la clase 'calculadora'
class Calculadora:
    
    def __init__(self,inputs):
        
        self.inputs = inputs
        print('Calculadora Activa!')
        
        self.leer_ingresos()
        self.leer_gastos()
        print('Bases de Datos leidas con exito')
    
    #Leer la base de datos ingresos
    def leer_ingresos(self):
        self.ingresos = pd.read_csv(self.inputs['ruta']+self.inputs['archivo ingresos'])
    
    #Leer la base de datos gastos
    def leer_gastos(self):
        self.gastos = pd.read_csv(self.inputs['ruta']+self.inputs['archivo gastos'])
    
    #Calcula los gastos totales usando la columna monto
    def gastos_totales(self):
        total = self.gastos['monto'].sum()
        media = self.gastos['monto'].mean()
        sd = np.sqrt(self.gastos['monto'].var())
        print(f'Tus gastos totales son de ${total}')
        print(f'El gasto promedio fue de ${media} con una desviación estandar de ${sd}')
        print('\n')
        
        #reporte gráfico
        plt.figure()
        
        plt.title('Histograma de Gastos')
        plt.hist(self.gastos['monto'])
        
        plt.show()
        
        return total
    
    #Calcula los ingresos totales usando la columna monto
    def ingresos_totales(self):
        total = self.ingresos['monto'].sum()
        media = self.ingresos['monto'].mean()
        sd = np.sqrt(self.ingresos['monto'].var())
        print(f'Tus ingresos totales son de ${total}')
        print(f'El ingreso promedio fue de ${media} con una desviación estandar de ${sd}')
        print('\n')
        
        #reporte gráfico
        plt.figure()
        
        plt.title('Histograma de Ingresos')
        plt.hist(self.ingresos['monto'])
        
        plt.show()
        
        return total
    
    #Utilizando gastos e ingresos totales, imprime reporte de balance
    def reporte(self):
        gt = self.gastos_totales()
        it = self.ingresos_totales()
        print(f'Tu balance es ${it} - ${gt} = ${it-gt}')
        
    #Agregar nuevos gastos a la base
    def agregar_gasto(self,obs):
        n = len(self.gastos)
        self.gastos.loc[n] = obs
        self.gastos.to_csv(self.inputs['ruta']+self.inputs['archivo gastos'],index=False)
        print('Dato Guardado con Exito!')
    
    #Agregar nuevos ingresos a la base
    def agregar_ingreso(self,obs):
        n = len(self.ingresos)
        self.ingresos.loc[n] = obs
        self.ingresos.to_csv(self.inputs['ruta']+self.inputs['archivo ingresos'],index=False)
        print('Dato Guardado con Exito!')

#instancia y manipulación de la clase
IE = Calculadora(inputs)

IE.reporte()