# Details
One can find the slides of lecture 2 `Lecture 2.pdf`.
 
Below one can find the first exercises for the Digital Signal Processing part of Introduction to Smart Systems Engineering course at the Hanze University of Applied Sciences.


# Exercises

1. Tidy up your exercises from last time, by making your own function that takes duration, samplerate, amplitude and frequency as arguments. The function returns a 1D np.array with time data, as well as a 1D np.array with the sine data.

1. Add phase shift functionality to the above.

1. Use np.convolve to create a moving average to a sine wave of your liking. What happens?
    - Extra challenge for those who like it: can you implement convolution yourself? How does it compare to the output of `np.convolve`?

1. Sum two sine waves, one with a relatively high frequency, the other with a low frequency, use `np.convolve` to make a moving average again. What happens?

1. Download a sound file in Python (see example below), apply a moving average to the sound data. What happens?

```python
import urllib.request
import librosa
from IPython import display

file_name = "2776.mp3"  # Source: https://bigsoundbank.com/detail-2776-cockatiel-parakeet-8.html
url = f"https://bigsoundbank.com/UPLOAD/mp3/{file_name}"

urllib.request.urlretrieve(url, file_name)
sound_data, samplerate = librosa.load(file_name)  # sr=None keeps the original sample rate

display.display(display.Audio(data=sound_data, rate=samplerate))
```