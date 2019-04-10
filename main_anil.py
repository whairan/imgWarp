from qMain import getFileNameList, importNeuroLucidaXML, doAnnotation, doBatchRegistration, createCompositeSumImage
import cv2

InputDir = 'Anil_XML'
OutDir = 'Anil_reg'
flist1 = getFileNameList(InputDir, '*.xml')


#for i in range(len(flist1)):
#    importNeuroLucidaXML(flist1[i], 'S1', OutDir, showMarkers=False, Markers='All', Xres=1600, Yres=1200)

if __name__ == '__main__':
    doAnnotation(OutDir,'Brain_Templates', 1)

#doBatchRegistration(OutDir, warpMarkers=False, includeMarkers=False, applyMask = False, dirTemplate = 'Brain_Templates', TemplateIndex=1, Xres=1600, Yres=1200)

#cimg, timg = createCompositeSumImage(OutDir, TemplateIndex=1, ptSize=3)

#cv2.imwrite('hongImg.png', cimg)