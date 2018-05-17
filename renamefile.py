
'''Program to rename multiple files in a single folder with common naming system and incrementing number at the end'''


import os
def main():
    i = 1
    path = '' #set path = the path of the folder where you want to do the renaming task. Make sure its in the single quotes
    stname = ''#set stname = the common characters/name you want for the files which wont change in every files of that folder
    exten = ''#set exten = the extension of file you want to have.

    #loop renaming the filenames
    for filename in os.listdir(path):
        dst = stname + str(i) + exten
        src = path + '/' + filename
        dst = path + '/' + dst
        os.rename(src, dst)
        i += 1

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
