from db import (
    create_studio, list_studios, update_studio_country, delete_studio,
    create_anime, list_anime_with_studio, get_anime_by_id, update_anime, delete_anime,
    create_genre, list_genres, add_genre_to_anime, remove_genre_from_anime
)

def print_rows(rows):
    if not rows:
        print("(no rows)")
        return
    for r in rows:
        print(r)

def main():
    while True:
        print("\n=== Anime DB Console ===")
        print("1) List studios")
        print("2) Add studio")
        print("3) Update studio country")
        print("4) Delete studio")
        print("5) List anime (with studio)")
        print("6) Add anime")
        print("7) Get anime by id")
        print("8) Update anime")
        print("9) Delete anime")
        print("10) List genres")
        print("11) Add genre")
        print("12) Add genre to anime")
        print("13) Remove genre from anime")
        print("0) Quit")

        choice = input("Choose: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            print_rows(list_studios())

        elif choice == "2":
            name = input("Studio name: ").strip()
            country = input("Country: ").strip()
            studio_id = create_studio(name, country)
            print(f"Created/updated studio_id={studio_id}")

        elif choice == "3":
            sid = int(input("studio_id: ").strip())
            country = input("New country: ").strip()
            ok = update_studio_country(sid, country)
            print("Updated." if ok else "No such studio_id.")

        elif choice == "4":
            sid = int(input("studio_id: ").strip())
            ok = delete_studio(sid)
            print("Deleted." if ok else "No such studio_id.")

        elif choice == "5":
            print_rows(list_anime_with_studio())

        elif choice == "6":
            title = input("Title: ").strip()
            year = int(input("Release year: ").strip())
            eps = int(input("Episodes: ").strip())
            studio_id = int(input("studio_id: ").strip())
            anime_id = create_anime(title, year, eps, studio_id)
            print(f"Created anime_id={anime_id}")

        elif choice == "7":
            aid = int(input("anime_id: ").strip())
            row = get_anime_by_id(aid)
            print(row if row else "No such anime_id.")

        elif choice == "8":
            aid = int(input("anime_id: ").strip())
            title = input("New title: ").strip()
            year = int(input("New release year: ").strip())
            eps = int(input("New episodes: ").strip())
            studio_id = int(input("New studio_id: ").strip())
            ok = update_anime(aid, title, year, eps, studio_id)
            print("Updated." if ok else "No such anime_id.")

        elif choice == "9":
            aid = int(input("anime_id: ").strip())
            ok = delete_anime(aid)
            print("Deleted." if ok else "No such anime_id.")

        elif choice == "10":
            print_rows(list_genres())

        elif choice == "11":
            name = input("Genre name: ").strip()
            gid = create_genre(name)
            print(f"Created/updated genre_id={gid}")

        elif choice == "12":
            aid = int(input("anime_id: ").strip())
            gid = int(input("genre_id: ").strip())
            ok = add_genre_to_anime(aid, gid)
            print("Added." if ok else "Already exists (or invalid ids).")

        elif choice == "13":
            aid = int(input("anime_id: ").strip())
            gid = int(input("genre_id: ").strip())
            ok = remove_genre_from_anime(aid, gid)
            print("Removed." if ok else "No such mapping.")

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
