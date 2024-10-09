import sys

from fontTools.misc.cython import returns
from numpy.ma.extras import average



def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date, county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list. This was changed to just give Rockingham and Harrisonburg
        if county == 'Rockingham' and state == 'Virginia':
            data.append(entry)
        if county == 'Harrisonburg city' and state == 'Virginia':
            data.append(entry)

        #data.append(entry)
    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """

    # your code here
    #create empty list
    rock=[]
    harr=[]
    #put tuples into two separate lists: one for Harrisonburg City (HBC) and one for Rockingham (RH)
    #the lines are tuples and county is in the 1st index
    for line in data:
        if line[1] == 'Rockingham':
            rock.append(line)
        else:
            harr.append(line)
    #grab the first instance of HBC and RH
    #Then grab the date of that first instant, then print
    firstrock = rock[0]
    firstdaterock = firstrock[0]
    firstharr = harr[0]
    firstharrdate = firstharr[0]

    return firstharrdate , firstdaterock

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """

    # your code here
    # create empty list (copied from 1)
    rock = []
    harr = []
    # put tuples into two separate lists: one for Harrisonburg City (HBC) and one for Rockingham (RH)
    # the lines are tuples and county is in the 1st index (copied from 1)
    for line in data:
        if line[1] == 'Rockingham':
            rock.append(line)
        else:
            harr.append(line)

    # new lists for #of cases
    num_casesr = []
    num_casesh = []
    for thing in rock:
        case = thing[4]
        num_casesr.append(case)

    for thing in harr:
        case = thing[4]
        num_casesh.append(case)

    # find out what the worse amount of new cases was by subtracting the previous day from current day.
    # if the new # of cases is bigger than last biggest it is saved
    #Harrisonburg
    add_hlist = []
    for i in range(0,(len(num_casesh))):
        added_h = num_casesh[i]-num_casesh[i-1]
        add_hlist.append(added_h)
    maxh = max(add_hlist)
    maxindexh = add_hlist.index(maxh)
    worstlisth = harr[maxindexh]
    worstdayh = worstlisth[0]

    # Repeat for Rockingham
    add_rlist = []
    for i in range(0,(len(num_casesr))):
        added_r = num_casesr[i]-num_casesr[i-1]
        add_rlist.append(added_r)
    maxr = max(add_rlist)
    maxindexr = add_rlist.index(maxr)
    worstlistr = rock[maxindexr]
    worstdayr = worstlistr[0]

    seconda = ("The worst day in Harrisonburg was " + str(worstdayh) + " with " + str(maxh) + " cases.")
    secondb = ("The worst day in Rockingham was " + str(worstdayr) + " with " + str(maxr) + " cases.")

    return seconda, secondb

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    #create empty list (copied from 1)
    rock=[]
    harr=[]
    #put tuples into two separate lists: one for Harrisonburg City (HBC) and one for Rockingham (RH)
    #the lines are tuples and county is in the 1st index (copied from 1)
    for line in data:
        if line[1] == 'Rockingham':
            rock.append(line)
        else:
            harr.append(line)

    #new lists for #of cases (copied from 2)
    num_casesr=[]
    num_casesh=[]
    for thing in rock:
        case = thing[4]
        num_casesr.append(case)

    for thing in harr:
        case = thing[4]
        num_casesh.append(case)

    #put all the new cases in a list, find the average of every 7 days and store the highest average
    #this is Rockingham
    before = 0
    case = []
    for i in num_casesr:
        newcases = i - before
        case.append(newcases)
        before = i
    oldav = 0
    inav = 0
    for j in case:
        k = case.index(j)
        sevenav = sum(case[k-3:k+3])/7
        if sevenav > oldav:
            oldav = sevenav
            inav = k
    lina = rock[inav-3]
    linb = rock[inav+3]
    daa = lina[0]
    dab = linb[0]


    #put all the new cases in a list, find the average of every 7 days and store the highest average
    #this is HBC
    before = 0
    case = []

    for i in num_casesh:
        newcases = i - before
        case.append(newcases)
        before = i
    oldav = 0
    inav = 0
    for j in case:
        k = case.index(j)
        sevenav = sum(case[k-3:k+3])/7
        if sevenav > oldav:
            oldav = sevenav
            inav = k
    linah = harr[inav-3]
    linbh = harr[inav+3]
    daah = linah[0]
    dabh = linbh[0]

    threea = str("The worst days in Rockingham were between " + str(daa) + " and " + str(dab) + ".")
    threeb = str("The worst days in Harrisonburg were between " + str(daah) + " and " + str(dabh) + ".")

    return threea, threeb

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    for (date, county, state, cases, deaths) in data:
        print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    (answer1a, answer1b) = first_question(data)

    print("The first instance of COVID in Rockingham was " + str(answer1b))
    print("The first instance of COVID in Harrisonburg was " + str(answer1a))



    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    (seca, secb) = second_question(data)
    print(seca)
    print(secb)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    (athree, bthree) = third_question(data)
    print(athree)
    print(bthree)
