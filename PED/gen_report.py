def generate_images(data):
	

	import pandas as pd
	import matplotlib.pyplot as plt

	path = r"D:\Mine\MyStuff\ML\Python\Practicals\WEB\Folder\reports\\" + str(data) + '.xlsx'
	df = pd.read_excel(path, sheetname=r'Sheet3')

	df.columns

	fig=plt.figure()
	x=[]
	for i in df.columns:
		x.append(sum(df[i]))
	x

	plt.plot(x)
	path = r"D:\Mine\MyStuff\ML\Python\Practicals\WEB\Folder\images\\" + str(data) + '.png'
	figure=fig.savefig(path)
	
