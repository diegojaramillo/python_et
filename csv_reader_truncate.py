import csv
import socket
import fileinput
import os
#get hostname
hostname= socket.gethostname()

#option 1, truncate the file and write the correct values

#open and read csv file
with open('hosts_lib.csv', 'rU') as csvfile:
   csvreader = csv.reader(csvfile, dialect=csv.excel_tab, delimiter=';')#,quotechar='|')
   for row in csvreader:
        #if hostname match...
        if hostname == row[0]:
            
            #find config file path and open the file in read/write mode
            file_search= row[3]+row[2]+'.config'
            file_input= open(file_search, 'r+')
            #path = row[3]
            #define new values for file
            table= row[1]+'.'+row[2]
            
            #truncate file, put new values and close the file 
            file_input.truncate()
            file_input.write('--driver \n')
            file_input.write(row[4])
            file_input.write('\n')            
            file_input.write('--table \n')
            file_input.write(table)
            file_input.write('\n') 
            file_input.write('-m \n')
            file_input.write('1 \n')
            file_input.close()

            print (row[2]+'.config -- archivo editado \n')
            
            """
            filename = 'result.log'
            with open(os.path.join(path, filename), 'wb') as result:
                result.write(row[2]+'.config -- archivo editado \n')"""
              
        else:
            print ("no match values for server "+row[0])
            """
            path = row[3]
            filename = 'result.log'
            with open(os.path.join(path, filename), 'wb') as result:
                result.write("no match values for server "+row[0]+'\n')"""
            
"""            
--driver
com.ibm.as400.access.AS400JDBCDriver
--table
LIBR.TABLE
-m
1
"""