import json
import requests
import os
# jdu assets downloader by mishok
# don't steal :heart:
with open("sku-packages.json", encoding="utf-8") as sku:
    skupackages = json.load(sku)
with open("songdb.json", encoding="utf-8") as db:
    songdb = json.load(db)
names = list(songdb)
i = 0
files_count = 0
local_path = 'assets/'
while i < len(names):
    name = names[i]
    print(name + " started downloading.")
    os.mkdir("assets/" + name)
    try:
        mainscene_name = name + "_mapContent"
        mainscene = skupackages[mainscene_name]['url']
        r = requests.get(mainscene, allow_redirects=True)
        open(local_path + name + "/" + name + '_mapContent.zip', 'wb').write(r.content)
        print("Mainscene downloaded.")
        files_count += 1
    except KeyError:
        print("Mainscene does not exist in sku-packages.json")
    try:
        banner_bkgImageUrl = songdb[name]['assets']['banner_bkgImageUrl']
        r = requests.get(banner_bkgImageUrl, allow_redirects=True)
        open(local_path + name + '/' + name + '_banner_bkg.tga.ckd', 'wb').write(r.content)
        print("Banner_bkg downloaded.")
        files_count += 1
    except KeyError:
        print("Banner_bkg does not exist in songdb.json")
    try:
        coach1ImageUrl = songdb[name]['assets']['coach1ImageUrl']
        r = requests.get(coach1ImageUrl, allow_redirects=True)
        open(local_path + name + '/' + name + '_coach_1.tga.ckd', 'wb').write(r.content)
        print("Coach 1 downloaded.")
        files_count += 1
    except KeyError:
        print("Coach 1 does not exist in sku-packages.json")
    try:
        coach2ImageUrl = songdb[name]['assets']['coach2ImageUrl']
        r = requests.get(coach2ImageUrl, allow_redirects=True)
        open(local_path + name + '/' + name + '_coach_2.tga.ckd', 'wb').write(r.content)
        print("Coach 2 downloaded.")
        files_count += 1
    except KeyError:
        print("Coach 2 texture does not exist in songdb.json")
    try:
        coach3ImageUrl = songdb[name]['assets']['coach3ImageUrl']
        r = requests.get(coach3ImageUrl, allow_redirects=True)
        open(local_path + name + '/' + name + '_coach_3.tga.ckd', 'wb').write(r.content)
        print("Coach 3 downloaded.")
        files_count += 1
    except KeyError:
        print("Coach 3 texture does not exist in songdb.json")
    try:
        coach4ImageUrl = songdb[name]['assets']['coach4ImageUrl']
        r = requests.get(coach4ImageUrl, allow_redirects=True)
        open(local_path + name + '/' + name + '_coach_4.tga.ckd', 'wb').write(r.content)
        print("Coach 4 downloaded.")
        files_count += 1
    except KeyError:
        print("Coach 4 texture does not exist in songdb.json")
    try:
        coverImageUrl = songdb[name]['assets']['coverImageUrl']
        r = requests.get(coverImageUrl, allow_redirects=True)
        open(local_path + name + '/' + name + '_cover_generic.tga.ckd', 'wb').write(r.content)
        print("Cover_generic downloaded.")
        files_count += 1
    except KeyError:
        print("Cover_generic does not exist in songdb.json")
    try:
        cover_1024ImageUrl = songdb[name]['assets']['cover_1024ImageUrl']
        r = requests.get(cover_1024ImageUrl, allow_redirects=True)
        open(local_path + name + '/' + name + '_Cover_1024.png', 'wb').write(r.content)
        print("Cover downloaded.")
        files_count += 1
    except KeyError:
        print("Cover does not exist in songdb.json")
    try:
        cover_smallImageUrl = songdb[name]['assets']['cover_smallImageUrl']
        r = requests.get(cover_smallImageUrl, allow_redirects=True)
        open(local_path + name + '/' + name + '_cover_online.tga.ckd', 'wb').write(r.content)
        print("Cover_online downloaded.")
        files_count += 1
    except KeyError:
        print("Cover_online does not exist in songdb.json")
    try:
        expandBkgImageUrl = songdb[name]['assets']['expandBkgImageUrl']
        r = requests.get(expandBkgImageUrl, allow_redirects=True)
        open(local_path + name + '/' + name + '_cover_albumbkg.tga.ckd', 'wb').write(r.content)
        print("Albumbkg downloaded.")
        files_count += 1
    except KeyError:
        print("Albumbkg does not exist in songdb.json")
    try:
        expandCoachImageUrl = songdb[name]['assets']['expandCoachImageUrl']
        r = requests.get(expandCoachImageUrl, allow_redirects=True)
        open(local_path + name + '/' + name + '_cover_albumcoach.tga.ckd', 'wb').write(r.content)
        print("Albumcoach downloaded.")
        files_count += 1
    except KeyError:
        print("Albumcoach does not exist in songdb.json")
    try:
        map_bkgImageUrl = songdb[name]['assets']['map_bkgImageUrl']
        r = requests.get(map_bkgImageUrl, allow_redirects=True)
        open(local_path + name + '/' + name + '_map_bkg.tga.ckd', 'wb').write(r.content)
        print("Map_bkg downloaded.")
        files_count += 1
    except KeyError:
        print("Map_bkg does not exist in songdb.json")
    try:
        phoneCoach1ImageUrl = songdb[name]['assets']['phoneCoach1ImageUrl']
        r = requests.get(phoneCoach1ImageUrl, allow_redirects=True)
        open(local_path + name + '/' + name + '_coach_1_phone.png', 'wb').write(r.content)
        print("Coach 1 for phone downloaded.")
        files_count += 1
    except KeyError:
        print("Coach 1 for phone does not exist in songdb.json")
    try:
        phoneCoach2ImageUrl = songdb[name]['assets']['phoneCoach2ImageUrl']
        r = requests.get(phoneCoach2ImageUrl, allow_redirects=True)
        open(local_path + name + '/' + name + '_coach_2_phone.png', 'wb').write(r.content)
        print("Coach 2 for phone downloaded.")
        files_count += 1
    except KeyError:
        print("Coach 2 texture for phone does not exist in songdb.json")
    try:
        phoneCoach3ImageUrl = songdb[name]['assets']['phoneCoach3ImageUrl']
        r = requests.get(phoneCoach3ImageUrl, allow_redirects=True)
        open(local_path + name + '/' + name + '_coach_3_phone.png', 'wb').write(r.content)
        print("Coach 3 for phone downloaded.")
        files_count += 1
    except KeyError:
        print("Coach 3 texture for phone does not exist in songdb.json")
    try:
        phoneCoach4ImageUrl = songdb[name]['assets']['phoneCoach4ImageUrl']
        r = requests.get(phoneCoach4ImageUrl, allow_redirects=True)
        open(local_path + name + '/' + name + '_coach_4_phone.png', 'wb').write(r.content)
        print("Coach 4 for phone downloaded.")
        files_count += 1
    except KeyError:
        print("Coach 4 texture for phone does not exist in songdb.json")
    try:
        phoneCoverImageUrl = songdb[name]['assets']['phoneCoverImageUrl']
        r = requests.get(phoneCoverImageUrl, allow_redirects=True)
        open(local_path + name + '/' + name + '_cover_phone.jpg', 'wb').write(r.content)
        print("Cover for phone downloaded.")
        files_count += 1
    except KeyError:
        print("Cover for phone does not exist in songdb.json")
    try:
        videoPreviewVideoURL = songdb[name]['assets']['videoPreviewVideoURL']
        r = requests.get(videoPreviewVideoURL, allow_redirects=True)
        open(local_path + name + '/' + name + '_VideoPreview.webm', 'wb').write(r.content)
        print("Videopreview downloaded.")
        files_count += 1
    except KeyError:
        print("Videopreview does not exist in songdb.json")
    print("Finished.")
    i += 1
print("Finished. Downloaded files: " + files_count)