import time
import random
import simpleaudio

#So lets create a program where we can choose which music we want to play

a1 = "omw.wav"
a2 = "wem.wav"
a3 = "flg.wav"
a4 = "mol.wav"

sobj1 = simpleaudio.WaveObject.from_wave_file(a1)
sobj2 = simpleaudio.WaveObject.from_wave_file(a2)
sobj3 = simpleaudio.WaveObject.from_wave_file(a3)
sobj4 = simpleaudio.WaveObject.from_wave_file(a4)

musics = ["On My Own", "Walk em down", "Feel like god", "My ordinary life"]

randMusicsDeclare = [a1,a2,a3,a4]
randMusicSObj = [sobj1,sobj2,sobj3,sobj4]

print("There are 4 songs in my list currently.")
time.sleep(2)
print("They are as follows:")
time.sleep(1)
print(musics[0])
print(musics[1])
print(musics[2])
print(musics[3])

time.sleep(2)
print("Do you want to play a specific song or a random song?")
time.sleep(2)
print("Enter 1 for specific and 2 for random.")
time.sleep(1)
ask1 = input("")

if ask1 == "1":
    time.sleep(1)
    print("Okay as your wish which song you want to play?")
    print("1. " + musics[0])
    print("2. " + musics[1])
    print("3. " + musics[2])
    print("4. " + musics[3])
    wmore = input()
    if wmore == "1":
        time.sleep(1)
        print("Playing " + musics[0])
        play1 = sobj1.play()
        play1.wait_done()
        time.sleep(1)
        print("Thanks for listening")
    elif wmore == "2":
        print("Playing " + musics[1])
        play2 = sobj2.play()
        play2.wait_done()
        time.sleep(1)
        print("Thanks for listening")
    elif wmore == "3":
        print("Playing " + musics[2])
        play3 = sobj3.play()
        play3.wait_done()
        time.sleep(1)
        print("Thanks for listening")
    elif wmore == "4":
        print("Playing " + musics[3])
        play4 = sobj4.play()
        play4.wait_done()
        time.sleep(1)
        print("Thanks for listening")
elif ask1 == "2":
    print("Playing a random song!")
    randPlay = random.choice(randMusicSObj).play()
    randPlay.wait_done()
    print("Playing all songs currently")
    print("Playing " + musics[0])
    play1 = sobj1.play()
    play1.wait_done()
    time.sleep(1)
    print("Playing " + musics[1])
    play2 = sobj2.play()
    play2.wait_done()
    time.sleep(1)
    print("Playing " + musics[2])
    play3 = sobj3.play()
    play3.wait_done()
    time.sleep(1)
    print("Playing " + musics[3])
    play4 = sobj4.play()
    play4.wait_done()
    time.sleep(1)
    print("Thanks for listening")

print("WANT MORE?!?!??!?!?, Yes or No")
morehuh = input("")
if morehuh.upper() == "YES" or "Y" or "YEAH" or "YH":
    i=1
    while True:
        print("STARTING THE DAMN BEATS!!!")
        randPlay = random.choice(randMusicSObj).play()
        randPlay.wait_done()
        time.sleep(1)
        print("Quit the program to exit the loop!")
        if i == 100:
            print("DAWG! YOU REALLY LISTENED THAT MUCH.")
            break
        i+=1




