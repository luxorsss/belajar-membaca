import asyncio
import os
import edge_tts

AUDIO_DIR = '/home/fadil/coding/belajar-membaca/audio'

ALPHABET = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

CHAR_SOUNDS = {
    'A': 'A', 'B': 'Be', 'C': 'Ce', 'D': 'De', 'E': 'E',
    'F': 'Ef', 'G': 'Ge', 'H': 'Ha', 'I': 'I', 'J': 'Je',
    'K': 'Ka', 'L': 'El', 'M': 'Em', 'N': 'En', 'O': 'O',
    'P': 'Pe', 'Q': 'Qi', 'R': 'Er', 'S': 'Es', 'T': 'Te',
    'U': 'U', 'V': 'Ve', 'W': 'We', 'X': 'Eks', 'Y': 'Ye',
    'Z': 'Zet'
}

VOICE = 'id-ID-GadisNeural'

async def main():
    os.makedirs(AUDIO_DIR, exist_ok=True)
    tasks = []
    
    for c in ALPHABET:
        lc = c.lower()
        sound_name = CHAR_SOUNDS[c]
        
        # 1. Bunyi huruf murni
        f_bunyi = os.path.join(AUDIO_DIR, f'bunyi_{lc}.mp3')
        if not os.path.exists(f_bunyi):
            tasks.append((f_bunyi, sound_name))
            
        # 2. Pertanyaan kuis
        f_tanya = os.path.join(AUDIO_DIR, f'tanya_{lc}.mp3')
        if not os.path.exists(f_tanya):
            tasks.append((f_tanya, f'Mana huruf {sound_name}?'))
            
        # 3. Jawaban benar
        f_benar = os.path.join(AUDIO_DIR, f'benar_{lc}.mp3')
        if not os.path.exists(f_benar):
            tasks.append((f_benar, f'Pintar! Ini huruf {sound_name}!'))
            
    print(f'Starting generation of {len(tasks)} audio files...')
    
    # Process sequentially with slight pause or batching to be smooth
    for idx, (filepath, text) in enumerate(tasks):
        fname = os.path.basename(filepath)
        print(f'[{idx+1}/{len(tasks)}] Generating {fname} -> {text}')
        tts = edge_tts.Communicate(text, VOICE, rate='-10%', pitch='+2Hz')
        await tts.save(filepath)
        
    print('All 26 letters audio generated successfully!')

if __name__ == '__main__':
    asyncio.run(main())
