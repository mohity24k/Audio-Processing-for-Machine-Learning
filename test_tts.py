"""
Simple tests for the Text-to-Speech model
"""

import os
import sys
from tts_model import TextToSpeech


def test_initialization():
    """Test TTS initialization"""
    print("Test 1: Initialization")
    try:
        tts = TextToSpeech()
        print("✓ TTS initialized successfully")
        return True
    except Exception as e:
        print(f"✗ Initialization failed: {e}")
        return False


def test_get_voices():
    """Test getting available voices"""
    print("\nTest 2: Get Available Voices")
    try:
        tts = TextToSpeech()
        voices = tts.get_available_voices()
        if voices and len(voices) > 0:
            print(f"✓ Found {len(voices)} available voices")
            return True
        else:
            print("✗ No voices found")
            return False
    except Exception as e:
        print(f"✗ Failed to get voices: {e}")
        return False


def test_text_to_speech():
    """Test basic text-to-speech conversion"""
    print("\nTest 3: Text-to-Speech Conversion")
    try:
        tts = TextToSpeech()
        test_text = "This is a test."
        output_file = "test_output.wav"
        
        result = tts.text_to_speech(test_text, output_file)
        
        if result == output_file:
            print(f"✓ Text-to-speech conversion completed")
            print(f"  Output file: {output_file}")
            return True
        else:
            print("✗ Conversion failed")
            return False
    except Exception as e:
        print(f"✗ Conversion failed: {e}")
        return False


def test_speak_method():
    """Test the speak method"""
    print("\nTest 4: Speak Method")
    try:
        tts = TextToSpeech()
        test_text = "Testing speak method."
        
        # This won't produce audio in a headless environment
        # but should not raise an error
        tts.speak(test_text)
        print("✓ Speak method executed successfully")
        return True
    except Exception as e:
        print(f"✗ Speak method failed: {e}")
        return False


def test_empty_text():
    """Test error handling for empty text"""
    print("\nTest 5: Empty Text Handling")
    try:
        tts = TextToSpeech()
        try:
            tts.text_to_speech("", "output.wav")
            print("✗ Should have raised ValueError for empty text")
            return False
        except ValueError:
            print("✓ Correctly raised ValueError for empty text")
            return True
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False


def test_voice_selection():
    """Test voice selection"""
    print("\nTest 6: Voice Selection")
    try:
        tts = TextToSpeech()
        voices = tts.get_available_voices()
        
        if voices and len(voices) > 1:
            # Try to set a different voice
            tts.set_voice(1)
            print("✓ Voice selection works")
            return True
        else:
            print("⚠ Only one voice available, skipping test")
            return True
    except Exception as e:
        print(f"✗ Voice selection failed: {e}")
        return False


def test_file_input():
    """Test converting text from a file"""
    print("\nTest 7: Text from File")
    try:
        # Create a test file
        test_file = "test_input.txt"
        with open(test_file, 'w') as f:
            f.write("This is test text from a file.")
        
        tts = TextToSpeech()
        output_file = tts.text_to_speech_from_file(test_file, "test_file_output.wav")
        
        # Clean up test file
        if os.path.exists(test_file):
            os.remove(test_file)
        
        print("✓ File-based conversion works")
        return True
    except Exception as e:
        print(f"✗ File-based conversion failed: {e}")
        return False


def main():
    """Run all tests"""
    print("=" * 60)
    print("Text-to-Speech Model - Test Suite")
    print("=" * 60 + "\n")
    
    tests = [
        test_initialization,
        test_get_voices,
        test_text_to_speech,
        test_speak_method,
        test_empty_text,
        test_voice_selection,
        test_file_input,
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 60)
    print("Test Results")
    print("=" * 60)
    print(f"Passed: {sum(results)}/{len(results)}")
    print(f"Failed: {len(results) - sum(results)}/{len(results)}")
    print("=" * 60)
    
    # Clean up test files
    for f in ["test_output.wav", "test_file_output.wav", "test_input.txt"]:
        if os.path.exists(f):
            try:
                os.remove(f)
            except:
                pass
    
    return all(results)


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
