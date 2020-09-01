import requests
import json
import pandas as pd
import glob2 # read and combine files
from time import sleep


def get_data(endpoint):
    response = requests.get(endpoint)   # timeout
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: {response.text}')
    print(response.status_code)
    #sleep(5)
    return response.json()

def write_data(data,AREA_TYPE,AREA_NAME):
    # To json and excel
    # data = get_data(endpoint)
    # print(data)
    # json
    with open(f"data/{AREA_TYPE}/{AREA_NAME}_out_data.json", "w") as write_file:
        json.dump(data, write_file)
    print(f"{AREA_NAME}_out_data.json"," file made")
    # excel
    pd.DataFrame(data["data"]).to_excel(f"data/{AREA_TYPE}/{AREA_NAME}_out_data.xlsx",
                                        index=False)
    print(f"{AREA_NAME}_out_data.xlsx"," file made")

def region_data(STRUCTURE=None):
    print("------- Pulling region data -------")
    AREA_TYPE = "region"
    #AREA_NAME = "West Midlands"
    AREA_NAME_LIST = ["East Midlands",
                      "East of England",
                      "London",
                      "North East",
                      "North West",
                      "South East",
                      "South West",
                      "West Midlands",
                      "Yorkshire and The Humber"]
    if STRUCTURE is None:
        for AREA_NAME in AREA_NAME_LIST:
            endpoint = (
                'https://api.coronavirus.data.gov.uk/v1/data?'
                f'filters=areaType={AREA_TYPE};areaName={AREA_NAME}&'
                'structure={"areaType":"areaType","areaName":"areaName","areaCode":"areaCode","date":"date","newCasesBySpecimenDate":"newCasesBySpecimenDate","cumCasesBySpecimenDate":"cumCasesBySpecimenDate","newDeaths28DaysByPublishDate":"newDeaths28DaysByPublishDate","cumDeaths28DaysByPublishDate":"cumDeaths28DaysByPublishDate"}&format=json'
            )
            data = get_data(endpoint)
            write_data(data, AREA_TYPE, AREA_NAME)
    else:
        for AREA_NAME in AREA_NAME_LIST:
            endpoint = (
                'https://api.coronavirus.data.gov.uk/v1/data?'
                f'filters=areaType={AREA_TYPE};areaName={AREA_NAME}&'
                f'structure={STRUCTURE}&format=json'
            )
            data = get_data(endpoint)
            write_data(data, AREA_TYPE, AREA_NAME)

def nation_data(STRUCTURE=None):
    print("------- Pulling nation data -------")
    AREA_TYPE = "nation"
    AREA_NAME_LIST = ["England",
                      "Scotland",
                      "Wales",
                      "Northern Ireland"] # nothern ireland returns 204 - success but not data
    if STRUCTURE is None:
        for AREA_NAME in AREA_NAME_LIST:
            endpoint = (
                'https://api.coronavirus.data.gov.uk/v1/data?'
                f'filters=areaType={AREA_TYPE};areaName={AREA_NAME}&'
                'structure={"areaType":"areaType","areaName":"areaName","areaCode":"areaCode","date":"date","newCasesBySpecimenDate":"newCasesBySpecimenDate","cumCasesBySpecimenDate":"cumCasesBySpecimenDate","newDeaths28DaysByPublishDate":"newDeaths28DaysByPublishDate","cumDeaths28DaysByPublishDate":"cumDeaths28DaysByPublishDate"}&format=json'
            )
            data = get_data(endpoint)
            write_data(data, AREA_TYPE, AREA_NAME)
    else:
        for AREA_NAME in AREA_NAME_LIST:
            endpoint = (
                'https://api.coronavirus.data.gov.uk/v1/data?'
                f'filters=areaType={AREA_TYPE};areaName={AREA_NAME}&'
                f'structure={STRUCTURE}&format=json'
            )
            data = get_data(endpoint)
            write_data(data, AREA_TYPE, AREA_NAME)


