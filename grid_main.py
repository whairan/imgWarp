from qMain import getFileNameList, importNeuroLucidaXML, doAnnotation, doBatchRegistration, createCompositeSumImage
import cv2

InputDir = 'Asht_XML'
OutDir = 'Asht_reg'
flist1 = getFileNameList(InputDir, '*.xml')

for i in range(len(flist1)):
   importNeuroLucidaXML(flist1[i], 'S1', OutDir)

# if __name__ == '__main__':
   # doAnnotation(OutDir, 'Templates', 0)

# doBatchRegistration(OutDir, warpMarkers=True, includeMarkers=True, applyMask = True, TemplateIndex=1)

# cimg, timg = createCompositeSumImage(OutDir, TemplateIndex=1, ptSize=1, singleColor=True)


# cv2.imwrite('AshtImg.png', cimg)
# cv2.imwrite('AshtMask.png', timg)

#import pdb; pdb.set_trace()
