#! /usr/bin/python
#
# ATBS Chapter 12
# Using the censuspopdata.xlsx file

import openpyxl, pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract'] # old way of calling sheet name is deprecated
countyData = {} # blank dictionary
# countyData[state abbrev][county]['tracts']
# countyData[state abbrev][county]['pop']

# TODO: Fill in countyData with each county's population and tracts.
print('Reading rows...')
for row in range(2, sheet.max_row + 1): # starting on row 2 because row 1 is the column names
    # Each row in the spreadsheet has data for one census tract
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # make sure the key for this state exists (will cause error if dict keys don't already exist)
    countyData.setdefault(state, {})
    # make sure the key for this county in this state exists
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row represents one census tract, so increment by one
    countyData[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract
    countyData[state][county]['pop'] += int(pop)


# TODO: Open a new text file and write the contents of countyData to it
print('Writing results...')
resultFile = open('census2010data.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done!')
