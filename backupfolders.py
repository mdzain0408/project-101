from posixpath import relpath
import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        for root,dir,files in os.walk(file_from):
            for f in files:
                path = os.path.join(root,f)
                relPath = os.path.relpath(path,file_from)
                dropboxPath = os.path.join(file_to,relPath)

                with open(path, 'rb') as file:
                    dbx.files_upload(file.read(), dropboxPath,mode=dropbox.files.WriteMode("overwrite"))

def main():
    access_token = 'BYytyNQcXgkAAAAAAAAAAQCbJMT4WesAc22iMtAwG9e5zpBYfz1QSJZjVkSqqYlT'
    transferData = TransferData(access_token)

    file_from = input("Location of the folder to be backedup: ")
    file_to = input("path in the dropbox to backup files: ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

    print("file have been uploaded")

if __name__ == '__main__':
    main()