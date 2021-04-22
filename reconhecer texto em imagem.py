from PIL import Image # bibliote Pillow carregamento de imagem,similar ao opencv,sendo que o pytesseract lê

import pytesseract as pyt 
import cv2
import os #import funções do sistema operacional

if __name__=="__main__":

 imagem=cv2.imread("BandeiraDoBrasil.jpg",0)#carregar imagem colorida
 

 filenameImagem="novaimagem.jpg".format(os.getpid()) # carregar imagem no windows temporário do processo do windows 
 cv2.imwrite(filenameImagem,imagem)

 texto = pyt.image_to_string(Image.open(filenameImagem)) #essa função vai transformar a imagem em uma string de texto

 os.remove(filenameImagem) # deletar a imagem temporária que estava em disco
    
print ("texto :" + texto) #exibir na tela 

cv2.imshow("imagem contendo o texto",imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
