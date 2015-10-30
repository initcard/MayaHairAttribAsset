# MayaHairAttribAsset
save Maya hair node attributes for later use.

Usage:
	1. Clone into youg Maya Python site-packages folder.(exp. D:\Autodesk\Maya2016\Python\Lib\site-packages)
	2. In youg Maya Pyton editor, copy follow line & Run( You MAY have to restart Maya):
	
	import MayaHairAttribAsset
	dlg = MayaHairAttribAsset.hairAttribAsset.HairAttribCache()
	dlg.show()