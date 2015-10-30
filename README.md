# MayaHairAttribAsset
save Maya hair node attributes for later use.

Install:
	1. Clone into youg Maya Python site-packages folder.(exp. D:\Autodesk\Maya2016\Python\Lib\site-packages)
	2. In youg Maya Pyton editor, copy follow line & Run( You MAY have to restart Maya):
	
	import MayaHairAttribAsset.hairAttribAsset as hairAttribAsset
	dlg = hairAttribAsset.HairAttribCache()
	dlg.show()
Usage:
	1. Specify the asset file first;
	2. Press refresh button;
	3. Use oter buttons to operate.
