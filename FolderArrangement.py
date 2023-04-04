import os
import shutil

def make_name(name, dest_list):
    n, e = os.path.splitext(name)
    for file_name in dest_list:
        dn, de = os.path.splitext(file_name)
        if not n[-1].isnumeric():
            if n==dn:
                n = n + '1'
        if n[-1].isnumeric():
            while True:
                if n in dn:
                    n = n[:-1] + str(int(n[-1])+1)
                else:
                    break
        
    return n+e
        

# Change the path to your own path
# Add the type of files if nessesary
src = 'D:/Coding/Automate_Project'
word_dest = 'D:/Coding/Automate_Project/Word'
excel_dest = 'D:/Coding/Automate_Project/Excel'
pdf_dest = 'D:/Coding/Automate_Project/pdf'
ppt_dest = "D:/Coding/Automate_Project/ptt"
photo_dest = "D:/Coding/Automate_Project/photo"

word_files = []
excel_files = []
pdf_files = []
ppt_files = []
photo_files = []

for file in os.listdir(src):
    if file.endswith('.doc') or file.endswith('.docx'):
        word_files.append(file)
    if file.endswith('.xlsx'):
        excel_files.append(file)
    if file.endswith('.pdf'):
        pdf_files.append(file)
    if file.endswith('.ppt') or file.endswith('.pptx'):
        ppt_files.append(file)
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        photo_files.append(file)

for files in word_files:
    if not os.path.exists(word_dest):
        os.makedirs(word_dest)
        print(files)
    os.rename(os.path.join(src,files), os.path.join(src,make_name(files,os.listdir(word_dest))))
    shutil.move(os.path.join(src,make_name(files,os.listdir(word_dest))),word_dest)
for files in excel_files:
    if not os.path.exists(excel_dest):
        os.makedirs(excel_dest)
    os.rename(os.path.join(src,files),os.path.join(src,make_name(files,os.listdir(excel_dest))))
    shutil.move(os.path.join(src,make_name(files,os.listdir(excel_dest))),excel_dest)
for files in pdf_files:
    if not os.path.exists(pdf_dest):
        os.makedirs(pdf_dest)
    os.rename(os.path.join(src,files),os.path.join(src,make_name(files,os.listdir(pdf_dest))))
    shutil.move(os.path.join(src,make_name(files,os.listdir(pdf_dest))),pdf_dest)
for files in ppt_files:
    if not os.path.exists(ppt_dest):
        os.makedirs(ppt_dest)
    os.rename(os.path.join(src,files),os.path.join(src,make_name(files,os.listdir(ppt_dest))))
    shutil.move(os.path.join(src,make_name(files,os.listdir(ppt_dest))),ppt_dest) 
for files in photo_files:
    if not os.path.exists(photo_dest):
        os.makedirs(photo_dest)
    os.rename(os.path.join(src,files),os.path.join(src,make_name(files,os.listdir(photo_dest))))
    shutil.move(os.path.join(src,make_name(files,os.listdir(photo_dest))),ppt_dest)    