def upper_tier_local_authority_data(STRUCTURE=None):
    print("------- Pulling UTLA data -------")
    AREA_TYPE = "utla"
    AREA_NAME_LIST = [  'Aberdeen City',
                        'Aberdeenshire',
                        'Angus',
                        'Argyll and Bute',
                        'Barking and Dagenham',
                        'Barnet',
                        'Barnsley',
                        'Bath and North East Somerset',
                        'Bedford',
                        'Bexley',
                        'Birmingham',
                        'Blackburn with Darwen',
                        'Blackpool',
                        'Blaenau Gwent',
                        'Bolton',
                        'Bournemouth, Christchurch and Poole',
                        'Bracknell Forest',
                        'Bradford',
                        'Brent',
                        'Bridgend',
                        'Brighton and Hove',
                        'Bristol, City of',
                        'Bromley',
                        'Buckinghamshire',
                        'Bury',
                        'Caerphilly',
                        'Calderdale',
                        'Cambridgeshire',
                        'Camden',
                        'Cardiff',
                        'Carmarthenshire',
                        'Central Bedfordshire',
                        'Ceredigion',
                        'Cheshire East',
                        'Cheshire West and Chester',
                        'City of Edinburgh',
                        'Clackmannanshire',
                        'Conwy',
                        'Cornwall and Isles of Scilly',
                        'County Durham',
                        'Coventry',
                        'Croydon',
                        'Cumbria',
                        'Darlington',
                        'Denbighshire',
                        'Derby',
                        'Derbyshire',
                        'Devon',
                        'Doncaster',
                        'Dorset',
                        'Dudley',
                        'Dumfries and Galloway',
                        'Dundee City',
                        'Ealing',
                        'East Ayrshire',
                        'East Dunbartonshire',
                        'East Lothian',
                        'East Renfrewshire',
                        'East Riding of Yorkshire',
                        'East Sussex',
                        'Enfield',
                        'Essex',
                        'Falkirk',
                        'Fife',
                        'Flintshire',
                        'Gateshead',
                        'Glasgow City',
                        'Gloucestershire',
                        'Greenwich',
                        'Gwynedd',
                        'Hackney and City of London',
                        'Halton',
                        'Hammersmith and Fulham',
                        'Hampshire',
                        'Haringey',
                        'Harrow',
                        'Hartlepool',
                        'Havering',
                        'Herefordshire, County of',
                        'Hertfordshire',
                        'Highland',
                        'Hillingdon',
                        'Hounslow',
                        'Inverclyde',
                        'Isle of Anglesey',
                        'Isle of Wight',
                        'Islington',
                        'Kensington and Chelsea',
                        'Kent',
                        'Kingston upon Hull, City of',
                        'Kingston upon Thames',
                        'Kirklees',
                        'Knowsley',
                        'Lambeth',
                        'Lancashire',
                        'Leeds',
                        'Leicester',
                        'Leicestershire',
                        'Lewisham',
                        'Lincolnshire',
                        'Liverpool',
                        'Luton',
                        'Manchester',
                        'Medway',
                        'Merthyr Tydfil',
                        'Merton',
                        'Middlesbrough',
                        'Midlothian',
                        'Milton Keynes',
                        'Monmouthshire',
                        'Moray',
                        'Na h-Eileanan Siar',
                        'Neath Port Talbot',
                        'Newcastle upon Tyne',
                        'Newham',
                        'Newport',
                        'Norfolk',
                        'North Ayrshire',
                        'North East Lincolnshire',
                        'North Lanarkshire',
                        'North Lincolnshire',
                        'North Somerset',
                        'North Tyneside',
                        'North Yorkshire',
                        'Northamptonshire',
                        'Northumberland',
                        'Nottingham',
                        'Nottinghamshire',
                        'Oldham',
                        'Orkney Islands',
                        'Oxfordshire',
                        'Pembrokeshire',
                        'Perth and Kinross',
                        'Peterborough',
                        'Plymouth',
                        'Portsmouth',
                        'Powys',
                        'Reading',
                        'Redbridge',
                        'Redcar and Cleveland',
                        'Renfrewshire',
                        'Rhondda Cynon Taf',
                        'Richmond upon Thames',
                        'Rochdale',
                        'Rotherham',
                        'Rutland',
                        'Salford',
                        'Sandwell',
                        'Scottish Borders',
                        'Sefton',
                        'Sheffield',
                        'Shetland Islands',
                        'Shropshire',
                        'Slough',
                        'Solihull',
                        'Somerset',
                        'South Ayrshire',
                        'South Gloucestershire',
                        'South Lanarkshire',
                        'South Tyneside',
                        'Southampton',
                        'Southend-on-Sea',
                        'Southwark',
                        'St. Helens',
                        'Staffordshire',
                        'Stirling',
                        'Stockport',
                        'Stockton-on-Tees',
                        'Stoke-on-Trent',
                        'Suffolk',
                        'Sunderland',
                        'Surrey',
                        'Sutton',
                        'Swansea',
                        'Swindon',
                        'Tameside',
                        'Telford and Wrekin',
                        'Thurrock',
                        'Torbay',
                        'Torfaen',
                        'Tower Hamlets',
                        'Trafford',
                        'Vale of Glamorgan',
                        'Wakefield',
                        'Walsall',
                        'Waltham Forest',
                        'Wandsworth',
                        'Warrington',
                        'Warwickshire',
                        'West Berkshire',
                        'West Dunbartonshire',
                        'West Lothian',
                        'West Sussex',
                        'Westminster',
                        'Wigan',
                        'Wiltshire',
                        'Windsor and Maidenhead',
                        'Wirral',
                        'Wokingham',
                        'Wolverhampton',
                        'Worcestershire',
                        'Wrexham',
                        'York']
    if STRUCTURE is None:
        for AREA_NAME in AREA_NAME_LIST:
            endpoint = (
                'https://api.coronavirus.data.gov.uk/v1/data?'
                f'filters=areaType={AREA_TYPE};areaName={AREA_NAME}&'
                'structure={"areaType":"areaType","areaName":"areaName","areaCode":"areaCode","date":"date","newCasesBySpecimenDate":"newCasesBySpecimenDate","cumCasesBySpecimenDate":"cumCasesBySpecimenDate","newDeaths28DaysByPublishDate":"newDeaths28DaysByPublishDate","cumDeaths28DaysByPublishDate":"cumDeaths28DaysByPublishDate"}&format=json'
            )
            data = get_data(endpoint)
            write_data(data, AREA_TYPE, AREA_NAME)
    else:
        for AREA_NAME in AREA_NAME_LIST:
            endpoint = (
                'https://api.coronavirus.data.gov.uk/v1/data?'
                f'filters=areaType={AREA_TYPE};areaName={AREA_NAME}&'
                f'structure={STRUCTURE}&format=json'
            )
            data = get_data(endpoint)
            write_data(data, AREA_TYPE, AREA_NAME)

