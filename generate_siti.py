import asyncio
import os
import edge_tts

AUDIO_DIR = '/home/fadil/coding/belajar-membaca/audio'
VOICE = 'jv-ID-SitiNeural'

# Specific phonetic pronunciation rules
PRONUNCIATION = {
    'a': 'A',
    'b': 'Beh',
    'c': 'Ce',
    'd': 'Deh',
    'e': 'E',
    'f': 'Ef',
    'g': 'Ge',
    'h': 'Haa',
    'i': 'I',
    'j': 'Jeee',
    'k': 'Kaa',
    'l': 'El',
    'm': 'Em',
    'n': 'En',
    'o': 'Ooo',
    'p': 'Pe',
    'q': 'Qi',
    'r': 'Er',
    's': 'Es',
    't': 'Teh',
    'u': 'Uuu',
    'v': 'Ve',
    'w': 'Weh',
    'x': 'Eks',
    'y': 'Ye',
    'z': 'Zzzzz'
}

async def generate():
    os.makedirs(AUDIO_DIR, exist_ok=True)
    all_tasks = []

    # 1. Vokal murni
    for v in ['a', 'i', 'u', 'e', 'o']:
        all_tasks.append((f'vokal_{v}.mp3', PRONUNCIATION[v]))

    # 2. Bunyi 26 huruf
    for char, pron in PRONUNCIATION.items():
        all_tasks.append((f'bunyi_{char}.mp3', pron))
        all_tasks.append((f'tanya_{char}.mp3', f'Mana huruf {pron}?'))
        all_tasks.append((f'benar_{char}.mp3', f'Pintar! Ini huruf {pron}!'))

    # 3. Kuis feedback
    all_tasks.append(('salah.mp3', 'Bukan yang itu, coba lagi ya!'))
    all_tasks.append(('selesai.mp3', 'Hore! Hebat sekali! Kamu berhasil menebak semua huruf!'))

    print(f'Generating {len(all_tasks)} audio files with voice {VOICE}...')
    for idx, (filename, text) in enumerate(all_tasks):
        filepath = os.path.join(AUDIO_DIR, filename)
        tts = edge_tts.Communicate(text, VOICE, rate='-8%', pitch='+1Hz')
        await tts.save(filepath)
        if (idx + 1) % 10 == 0 or idx + 1 == len(all_tasks):
            print(f'Progress: {idx+1}/{len(all_tasks)} done')

    print('All audio generated with Siti successfully!')

if __name__ == '__main__':
    asyncio.run(generate())
