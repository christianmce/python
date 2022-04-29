import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

df = pd. DataFrame ({'horas': [1, 2, 4, 5, 5, 6, 6, 7, 8, 10, 11, 11, 12, 12, 14],
                   'pts': [64, 66, 76, 73, 74, 81, 83, 82, 80, 88, 84, 82, 91, 93, 90]})

print(df [0: 6])

def reglineal(x, y):
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    print(model.summary())
    B0 = model.params[0]
    B1 = model.params[1]
    x = x[:, 1]
    
    # Returna el summary y la grafica
    x2 = np.linspace(x.min(), x.max(), 100)
    y_hat = x2 * B1 + B0
    plt.scatter(x, y, alpha=1) #grafica el scatter plot
    plt.plot(x2, y_hat, 'r', alpha=1) # la linea de regresion en rojo
    plt.xlabel('X Value')
    plt.ylabel('Y Value')
    return model, B0, B1

# Asignación de los datos a las variables X y Y
y = df['pts'].values
x = df['horas'].values

# invocamos la función
reglineal(x, y)
