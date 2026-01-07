"""
Example usage of the Text-to-Speech model
This script demonstrates different ways to use the TTS model.
"""

from tts_model import TextToSpeech


def example_basic_tts():
    """Example: Basic text-to-speech conversion"""
    print("=" * 50)
    print("Example 1: Basic Text-to-Speech")
    print("=" * 50)
    
    tts = TextToSpeech()
    text = "Welcome to the Audio Processing for Machine Learning project."
    output_file = tts.text_to_speech(text, 'example1_basic.wav')
    print(f"✓ Generated audio: {output_file}")
    print()


def example_speech_rate():
    """Example: Different speech rates"""
    print("=" * 50)
    print("Example 2: Speech Rate Variations")
    print("=" * 50)
    
    # Slow speech
    tts_slow = TextToSpeech(rate=100)
    text = "This is an example of slow speech for better understanding."
    output_file = tts_slow.text_to_speech(text, 'example2_slow.wav')
    print(f"✓ Generated slow speech: {output_file}")
    
    # Fast speech
    tts_fast = TextToSpeech(rate=200)
    output_file = tts_fast.text_to_speech(text, 'example2_fast.wav')
    print(f"✓ Generated fast speech: {output_file}")
    print()


def example_volume_control():
    """Example: Volume control"""
    print("=" * 50)
    print("Example 3: Volume Control")
    print("=" * 50)
    
    text = "This demonstrates volume control in text-to-speech."
    
    # Normal volume
    tts_normal = TextToSpeech(volume=1.0)
    output_file = tts_normal.text_to_speech(text, 'example3_normal.wav')
    print(f"✓ Generated normal volume: {output_file}")
    
    # Lower volume
    tts_quiet = TextToSpeech(volume=0.5)
    output_file = tts_quiet.text_to_speech(text, 'example3_quiet.wav')
    print(f"✓ Generated lower volume: {output_file}")
    print()


def example_from_file():
    """Example: Convert text from a file to speech"""
    print("=" * 50)
    print("Example 4: Text from File")
    print("=" * 50)
    
    # Create a sample text file
    sample_text = """
    Text-to-speech technology enables machines to convert written text into spoken words.
    This is particularly useful in various applications such as virtual assistants,
    accessibility tools for visually impaired users, and educational software.
    """
    
    with open('sample_input.txt', 'w', encoding='utf-8') as f:
        f.write(sample_text.strip())
    
    tts = TextToSpeech()
    output_file = tts.text_to_speech_from_file('sample_input.txt', 'example4_from_file.wav')
    print(f"✓ Generated audio from file: {output_file}")
    print()


def example_voice_selection():
    """Example: Select different voices"""
    print("=" * 50)
    print("Example 5: Voice Selection")
    print("=" * 50)
    
    tts = TextToSpeech()
    voices = tts.get_available_voices()
    
    print(f"Available voices: {len(voices)}")
    for i, voice in enumerate(voices[:3]):  # Show first 3 voices
        print(f"  Voice {i}: {voice.name}")
        tts.set_voice(i)
        output_file = tts.text_to_speech(
            f"This is voice number {i}.",
            f'example5_voice{i}.wav'
        )
        print(f"  ✓ Generated: {output_file}")
    print()


def main():
    """Run all examples"""
    print("\n" + "=" * 50)
    print("Text-to-Speech Model Examples")
    print("=" * 50 + "\n")
    
    try:
        example_basic_tts()
        example_speech_rate()
        example_volume_control()
        example_from_file()
        example_voice_selection()
        
        print("=" * 50)
        print("All examples completed successfully!")
        print("=" * 50)
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
