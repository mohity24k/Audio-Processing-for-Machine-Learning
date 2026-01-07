# Audio-Processing-for-Machine-Learning

A project which I took upon during this semester as a part of my minor degree - Artificial Intelligence and Machine Learning.

## Text-to-Speech Model

This repository includes a text-to-speech (TTS) model implementation that converts written text into spoken audio using the pyttsx3 library, an offline text-to-speech conversion library.

### Features

- **Simple API**: Easy-to-use Python interface for text-to-speech conversion
- **Offline Processing**: No internet connection required - works completely offline
- **Voice Selection**: Choose from multiple available system voices
- **Speed Control**: Adjustable speech rate (words per minute)
- **Volume Control**: Configurable volume levels
- **File Input**: Convert text from files directly to speech
- **Multiple Formats**: Save audio output in WAV format

### Installation

1. Clone this repository:
```bash
git clone https://github.com/mohity24k/Audio-Processing-for-Machine-Learning.git
cd Audio-Processing-for-Machine-Learning
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Usage

#### Basic Usage

```python
from tts_model import TextToSpeech

# Create TTS instance
tts = TextToSpeech()

# Convert text to speech
text = "Hello! This is a text-to-speech model."
tts.text_to_speech(text, 'output.wav')
```

#### Advanced Usage

```python
from tts_model import TextToSpeech

# Customize speech rate (words per minute)
tts = TextToSpeech(rate=150, volume=1.0)
tts.text_to_speech("This is at normal speed.", 'normal_speed.wav')

# Slow speech for better clarity
tts_slow = TextToSpeech(rate=100)
tts_slow.text_to_speech("This is spoken slowly.", 'slow_output.wav')

# Fast speech
tts_fast = TextToSpeech(rate=200)
tts_fast.text_to_speech("This is spoken quickly.", 'fast_output.wav')

# Adjust volume
tts_quiet = TextToSpeech(volume=0.5)
tts_quiet.text_to_speech("This is quieter.", 'quiet_output.wav')

# Convert text from a file
tts.text_to_speech_from_file('input.txt', 'file_output.wav')

# List available voices
voices = tts.get_available_voices()
for i, voice in enumerate(voices):
    print(f"{i}: {voice.name}")

# Select a specific voice
tts.set_voice(0)  # Use first available voice
```

#### Running Examples

Run the example script to see various use cases:

```bash
python tts_examples.py
```

This will generate several audio files demonstrating:
- Basic text-to-speech conversion
- Different speech rates (slow and fast)
- Volume control
- Converting text from files
- Voice selection

### API Reference

#### TextToSpeech Class

**Constructor:**
- `TextToSpeech(rate=150, volume=1.0, voice_index=0)`
  - `rate`: Speech rate in words per minute (default: 150)
  - `volume`: Volume level from 0.0 to 1.0 (default: 1.0)
  - `voice_index`: Index of the voice to use (default: 0)

**Methods:**
- `text_to_speech(text, output_file='output.wav')`: Convert text to speech and save to file
- `text_to_speech_from_file(input_file, output_file='output.wav')`: Convert text from file to speech
- `speak(text)`: Convert text to speech and play it (without saving to file)
- `get_available_voices()`: Get list of available system voices
- `set_voice(voice_index)`: Set the voice to use for speech

### Voice Options

The model uses the system's built-in TTS voices. Available voices depend on your operating system:
- **Windows**: Microsoft Speech API (SAPI5) voices
- **macOS**: NSSpeechSynthesizer voices
- **Linux**: eSpeak voices

Use `get_available_voices()` to see what's available on your system.

### Requirements

- Python 3.6+
- pyttsx3 2.90+

### Technical Details

The implementation uses pyttsx3, which is a text-to-speech conversion library in Python. Unlike cloud-based services, it works offline and uses the operating system's native TTS engines:
- **Windows**: Uses SAPI5
- **macOS**: Uses NSSpeechSynthesizer
- **Linux**: Uses eSpeak

### License

This project is for educational purposes as part of an AI and Machine Learning minor degree program.
