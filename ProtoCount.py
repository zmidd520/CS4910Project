import csv

# display information about capatured packed protocols
def printProtos(protos):
    print('Protocol'.ljust(20) + 'Occurrences'.rjust(12))         # header

    for (x, y) in protos.items():
        print(x.ljust(20, '.') + str(y).rjust(10, '.'))  # item information
    print()

# check if a high volume of pings are coming in
def checkICMP(protocols):
    if ('ICMP' in protocols.keys()):
        # allow headway for a few pings, but notify if high volume
        if protocols['ICMP'] > 12:
            print('IMPORTANT: HIGH VOLUME OF ICMP REQUESTS')

'''
def checknMap():
'''

protocols = {}

# open csv file
file = csv.reader(open('log.csv'))

# iterate through csv
for row in file:
    
    # skip first row since it just contains column headers
    if row[4] != 'Protocol':
        # check if protocol already has dictionary entry
        # protocol is the 5th value in csv row
        if row[4] not in protocols.keys():

            # create new dictionary item for protocol
            protocols[row[4]] = 1

        else:
            # increment protocol occurence number
            protocols[row[4]] += 1

printProtos(protocols)

# check for suspicious activity

# see if pings were detected
checkICMP(protocols)