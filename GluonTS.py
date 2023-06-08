

url = "C:/Path/SENER_ProduccionPetroleoCrudoEF.csv"

dataset1 = pd.read_csv(url,header=0,index_col=0)

ds_datatrain = ListDataset(
    [{"start":dataset1.index[0], "target":dataset1.value[:"2020-12-01 00:00:00"]}],
    freq=metadatos['freq'])

ds_datatest = ListDataset(
    [{"start":dataset1.index[0], "target":dataset1.value[:"2021-12-01 00:00:00"]}],
    freq=metadatos['freq'])
