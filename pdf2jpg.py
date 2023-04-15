from pdf2image import convert_from_path
import os

print("Converting pdfs to images in directory [img/]...\n");
for filename in os.listdir("pdf"):
	pages = convert_from_path("pdf/" + filename);
	filename = filename[:-4];
	for i in range(len(pages)):
		pages[i].save("img/" + filename + ".jpg", "JPEG");
print("Conversion completed!\n");