def lower_tier_local_authority_data(STRUCTURE=None):
    print("------- Pulling LTLA data -------")
    AREA_TYPE = "ltla"
    AREA_NAME_LIST = [  "Aberdeen City",
                        "Aberdeenshire",
                        "Adur",
                        "Allerdale",
                        "Amber Valley",
                        "Angus",
                        "Argyll and Bute",
                        "Arun",
                        "Ashfield",
                        "Ashford",
                        "Aylesbury Vale",
                        "Babergh",
                        "Barking and Dagenham",
                        "Barnet",
                        "Barnsley",
                        "Barrow-in-Furness",
                        "Basildon",
                        "Basingstoke and Deane",
                        "Bassetlaw",
                        "Bath and North East Somerset",
                        "Bedford",
                        "Bexley",
                        "Birmingham",
                        "Blaby",
                        "Blackburn with Darwen",
                        "Blackpool",
                        "Blaenau Gwent",
                        "Bolsover",
                        "Bolton",
                        "Boston",
                        "Bournemouth, Christchurch and Poole",
                        "Bracknell Forest",
                        "Bradford",
                        "Braintree",
                        "Breckland",
                        "Brent",
                        "Brentwood",
                        "Bridgend",
                        "Brighton and Hove",
                        "Bristol, City of",
                        "Broadland",
                        "Bromley",
                        "Bromsgrove",
                        "Broxbourne",
                        "Broxtowe",
                        "Burnley",
                        "Bury",
                        "Caerphilly",
                        "Calderdale",
                        "Cambridge",
                        "Camden",
                        "Cannock Chase",
                        "Canterbury",
                        "Cardiff",
                        "Carlisle",
                        "Carmarthenshire",
                        "Castle Point",
                        "Central Bedfordshire",
                        "Ceredigion",
                        "Charnwood",
                        "Chelmsford",
                        "Cheltenham",
                        "Cherwell",
                        "Cheshire East",
                        "Cheshire West and Chester",
                        "Chesterfield",
                        "Chichester",
                        "Chiltern",
                        "Chorley",
                        "City of Edinburgh",
                        "Clackmannanshire",
                        "Colchester",
                        "Conwy",
                        "Copeland",
                        "Corby",
                        "Cornwall and Isles of Scilly",
                        "Cotswold",
                        "County Durham",
                        "Coventry",
                        "Craven",
                        "Crawley",
                        "Croydon",
                        "Dacorum",
                        "Darlington",
                        "Dartford",
                        "Daventry",
                        "Denbighshire",
                        "Derby",
                        "Derbyshire Dales",
                        "Doncaster",
                        "Dorset",
                        "Dover",
                        "Dudley",
                        "Dumfries and Galloway",
                        "Dundee City",
                        "Ealing",
                        "East Ayrshire",
                        "East Cambridgeshire",
                        "East Devon",
                        "East Dunbartonshire",
                        "East Hampshire",
                        "East Hertfordshire",
                        "East Lindsey",
                        "East Lothian",
                        "East Northamptonshire",
                        "East Renfrewshire",
                        "East Riding of Yorkshire",
                        "East Staffordshire",
                        "East Suffolk",
                        "Eastbourne",
                        "Eastleigh",
                        "Eden",
                        "Elmbridge",
                        "Enfield",
                        "Epping Forest",
                        "Epsom and Ewell",
                        "Erewash",
                        "Exeter",
                        "Falkirk",
                        "Fareham",
                        "Fenland",
                        "Fife",
                        "Flintshire",
                        "Folkestone and Hythe",
                        "Forest of Dean",
                        "Fylde",
                        "Gateshead",
                        "Gedling",
                        "Glasgow City",
                        "Gloucester",
                        "Gosport",
                        "Gravesham",
                        "Great Yarmouth",
                        "Greenwich",
                        "Guildford",
                        "Gwynedd",
                        "Hackney and City of London",
                        "Halton",
                        "Hambleton",
                        "Hammersmith and Fulham",
                        "Harborough",
                        "Haringey",
                        "Harlow",
                        "Harrogate",
                        "Harrow",
                        "Hart",
                        "Hartlepool",
                        "Hastings",
                        "Havant",
                        "Havering",
                        "Herefordshire, County of",
                        "Hertsmere",
                        "High Peak",
                        "Highland",
                        "Hillingdon",
                        "Hinckley and Bosworth",
                        "Horsham",
                        "Hounslow",
                        "Huntingdonshire",
                        "Hyndburn",
                        "Inverclyde",
                        "Ipswich",
                        "Isle of Anglesey",
                        "Isle of Wight",
                        "Islington",
                        "Kensington and Chelsea",
                        "Kettering",
                        "King's Lynn and West Norfolk",
                        "Kingston upon Hull, City of",
                        "Kingston upon Thames",
                        "Kirklees",
                        "Knowsley",
                        "Lambeth",
                        "Lancaster",
                        "Leeds",
                        "Leicester",
                        "Lewes",
                        "Lewisham",
                        "Lichfield",
                        "Lincoln",
                        "Liverpool",
                        "Luton",
                        "Maidstone",
                        "Maldon",
                        "Malvern Hills",
                        "Manchester",
                        "Mansfield",
                        "Medway",
                        "Melton",
                        "Mendip",
                        "Merthyr Tydfil",
                        "Merton",
                        "Mid Devon",
                        "Mid Suffolk",
                        "Mid Sussex",
                        "Middlesbrough",
                        "Midlothian",
                        "Milton Keynes",
                        "Mole Valley",
                        "Monmouthshire",
                        "Moray",
                        "Na h-Eileanan Siar",
                        "Neath Port Talbot",
                        "New Forest",
                        "Newark and Sherwood",
                        "Newcastle upon Tyne",
                        "Newcastle-under-Lyme",
                        "Newham",
                        "Newport",
                        "North Ayrshire",
                        "North Devon",
                        "North East Derbyshire",
                        "North East Lincolnshire",
                        "North Hertfordshire",
                        "North Kesteven",
                        "North Lanarkshire",
                        "North Lincolnshire",
                        "North Norfolk",
                        "North Somerset",
                        "North Tyneside",
                        "North Warwickshire",
                        "North West Leicestershire",
                        "Northampton",
                        "Northumberland",
                        "Norwich",
                        "Nottingham",
                        "Nuneaton and Bedworth",
                        "Oadby and Wigston",
                        "Oldham",
                        "Orkney Islands",
                        "Oxford",
                        "Pembrokeshire",
                        "Pendle",
                        "Perth and Kinross",
                        "Peterborough",
                        "Plymouth",
                        "Portsmouth",
                        "Powys",
                        "Preston",
                        "Reading",
                        "Redbridge",
                        "Redcar and Cleveland",
                        "Redditch",
                        "Reigate and Banstead",
                        "Renfrewshire",
                        "Rhondda Cynon Taf",
                        "Ribble Valley",
                        "Richmond upon Thames",
                        "Richmondshire",
                        "Rochdale",
                        "Rochford",
                        "Rossendale",
                        "Rother",
                        "Rotherham",
                        "Rugby",
                        "Runnymede",
                        "Rushcliffe",
                        "Rushmoor",
                        "Rutland",
                        "Ryedale",
                        "Salford",
                        "Sandwell",
                        "Scarborough",
                        "Scottish Borders",
                        "Sedgemoor",
                        "Sefton",
                        "Selby",
                        "Sevenoaks",
                        "Sheffield",
                        "Shetland Islands",
                        "Shropshire",
                        "Slough",
                        "Solihull",
                        "Somerset West and Taunton",
                        "South Ayrshire",
                        "South Bucks",
                        "South Cambridgeshire",
                        "South Derbyshire",
                        "South Gloucestershire",
                        "South Hams",
                        "South Holland",
                        "South Kesteven",
                        "South Lakeland",
                        "South Lanarkshire",
                        "South Norfolk",
                        "South Northamptonshire",
                        "South Oxfordshire",
                        "South Ribble",
                        "South Somerset",
                        "South Staffordshire",
                        "South Tyneside",
                        "Southampton",
                        "Southend-on-Sea",
                        "Southwark",
                        "Spelthorne",
                        "St Albans",
                        "St. Helens",
                        "Stafford",
                        "Staffordshire Moorlands",
                        "Stevenage",
                        "Stirling",
                        "Stockport",
                        "Stockton-on-Tees",
                        "Stoke-on-Trent",
                        "Stratford-on-Avon",
                        "Stroud",
                        "Sunderland",
                        "Surrey Heath",
                        "Sutton",
                        "Swale",
                        "Swansea",
                        "Swindon",
                        "Tameside",
                        "Tamworth",
                        "Tandridge",
                        "Teignbridge",
                        "Telford and Wrekin",
                        "Tendring",
                        "Test Valley",
                        "Tewkesbury",
                        "Thanet",
                        "Three Rivers",
                        "Thurrock",
                        "Tonbridge and Malling",
                        "Torbay",
                        "Torfaen",
                        "Torridge",
                        "Tower Hamlets",
                        "Trafford",
                        "Tunbridge Wells",
                        "Uttlesford",
                        "Vale of Glamorgan",
                        "Vale of White Horse",
                        "Wakefield",
                        "Walsall",
                        "Waltham Forest",
                        "Wandsworth",
                        "Warrington",
                        "Warwick",
                        "Watford",
                        "Waverley",
                        "Wealden",
                        "Wellingborough",
                        "Welwyn Hatfield",
                        "West Berkshire",
                        "West Devon",
                        "West Dunbartonshire",
                        "West Lancashire",
                        "West Lindsey",
                        "West Lothian",
                        "West Oxfordshire",
                        "West Suffolk",
                        "Westminster",
                        "Wigan",
                        "Wiltshire",
                        "Winchester",
                        "Windsor and Maidenhead",
                        "Wirral",
                        "Woking",
                        "Wokingham",
                        "Wolverhampton",
                        "Worcester",
                        "Worthing",
                        "Wrexham",
                        "Wychavon",
                        "Wycombe",
                        "Wyre",
                        "Wyre Forest",
                        "York"]
    if STRUCTURE is None:
        for AREA_NAME in AREA_NAME_LIST:
            endpoint = (
                'https://api.coronavirus.data.gov.uk/v1/data?'
                f'filters=areaType={AREA_TYPE};areaName={AREA_NAME}&'
                'structure={"areaType":"areaType","areaName":"areaName","areaCode":"areaCode","date":"date","newCasesBySpecimenDate":"newCasesBySpecimenDate","cumCasesBySpecimenDate":"cumCasesBySpecimenDate","newDeaths28DaysByPublishDate":"newDeaths28DaysByPublishDate","cumDeaths28DaysByPublishDate":"cumDeaths28DaysByPublishDate"}&format=json'
            )
            data = get_data(endpoint)
            write_data(data, AREA_TYPE, AREA_NAME)
    else:
        for AREA_NAME in AREA_NAME_LIST:
            endpoint = (
                'https://api.coronavirus.data.gov.uk/v1/data?'
                f'filters=areaType={AREA_TYPE};areaName={AREA_NAME}&'
                f'structure={STRUCTURE}&format=json'
            )
            data = get_data(endpoint)
            write_data(data, AREA_TYPE, AREA_NAME)

