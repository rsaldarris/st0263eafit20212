from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
      idemp, sector,sal,year = line.split(',')
      yield idemp, str(sector)

    def reducer(self, idemp, values):
      val = str(values) + str(values)
      yield idemp, val

if __name__ == '__main__':
    MRWordFrequencyCount.run()
