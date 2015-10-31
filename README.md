# MayaHairAttribAsset
save Maya hair node attributes for later use.

## Install:
	1. Use git clone into young Maya Python site-packages folder.
            (exp. D:\Autodesk\Maya2016\Python\Lib\site-packages).

    2. You need run: git submodule init & git submodule update to download
           the maya_utils.
	3. In young Maya Python editor, copy follow line & Run( You MAY have to restart Maya):
	
	import MayaHairAttribAsset.hairAttribAsset as hairAttribAsset
	dlg = hairAttribAsset.hairAttribAsset()
	dlg.show()

## Usage:
	1. Specify the asset file first;
	2. Press refresh button;
	3. Use other buttons to operate.
