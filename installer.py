import requests
import py7zr
import os

url='https://builds.shipofharkinian.com/job/SoH_Multibranch/job/PR-416/lastSuccessfulBuild/artifact/soh.7z'
r = requests.get(url, allow_redirects=True)

print('Checking to see if \'C:\Ship of Harkinian\' exists.')
soh_path = 'C:\Ship of Harkinian'
if not os.path.exists(soh_path):
    print('Creating the folder \'Ship of Harkinian\' at the root of the C drive.')
    os.mkdir(soh_path)
else:
    print('The directory \'Ship of Harkinian\' already exists, proceeding to download.')

print('Downloading the latest rando build.')
open('C:\Ship of Harkinian\soh.7z', 'wb').write(r.content)
print('Done.\n')

print('Unzipping Ship of Harkinian')
with py7zr.SevenZipFile('C:\Ship of Harkinian\soh.7z', mode='r') as z:
    z.extractall(path='C:\Ship of Harkinian')
print('Done\n')

print('Cleaning up the soh.7z')
os.remove('C:\Ship of Harkinian\soh.7z')
print('Done.\n')

if not os.path.exists('C:\Ship of Harkinian\oot.otr'):
    print('WARNING: oot.otr is missing from the Ship of Harkinian directory.  You must extract the .otr file from a valid rom.\n')

print('All done! Press Enter to exit.')
user_input = input()