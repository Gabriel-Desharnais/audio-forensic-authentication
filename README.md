# audio-forensic-authentication
This is a software developed in python to assess the autencity of an audio document forencically

## UserGuide
### Installation
To install *afa* download the latest release on GitHub and unzip it where you want it to be installed. If you want to be able to lauch the *afa* command where ever you want, add a link of *afa.py* in the folder */usr/bin/*

Be sure to install *matplotlib*, *numpy* and *scipy* before runing *afa*
### Launch an analysis
**comming soon**
You can launch all the tests available with the following command:

``` bash
afa [ audiofile ] 
```

### Launch a viewer
**comming soon**
Sometimes you just want to view the raw signal in the form of a waveform of the audio file you can do that by simply using the following command:

``` bash
afa [ audiofile ] -V
```
This will open a matplotlib window of the signal

### writing a report
**comming soon**
If you want a report to be written in a text file, use the following command:
``` bash
afa [ audiofile] -o [outputfile]
```
### Analysis done
The only test done at the moment is *tempering detection using waveforms*
