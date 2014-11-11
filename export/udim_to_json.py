import pprint, mari, json
from PySide import QtCore, QtGui

ret_dict = {}

chan = mari.geo.current().currentChannel()
layer = chan.currentLayer()

udim_dict = {}
if layer.isPaintableLayer():
    image_set = layer.imageSet()

    for index, image in enumerate(image_set.uvImageList()):
        info_dict = {}
        info_dict['width'] = image.width()
        info_dict['height'] = image.height()
        udim_dict[str(1001 + index)] = info_dict


ret_dict['udim'] = udim_dict
ret_dict['channel'] = chan.name()

udim_json = json.dumps(ret_dict, indent=4)
#print(udim_json)

file_path, file_filter = QtGui.QFileDialog.getSaveFileName(None, 'Save UDIM', '/home', "*.json")

if file_path:
    f = open(file_path,'w')
    f.write(udim_json)
    f.close()