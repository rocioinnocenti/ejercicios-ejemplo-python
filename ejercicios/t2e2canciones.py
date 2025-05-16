#Obtener valores de la cancion favorita del usuario
nombre_cancion_f = input("¿Como se llama tu canción favorita?: ")
nombre_artista_f = input("¿Como se llama el artista? ")
album_f = input("¿De que album forma parte? ")
lanzamiento_f = int(input("¿En que año fue su lanzamiento? "))
duracion_f = int(input("¿Cuantos segundos dura? "))
tiene_videoclip_f = input("¿Tiene videoclip? (True/False): ") == "True"

#Obtener valores de la cancion menos favorita del usuario
nombre_cancion_mf = input("¿Como se llama tu canción menos favorita?: ")
nombre_artista_mf = input("¿Como se llama el artista? ")
album_mf = input("¿De que album forma parte? ")
lanzamiento_mf = int(input("¿En que año fue su lanzamiento? "))
duracion_mf = int(input("¿Cuantos segundos dura? "))
tiene_videoclip_mf = input("¿Tiene videoclip? (True/False): ") == "True"


print("Título de tu canción favorita: ", nombre_cancion_f)
print("Artista: ", nombre_artista_f)
print("Álbum: ", album_f)
print("Año: ", lanzamiento_f)
print(f"Dura {duracion_f} segundos ")
print("Tiene videoclip: ", tiene_videoclip_f)

print("Título de tu canción menos favorita: ", nombre_cancion_mf)
print("Artista: ", nombre_artista_mf)
print("Álbum: ", album_mf)
print("Año: ", lanzamiento_mf)
print(f"Dura {duracion_mf} segundos ")
print("Tiene videoclip: ", tiene_videoclip_mf)


