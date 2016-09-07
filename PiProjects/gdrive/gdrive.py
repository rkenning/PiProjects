from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
drive = GoogleDrive(gauth)

def find_folders(fldname):
    file_list = drive.ListFile({
        'q': "title='{}' and mimeType contains 'application/vnd.google-apps.folder' and trashed=false".format(fldname)
        }).GetList()
    return file_list



def main():
 
    PicsDir = '/Pics/'
    PicsDir = os.getcwd() + '/Pics/'
    Pics = os.listdir(PicsDir)
    gpath = 'PiPics'
    file_list1 = find_folders(gpath)

    #Loop through the GDrive Dirs and find the ID for the PiPics location
    for file1 in file_list1:
        if file1['title'] == gpath:
         id = file1['id']


    #Loop through pics found and upload
    for pic in Pics:
        f = drive.CreateFile({'title':pic, 'mimeType':'image/jpeg', "parents": [{"kind": "drive#fileLink","id": id}]})
        f.SetContentFile(PicsDir+pic)
        f.Upload()
        print('title: %s, mimeType: %s' % (f['title'], f['mimeType']))

        #Remove all the pictures
        for pic in Pics:
            os.remove(PicsDir+pic)

        gauth.SaveCredentialsFile("mycreds.txt")

if __name__ == '__main__': main()
    