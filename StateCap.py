"""We have an existing dictionary that maps US states to their capitals.
1. Print the state capital of Idaho - Done.
2. Print all states - Done.
3. Print all capitals - Done.
4. Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...' - Done.
5. Ensure the string you created in 4. is alphabetically sorted by state
    - Added sorted list for the states, and with for loop on this list added the
    keys to another list with the values from the dictionary.

7. Now we want to add the reverse look up, given the name of a capital what state
is it in? - Done.
Implement the function def get_state(capital): below so it returns the state.
GOTCHAS: What happens if two states have the same capital name, how do you
handle that?
    -we are using a for loop to do that so the last state will be returned...
    so we added a list that collects all of the possible answers and then if the
    length of this list is grater than one the user will get  all of the options
    {'Texasa' : 'Austin'} was added to the dictionary to ensure that it's work.

"""
import sys

import pytest

STATES_CAPITALS = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas': 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Indiana' : 'Indianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismarck',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Texasa' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne',
}


def capital_of_Idaho():
    coi=STATES_CAPITALS['Idaho']
    print ('The capital of Idaho is: ' + coi)

def all_states():
    for i in STATES_CAPITALS.keys():
        print(i)

def all_capitals():
    for val in STATES_CAPITALS.values():
        print(val)


def states_capitals_string():
    sortednames=sorted(STATES_CAPITALS.keys(), key=lambda x:x.lower())
    sc_string=""
    for i in sortednames:
        values=STATES_CAPITALS[i]
        sc_string += i + ' -> ' + values + ', '
    print(sc_string)

def get_state(capital):
    if capital == '':
        raise KeyError('param is not set')
    msg="sorry your state is not found"
    st_list=[]
    for c,d in STATES_CAPITALS.items():
        if capital == d:
          msg = c
          st_list.append(c)
    if msg=="sorry your state is not found":
        print(msg)
    elif len(st_list)>1:
        print ("you have more than one option, the options is: " + str(st_list))
        msg =' '.join(st_list)
    else:
        print ("Your State is: " + msg)
    return msg



def test_state_to_capital():
    assert 'Cheyenne' == STATES_CAPITALS['Wyoming']


def test_state_to_capital_unknown():
    with pytest.raises(KeyError):
        STATES_CAPITALS['']


def test_capital_to_state():
    assert 'Wyoming' == get_state('Cheyenne')


def test_capital_to_state_unknown():
    with pytest.raises(KeyError):
        get_state('')


def main():
    return pytest.main(__file__)


if __name__ == '__StateCap__':
    sys.exit(main())
"""
Here is the functions that we used to check our code:

test_state_to_capital()
test_state_to_capital_unknown()
test_capital_to_state()
test_capital_to_state_unknown()

capital_of_Idaho()
all_states()
all_capitals()
states_capitals_string()

capital= str(input("enter your capital to get state: "))
get_state(capital)
"""
