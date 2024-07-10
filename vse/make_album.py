def make_album(perfomer_name,album_name, age=''):
    """Исполнитель и альбом бесконечный цикл"""
    album = {'perfomer_name': perfomer_name.title(), 'album_name': album_name.title()}
    if age:
        album['age'] = age
    return album


while True:
    print("\nPlease enter the artist and the album name ")
    print("\nEnter 'q' at  any time to quit")

    p_name=input("Perfoment name: ")
    if p_name == 'q':
        break

    a_name = input("Album name: ")
    if a_name == 'q':
        break

    a_age = input("Age: ")
    if a_age=='q':
        break


    music_album = make_album(p_name, a_name, a_age)

    print(music_album)

