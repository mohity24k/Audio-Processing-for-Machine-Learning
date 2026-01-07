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
    
    tts = TextToSpeech(language='en')
    text = "Welcome to the Audio Processing for Machine Learning project."
    output_file = tts.text_to_speech(text, 'example1_basic.mp3')
    print(f"✓ Generated audio: {output_file}")
    print()


def example_slow_speech():
    """Example: Slow speech for better clarity"""
    print("=" * 50)
    print("Example 2: Slow Speech")
    print("=" * 50)
    
    tts = TextToSpeech(language='en', slow=True)
    text = "This is an example of slow speech for better understanding."
    output_file = tts.text_to_speech(text, 'example2_slow.mp3')
    print(f"✓ Generated audio: {output_file}")
    print()


def example_multilingual():
    """Example: Text-to-speech in different languages"""
    print("=" * 50)
    print("Example 3: Multilingual Support")
    print("=" * 50)
    
    examples = [
        ('en', "Hello, how are you?", 'example3_english.mp3'),
        ('es', "Hola, ¿cómo estás?", 'example3_spanish.mp3'),
        ('fr', "Bonjour, comment allez-vous?", 'example3_french.mp3'),
    ]
    
    for lang, text, output in examples:
        tts = TextToSpeech(language=lang)
        output_file = tts.text_to_speech(text, output)
        print(f"✓ Generated {lang} audio: {output_file}")
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
    
    tts = TextToSpeech(language='en')
    output_file = tts.text_to_speech_from_file('sample_input.txt', 'example4_from_file.mp3')
    print(f"✓ Generated audio from file: {output_file}")
    print()


def main():
    """Run all examples"""
    print("\n" + "=" * 50)
    print("Text-to-Speech Model Examples")
    print("=" * 50 + "\n")
    
    try:
        example_basic_tts()
        example_slow_speech()
        example_multilingual()
        example_from_file()
        
        print("=" * 50)
        print("All examples completed successfully!")
        print("=" * 50)
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