def combine_dataframes(AREA_TYPE,WRITE=False):
    data_you_need = pd.DataFrame()
    for infile in glob2.glob(f"data\{AREA_TYPE}\*.xlsx"):
        #print(infile)
        data = pd.read_excel(infile)
        #print(data)
        data_you_need = data_you_need.append(data, ignore_index=True)
        if WRITE == True:
            data_you_need.to_excel(f"data/{AREA_TYPE}/_{AREA_TYPE}_COMBINED_out_data.xlsx",
                            index=False)
    print(f"Data for {AREA_TYPE} combined")
    return data_you_need

def spread_dataframe_columns(AREA_TYPE,WRITE=False):
    df = pd.read_excel(f'data/{AREA_TYPE}/_{AREA_TYPE}_COMBINED_out_data.xlsx')
    spread_df = df.pivot(index='date',columns='areaName',values='newCasesBySpecimenDate')
    print(spread_df.head(),
          spread_df.tail()
          )
    if WRITE==True:
        spread_df.to_excel(f"data/{AREA_TYPE}/_{AREA_TYPE}_SPREAD_out_data.xlsx",
                           index=True)
        print(f'{AREA_TYPE} combined with spread columns file written')
        print(f'Filepath : data/{AREA_TYPE}/_{AREA_TYPE}_SPREAD_out_data.xlsx')

