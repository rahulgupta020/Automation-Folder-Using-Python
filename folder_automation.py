import os

allfiles=os.listdir()
allfiles.remove("folder_automation.py")
# print(allfiles)

def create(folders):
	if not os.path.exists(folders):
		os.makedirs(folders)

def move(foldername, allfiles):
	for file in allfiles:
		os.replace(file, f"{foldername}/{file}")

create('Images')
create('Docs')
create('Media')
create('Web')
create('Others')

imgext=[".png",".jpg",".jpeg",".jfif",".gif"]
img = [file for file in allfiles if os.path.splitext(file)[1].lower() in imgext]
# print("Images :",img)
# print("*************************")

docext=[".txt", ".docx", ".doc", ".pdf"]
doc = [file for file in allfiles if os.path.splitext(file)[1].lower() in docext]
# print("Docs :",doc)
# print("*************************")

webext=['.html', "htm",".css",".js"]
web = [file for file in allfiles if os.path.splitext(file)[1].lower() in webext]
# print("Web :",web)
# print("*************************")

mediaext=[".mp4", ".mp3"]
media = [file for file in allfiles if os.path.splitext(file)[1].lower() in mediaext]
# print("Media :", media)
# print("*************************")

others=[]
for file in allfiles:
	allext = os.path.splitext(file)[1].lower()
	if(allext not in imgext) and (allext not in docext) and (allext not in imgext) and os.path.isfile(file):
		others.append(file)
# print(others)

move("Images", img)
move("Docs", doc)
move("Media", media)
move("Web", web)
move("Others", others)

print("Done.....")