from scipy import fft
from sys import argv

#Path of input timeseries file given at command line
input_filename = argv[1]

#Use command line input to open timeseries file
infile = open(input_filename,'r')

#Create array to hold timeseries
timeseries = []

#Loop over lines in input file
for i, line in enumerate(infile):
    #Ignore first line in file - contains data labels, not values
    if (i!=0):
        #For all other lines, split at "," and add the first element to the timeseries array
        linearray=line.split(',')
        timeseries.append(float(linearray[0]))

#Run fast fourier transform fft on timeseries to fill the "transformed" array
transformed = fft(timeseries)

#Create power spectrum array by taking the square of the absolute value of the fourier transform
power_spectrum = []
for x in transformed:
    power_spectrum.append((abs(x))**2)

#Output filename the same as input filename but appended with "power_spectrum"
outfile = open(input_filename[0:-4]+'_power_spectrum.txt','w')

#Write power spectrum to file 
for element in transformed:
    output_value = (abs(element))**2
    outfile.write(str(output_value)+'\n')
