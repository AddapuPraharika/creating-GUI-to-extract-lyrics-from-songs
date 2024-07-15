import tkinter as tk
import requests

def get_lyrics():
    api_url = f"(link unavailable){song_entry.get()}"
    response = requests.get(api_url, headers={"Authorization": "Bearer YOUR_API_KEY"})
    json = response.json()
    lyrics = json["response"]["hits"][0]["lyrics"]
    lyrics_text.delete(1.0, tk.END)
    lyrics_text.insert(tk.END, lyrics)

root = (link unavailable)()
root.title("Lyrics Extractor")

song_label = tk.Label(root, text="Song Title:")
song_label.pack()
song_entry = tk.Entry(root)
song_entry.pack()
search_button = tk.Button(root, text="Get Lyrics", command=get_lyrics)
search_button.pack()
lyrics_text = tk.Text(root)
lyrics_text.pack()

root.mainloop()
