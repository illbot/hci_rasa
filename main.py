import pandas as pd


class SongData:
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame

    def acousticness(self, minAcousticness, maxAcousticness):
        if minAcousticness <= self.dataFrame['acousticness'].min():
            minAcousticness = self.dataFrame['acousticness'].min()
        if maxAcousticness >= self.dataFrame['acousticness'].max():
            maxAcousticness = self.dataFrame['acousticness'].max()
        if minAcousticness >= self.dataFrame['acousticness'].max():
            minAcousticness = self.dataFrame['acousticness'].max()
        if maxAcousticness <= self.dataFrame['acousticness'].min():
            maxAcousticness = self.dataFrame['acousticness'].min()
        if minAcousticness > maxAcousticness:
            temp = minAcousticness
            minAcousticness = maxAcousticness
            maxAcousticness = temp

        return SongData(self.dataFrame[
                            (self.dataFrame['acousticness'] <= maxAcousticness) &
                            (self.dataFrame['acousticness'] >= minAcousticness)])

    def danceability(self, minDanceability, maxDanceability):
        if minDanceability <= self.dataFrame['danceability'].min():
            minDanceability = self.dataFrame['danceability'].min()
        if maxDanceability >= self.dataFrame['danceability'].max():
            maxDanceability = self.dataFrame['danceability'].max()
        if minDanceability >= self.dataFrame['danceability'].max():
            minDanceability = self.dataFrame['danceability'].max()
        if maxDanceability <= self.dataFrame['danceability'].min():
            maxDanceability = self.dataFrame['danceability'].min()
        if minDanceability > maxDanceability:
            temp = minDanceability
            minDanceability = maxDanceability
            maxDanceability = temp

        return SongData(self.dataFrame[
                            (self.dataFrame['danceability'] <= maxDanceability) &
                            (self.dataFrame['danceability'] >= minDanceability)])

    def energy(self, minEnergy, maxEnergy):
        if minEnergy <= self.dataFrame['energy'].min():
            minEnergy = self.dataFrame['energy'].min()
        if maxEnergy >= self.dataFrame['energy'].max():
            maxEnergy = self.dataFrame['energy'].max()
        if minEnergy >= self.dataFrame['energy'].max():
            minEnergy = self.dataFrame['energy'].max()
        if maxEnergy <= self.dataFrame['energy'].min():
            maxEnergy = self.dataFrame['energy'].min()
        if minEnergy > maxEnergy:
            temp = minEnergy
            minEnergy = maxEnergy
            maxEnergy = temp
        return SongData(self.dataFrame[
                            (self.dataFrame['energy'] <= maxEnergy) &
                            (self.dataFrame['energy'] >= minEnergy)])

    def instrumentalness(self, minInstrumentalness, maxInstrumentalness):
        if minInstrumentalness <= self.dataFrame['instrumentalness'].min():
            minInstrumentalness = self.dataFrame['instrumentalness'].min()
        if maxInstrumentalness >= self.dataFrame['instrumentalness'].max():
            maxInstrumentalness = self.dataFrame['instrumentalness'].max()
        if minInstrumentalness >= self.dataFrame['instrumentalness'].max():
            minInstrumentalness = self.dataFrame['instrumentalness'].max()
        if maxInstrumentalness <= self.dataFrame['instrumentalness'].min():
            maxInstrumentalness = self.dataFrame['instrumentalness'].min()
        if minInstrumentalness > maxInstrumentalness:
            temp = minInstrumentalness
            minInstrumentalness = maxInstrumentalness
            maxInstrumentalness = temp
        return SongData(self.dataFrame[
                            (self.dataFrame['instrumentalness'] <= maxInstrumentalness) &
                            (self.dataFrame['instrumentalness'] >= minInstrumentalness)])

    def liveness(self, minLiveness, maxLiveness):
        if minLiveness <= self.dataFrame['instrumentalness'].min():
            minLiveness = self.dataFrame['instrumentalness'].min()
        if maxLiveness >= self.dataFrame['instrumentalness'].max():
            maxLiveness = self.dataFrame['instrumentalness'].max()
        if minLiveness >= self.dataFrame['instrumentalness'].max():
            minLiveness = self.dataFrame['instrumentalness'].max()
        if maxLiveness <= self.dataFrame['instrumentalness'].min():
            maxLiveness = self.dataFrame['instrumentalness'].min()
        if minLiveness > maxLiveness:
            temp = minLiveness
            minLiveness = maxLiveness
            maxLiveness = temp
        return SongData(self.dataFrame[
                            (self.dataFrame['instrumentalness'] <= maxLiveness) &
                            (self.dataFrame['instrumentalness'] >= minLiveness)])

    def speechiness(self, minSpeechiness, maxSpeechiness):
        if minSpeechiness <= self.dataFrame['speechiness'].min():
            minSpeechiness = self.dataFrame['speechiness'].min()
        if maxSpeechiness >= self.dataFrame['speechiness'].max():
            maxSpeechiness = self.dataFrame['speechiness'].max()
        if minSpeechiness >= self.dataFrame['speechiness'].max():
            minSpeechiness = self.dataFrame['speechiness'].max()
        if maxSpeechiness <= self.dataFrame['speechiness'].min():
            maxSpeechiness = self.dataFrame['speechiness'].min()
        if minSpeechiness > maxSpeechiness:
            temp = minSpeechiness
            minSpeechiness = maxSpeechiness
            maxSpeechiness = temp
        return SongData(self.dataFrame[
                            (self.dataFrame['speechiness'] <= maxSpeechiness) &
                            (self.dataFrame['speechiness'] >= minSpeechiness)])

    def valence(self, minValence, maxValence):
        if minValence <= self.dataFrame['valence'].min():
            minValence = self.dataFrame['valence'].min()
        if maxValence >= self.dataFrame['valence'].max():
            maxValence = self.dataFrame['valence'].max()
        if minValence >= self.dataFrame['valence'].max():
            minValence = self.dataFrame['valence'].max()
        if maxValence <= self.dataFrame['valence'].min():
            maxValence = self.dataFrame['valence'].min()
        if minValence > maxValence:
            temp = minValence
            minValence = maxValence
            maxValence = temp
        return SongData(self.dataFrame[
                            (self.dataFrame['valence'] <= maxValence) &
                            (self.dataFrame['valence'] >= minValence)])


if __name__ == '__main__':
    # acousticness,danceability,duration_ms,energy,instrumentalness,key,liveness,loudness,mode,speechiness,tempo,time_signature,valence,target,song_title,artist
    df = pd.read_csv(r'.\data.csv')
    sd = SongData(df)
    result = sd.acousticness(0.2, 0.8).danceability(0.2, 0.8).energy(0.2, 0.8).instrumentalness(0.2, 0.8).liveness(0.2, 0.8).speechiness(0.05, 0.1).valence(0.1, 0.6).dataFrame
    print(pd.DataFrame(result, columns=['valence', 'song_title', 'artist']))
