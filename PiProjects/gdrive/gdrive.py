from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()

drive = GoogleDrive(gauth)

def find_folders(fldname):
    file_list = drive.ListFile({
        'q': "title='{}' and mimeType contains 'application/vnd.google-apps.folder' and trashed=false".format(fldname)
        }).GetList()
    return file_list



def upload(Picture_Name):
 
    gauth.LoadCredentialsFile("mycreds.txt")    
    print "Uploading Picture : " +Picture_Name
    gpath = 'PiPics'
    file_list1 = find_folders(gpath)

    #Loop through the GDrive Dirs and find the ID for the PiPics location
    for file1 in file_list1:
        if file1['title'] == gpath:
         id = file1['id']

    pic = Picture_Name
    
    f = drive.CreateFile({'title':pic, 'mimeType':'image/jpeg', "parents": [{"kind": "drive#fileLink","id": id}]})
    f.SetContentFile(pic)
    f.Upload()
    print('title: %s, mimeType: %s' % (f['title'], f['mimeType']))
    
    while f.uploaded == False:
        sleep(1)
    
    print "Removing the file : " + pic
    f = None
    os.remove(pic)
    
    gauth.SaveCredentialsFile("mycreds.txt")

if __name__ == '__main__': 
    print "Main"

