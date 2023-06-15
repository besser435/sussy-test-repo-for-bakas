import urllib.request, os

# This is bad because its static. I cant download new files, it has to be hard coded.
# Could maybe just add a extra links that that dont have anything yet
url = "https://raw.githubusercontent.com/besser435/sussy-test-repo-for-bakas/main/1.txt"
script_dir = os.path.dirname(os.path.abspath(__file__))

# \\ is windows specific. Test on linux
file_path = script_dir + "\\new_file.txt"

print("Starting download...")
urllib.request.urlretrieve(url, file_path)
print("Downloaded to: " + file_path)


"""import os

print("Starting download...")
script_dir = os.path.dirname(os.path.abspath(__file__))

# doesnt work on directories with files
os.system("git clone https://github.com/besser435/sussy-test-repo-for-bakas.git " + script_dir)

# requires the directory to be a git repo
#os.system("git pull origin main")
print("Downloaded to: " + script_dir)
"""

#append to usa_secrets if changes there
#TODO test on linux