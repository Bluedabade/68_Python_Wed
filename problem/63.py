def calculate_number_of_songs(hours: float, avg_song_length: float = 3.5) -> int:
    listen_time = hours *60
    total_song = listen_time // avg_song_length
    return(total_song)

hours = 2 
avg_song_length = 3.5

print(calculate_number_of_songs(hours,avg_song_length))