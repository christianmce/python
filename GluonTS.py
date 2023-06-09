

url = "C:/Path/SENER_ProduccionPetroleoCrudoEF.csv"

dataset1 = pd.read_csv(url,header=0,index_col=0)

ds_datatrain = ListDataset(
    [{"start":dataset1.index[0], "target":dataset1.value[:"2020-12-01 00:00:00"]}],
    freq=metadatos['freq'])

ds_datatest = ListDataset(
    [{"start":dataset1.index[0], "target":dataset1.value[:"2021-12-01 00:00:00"]}],
    freq=metadatos['freq'])


estimator = DeepAREstimator(
	predicion_length=metadatos['prediction_months'],
	context_length=2*metadatos['prediction_months'],
	freq=metadatos['freq'],
	trainer=Trainer(
	ctx="cpu",
	epochs=5,
	learning_rate=1e-3,
	hybridize=False,
	num_batches_per_epoch=100
	)
)
predictor = estimator.train(ds_datatrain)


predict_eval, ts_it = make_evaluation_predictions(
	dataset = ds_datatrain,
	predictor = predictor,
	num_samples = 100,
)

result_predict = list(predict_eval)
tss = list(ts_it)


def show_plot_forecast_results(tss,forecasts):
	for target, forecast in islice(zip(tss,forecasts),1):
		ax = target[-100:].plot(figsize=(12,5), linewidth=2)
		forecast.plot(color='g',prediction_intervals=[50.0,90.0])
		plt.grid(which='both')
		plt.legend(["Observations","Median prediction",
		"90% Confidence interval","50% Confidence interval"])
		plt.show()

show_plot_forecast_results(tss,result_predict)
