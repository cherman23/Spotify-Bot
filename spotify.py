import spotipy
import spotipy.util as util


def main():
    print("Welcome to spotify search!")
    artistName = input(print("Enter artist name: "))

    artistList = spotipy.search(q=artistName, type="artist", limit=3)
    for i in range(len(artistList)):
        print(i+1 + ". " + artistList[i])

    choice = input("Pick one of the artists by number: ")
    songList = spotipy.artist_track(q=artistList[choice-1], type="track", limit=3)
    for i in range(len(songList)):
        print(i+1 + ". " + songList[i])

main()