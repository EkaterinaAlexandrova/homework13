class Player:
    def __init__(self, media_source, quality='1080p'):
        self.media_source = media_source
        self.quality = quality
        self.playing = False
        self.last_time = 0

    def play(self):
        if not self.playing:
            self.playing = True
            print(f'Playing {self.media_source} in {self.quality} quality.')
        else:
            print('Already playing.')

    def pause(self):
        if self.playing:
            self.playing = False
            print('Paused.')
        else:
            print('Already paused.')

    def save_last_time(self, time):
        self.last_time = time
        print(f'Last time played saved: {self.last_time}')

    def change_quality(self, new_quality):
        self.quality = new_quality
        print(f'Quality changed to {self.quality}')