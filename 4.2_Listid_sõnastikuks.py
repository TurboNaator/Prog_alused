def listid_sonastikuks(jarjend1, jarjend2):
  sonastik = {}
  for i in range(len(jarjend1)):
    sonastik[jarjend1[i]]=jarjend2[i]
  return sonastik
  
print(listid_sonastikuks([0, 1, 0], ['a', 'b', 'c']))