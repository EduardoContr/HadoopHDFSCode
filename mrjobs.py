##python code
##import the mrjobs libraries for use with functions, class for hadoop with ##hadoop-streaming
from mrjob.job import MRJob
from mrjob.step import MRStep

class PercentileRun: 
     def steps(self):
          return [
               MRStep(mapper=self.mapper_ranges,
                              reducer=self.reducer_lenrs1)
          ]
     
     def mapper_ranges(self, _, line):
	     (Symbol,Bid,Ask,Price,Chg ($),Chg	        			     (%),Open,High,Low,Volume,Wl,Timestamp,Range) = line.split('\t')
	     yield Range, 1
     
     def reducer_lenrs1(self, key, values):
     yield key, sum(values)

if __name__ == '__main__':
     PercentileRun.run()

### multiline comments start, review, the two separate files with the functions:


	question to identify what stocks in datamart, (datawarehouse object, eg.) were in the range of one percent movememt to the positie side:
	how many were rated in one, two or three is sequence of jobs,
job two, step,
def reducer_lenrs1(self, key, values):
     yield key, sum(values)

//Review of Job one below added for ease of user
	
	def mapper_ranges(self, _, line):
	     (Symbol,Bid,Ask,Price,Chg ($),Chg (%),Open,High,Low,Volume,Wl,Timestamp,Range) = line.split('\t')
##	Symbol,Bid,Ask,Price,Chg ($),Chg (%),Open,High,Low,Volume,Wl,Timestamp,Range
##	was cut and pasted from csv of the column names
	     yield Range, 1
job two- (step) ##see next file, mrjobstep2

##optional, rename the files containing % to pct to save overhead for offsetting the special characters with the additional '\'
//see file mrjobs.py for the python code in full with libraries and class defined,
called in the __main__ context/syntax of python, testing in ubuntu on flask, eg.


