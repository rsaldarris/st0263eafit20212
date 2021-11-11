from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
      idemp, sector,sal,year = line.split(',')
      yield sector, int(sal)

    def reducer(self, sector, values):
        l = list(values)
        avg = sum(l) / len(l)
        yield sector, avg

if __name__ == '__main__':
    MRWordFrequencyCount.run()
