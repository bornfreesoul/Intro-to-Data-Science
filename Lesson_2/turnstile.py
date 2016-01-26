import csv
import pandas

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task. 
    
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file in the links below:
    
    Sample input file:
    https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
    Sample updated file:
    https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
    '''
    # def find_keyword(theList, keyword):
    #     print "keyword = " + keyword        
    #     result = []
    #     for ind, entry1 in enumerate(theList):
    #         print ind, entry1
    #         if entry1 == keyword:
    #             result.append(ind)
                
    #     print "result", result
    #     return result
    
    for name in filenames:
        f_in = open(name, "r")
        f_out = open("updated_" + name, "wb")
        
        reader_in = csv.reader(f_in, delimiter = ",")
        writer_out = csv.writer(f_out, delimiter = ",")


        
        for line in reader_in:
            constant_part = line[0:3]
            other_part = line[3:]
            index = 0
            while index < len(other_part) and index + 4 < len(other_part):         
                if index + 5 > len(other_part):
                    newLine =  constant_part + other_part[index:]                    
                else:
                    newLine = constant_part + other_part[index:(index + 5)]
                newLine = [x.strip(" ") for x in newLine]
                #print newLine
                writer_out.writerow(newLine)
                index = index + 5
    return 
            
        
        


fix_turnstile_data(["turnstile_110528.txt"])

df1 =  pandas.read_csv("updated_turnstile_110528.txt", header = None)

print df1.head()

df2 = pandas.read_csv("solution_turnstile_110528.txt", header = None)

print df2.head()

