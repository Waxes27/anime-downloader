import requests
import os

def anime_name():
    return input(" What anime do you want to download: ").split()

def anime_site_name(anime):
    for i in anime:
        anime_dash = ('-'.join(anime))
    try: 
        return requests.get(f"https://www12.9anime.to/search?keyword={' '.join(anime)}").text, anime_dash
    except requests.exceptions.ConnectionError:
        print("Check Internet connection")


def anime_url_finder(site, anime_dash):
    anime_urls = []
    for i in site.split():
        if f'="/watch/{anime_dash}'.lower() in i.lower():
            anime_url = i.split('href="')
            anime_url = f'https://www12.9anime.to{anime_url[1]}'
            anime_urls.append(anime_url.strip('">'))
    return anime_urls


def dub_or_sub(anime_urls):


    dub_sub = input("1. English(Dub)\n2. Japanese(Sub)\n(1./2.) > ")


    dublist = []
    sublist = []
    # print(anime_urls)
    if dub_sub == '1':  
        for i in anime_urls:
            if '-dub' in i:
                dublist.append(i)
                return dub_sub, dublist
        
    else:           
        for i in anime_urls:
            print(i)
            if '-dub' not in i:
                sublist.append(i)
                print(i)
                return dub_sub, sublist


    


def main():
    anime = anime_name()
    site, anime_dash = anime_site_name(anime)
    anime_urls = anime_url_finder(site, anime_dash)
    try:
        dub_sub, list_of_anime = dub_or_sub(anime_urls)
    except TypeError:
        print(f"Anime '{anime[0:]}' not found")
        main()
        return
    # os.system("clear")
    print("Description:\n\n")
    for i in range(10):
        content = requests.get(list_of_anime[i]).text
        description = content.split('itemprop="description">')[1].split('</p>')[0]
        print(description,"\n\n")
    download = input("Download? (Enter)/(CTRL + C): ")
    

main()