def combine_all_data():
    AREA_TYPE_LIST = ["region",
                      "nation",
                      "utla",
                      "ltla"]
    for AREA_TYPE in AREA_TYPE_LIST:
        combine_dataframes(AREA_TYPE,WRITE=True)

def pull_all_data():
    nation_data()
    region_data()
    lower_tier_local_authority_data()
    upper_tier_local_authority_data()

def nhs_region_admissions():
    "https://api.coronavirus-staging.data.gov.uk/v1/data?filters=areaType=nation&structure=%7B%22areaType%22:%22areaType%22,%22areaName%22:%22areaName%22,%22areaCode%22:%22areaCode%22,%22date%22:%22date%22,%22newAdmissions%22:%22newAdmissions%22,%22cumAdmissions%22:%22cumAdmissions%22%7D&format=json"
    pass


if __name__ == '__main__':

    nation_data()

    structure = '{"areaType":"areaType",' \
                '"areaName":"areaName",' \
                '"areaCode":"areaCode",' \
                '"date":"date",' \
                '"newCasesBySpecimenDate":"newCasesBySpecimenDate",' \
                '"cumCasesBySpecimenDate":"cumCasesBySpecimenDate",' \
                '"newDeaths28DaysByPublishDate":"newDeaths28DaysByPublishDate",' \
                '"cumDeaths28DaysByPublishDate":"cumDeaths28DaysByPublishDate"}'

    nation_data(structure)


    # # ctrl + / block comment


