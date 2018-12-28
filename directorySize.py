import os

totalSize = 0

while True:
    directory = input('Please enter the file path: ')
    if os.path.isdir(directory):
        break
    else:
        print('Invalid location.  Please try again.')

for filename in os.listdir (directory):
    if not os.path.isfile(os.path.join(directory, filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join(directory, filename))

print('The total size of all files within this directory is: ' + str(round((totalSize/1073741824), 2)) + ' GB.')

input('Press enter to close...')
