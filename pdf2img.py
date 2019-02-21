from wand.image import Image as wi
pdf = wi(filename="invoice4.pdf", resolution=300)
pdfImage = pdf.convert("png")
i=1
for img in pdfImage.sequence:
    page = wi(image=img)
    page.save(filename=str(i)+".png")
    i +=1
