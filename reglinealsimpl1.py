import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd

df = pd. DataFrame ({'horas': [1, 2, 4, 5, 5, 6, 6, 7, 8, 10, 11, 11, 12, 12, 14,14],
                   'pts': [64, 66, 76, 73, 74, 81, 83, 82, 84, 88, 84, 84, 91, 93, 94,93]})

print(df [0: 6])

plt.scatter(df.horas, df.pts)
plt.title ('Horas estudiadas vs. Puntaje del examen')
plt.xlabel ('Horas')
plt.ylabel ('Puntuación')
plt.show()

#create boxplot
df.boxplot(column=['pts'])

#fit simple linear regression model
y = df['pts']
x = df[['horas']]

x = sm.add_constant(x)
model = sm.OLS(y, x).fit()

#view model summary
print(model.summary())

#produce residual plots
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.plot_regress_exog(model, 'horas', fig=fig)

#produce Q-Q plot
res = model.resid
fig = sm.qqplot(res, fit=True, line="45")
plt.show()
