from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
      idemp, sector,sal,year = line.split(',')
      yield idemp, int(sal)

    def reducer(self, idemp, values):
        l = list(values)
        avg = sum(l) / len(l)
        yield idemp, avg

if __name__ == '__main__':
    MRWordFrequencyCount.run()
