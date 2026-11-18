import asyncio
import os
import edge_tts

AUDIO_DIR = "/home/fadil/coding/belajar-membaca/audio"
VOICE = "id-ID-GadisNeural"

ITEMS = [
    # Explore
    ("huruf_a.mp3", "A... Apel!"),
    ("huruf_i.mp3", "I... Ikan!"),
    ("huruf_u.mp3", "U... Udang!"),
    ("huruf_e.mp3", "E... Ember!"),
    ("huruf_o.mp3", "O... Obat!"),
    # Quiz questions
    ("tanya_a.mp3", "Mana huruf A?"),
    ("tanya_i.mp3", "Mana huruf I?"),
    ("tanya_u.mp3", "Mana huruf U?"),
    ("tanya_e.mp3", "Mana huruf E?"),
    ("tanya_o.mp3", "Mana huruf O?"),
    # Correct feedback
    ("benar_a.mp3", "Pintar! Ini huruf A!"),
    ("benar_i.mp3", "Pintar! Ini huruf I!"),
    ("benar_u.mp3", "Pintar! Ini huruf U!"),
    ("benar_e.mp3", "Pintar! Ini huruf E!"),
    ("benar_o.mp3", "Pintar! Ini huruf O!"),
    # Wrong feedback
    ("salah.mp3", "Bukan yang itu, coba cari lagi ya!"),
    # Welcome & Victory
    ("welcome.mp3", "Halo! Mari belajar huruf vokal!"),
    ("victory.mp3", "Hore! Hebat sekali! Kamu berhasil mengenal semua huruf vokal!"),
]

async def generate_all():
    os.makedirs(AUDIO_DIR, exist_ok=True)
    for filename, text in ITEMS:
        filepath = os.path.join(AUDIO_DIR, filename)
        print(f"Generating {filename} -> '{text}'")
        tts = edge_tts.Communicate(text, VOICE, rate="-8%", pitch="+3Hz")
        await tts.save(filepath)
    print("All audio files generated successfully!")

if __name__ == "__main__":
    asyncio.run(generate_all())
