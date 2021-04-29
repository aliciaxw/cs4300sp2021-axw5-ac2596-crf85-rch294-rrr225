import requests
from bs4 import BeautifulSoup
import time
import json
import re

dropdown = """<div class="ui-selectmenu-menu ui-front ui-selectmenu-open" style="top: 888px; left: 142px;"><ul aria-hidden="false" aria-labelledby="trail-list-button" id="trail-list-menu" class="ui-menu ui-widget ui-widget-content ui-corner-bottom" role="listbox" tabindex="0" aria-activedescendant="ui-id-2" aria-disabled="false" style="width: 249px;"><li class="ui-menu-item" id="ui-id-1" tabindex="-1" role="option">By Site</li><li class="ui-menu-item ui-state-focus" id="ui-id-2" tabindex="-1" role="option">&nbsp;</li><li class="ui-menu-item" id="ui-id-3" tabindex="-1" role="option">Abbott Loop East</li><li class="ui-menu-item" id="ui-id-4" tabindex="-1" role="option">Abbott Loop West</li><li class="ui-menu-item" id="ui-id-5" tabindex="-1" role="option">Bald Hill Natural Area</li><li class="ui-menu-item" id="ui-id-6" tabindex="-1" role="option">Beebe Lake Natural Area</li><li class="ui-menu-item" id="ui-id-7" tabindex="-1" role="option">Black Diamond Trail</li><li class="ui-menu-item" id="ui-id-8" tabindex="-1" role="option">Bob Cameron Loop</li><li class="ui-menu-item" id="ui-id-9" tabindex="-1" role="option">Bock-Harvey Nature Preserve</li><li class="ui-menu-item" id="ui-id-10" tabindex="-1" role="option">Buttermilk Falls State Park</li><li class="ui-menu-item" id="ui-id-11" tabindex="-1" role="option">Campbell Meadows</li><li class="ui-menu-item" id="ui-id-12" tabindex="-1" role="option">Carl Sagan Planet Walk</li><li class="ui-menu-item" id="ui-id-13" tabindex="-1" role="option">Cascadilla Gorge Natural Area</li><li class="ui-menu-item" id="ui-id-14" tabindex="-1" role="option">Cascadilla Meadows Natural Area</li><li class="ui-menu-item" id="ui-id-15" tabindex="-1" role="option">Cayuga Nature Center</li><li class="ui-menu-item" id="ui-id-16" tabindex="-1" role="option">Cayuga Trail</li><li class="ui-menu-item" id="ui-id-17" tabindex="-1" role="option">Cayuga Waterfront Trail</li><li class="ui-menu-item" id="ui-id-18" tabindex="-1" role="option">City of Ithaca Cemetery Walk</li><li class="ui-menu-item" id="ui-id-19" tabindex="-1" role="option">Cornell Botanic Gardens</li><li class="ui-menu-item" id="ui-id-20" tabindex="-1" role="option">Danby State Forest Chestnut Lean-to</li><li class="ui-menu-item" id="ui-id-21" tabindex="-1" role="option">Dotson Park</li><li class="ui-menu-item" id="ui-id-22" tabindex="-1" role="option">Dryden Rail Trail</li><li class="ui-menu-item" id="ui-id-23" tabindex="-1" role="option">Dunlop Meadow Natural Area</li><li class="ui-menu-item" id="ui-id-24" tabindex="-1" role="option">East Ithaca Recreation Way</li><li class="ui-menu-item" id="ui-id-25" tabindex="-1" role="option">Edwards Lake Cliffs Natural Area</li><li class="ui-menu-item" id="ui-id-26" tabindex="-1" role="option">Eldridge Wilderness Preserve</li><li class="ui-menu-item" id="ui-id-27" tabindex="-1" role="option">Ellis Hollow Nature Preserve</li><li class="ui-menu-item" id="ui-id-28" tabindex="-1" role="option">Ellis Hollow Wetlands - Dewey Preserve</li><li class="ui-menu-item" id="ui-id-29" tabindex="-1" role="option">Emilie Jonas Falls Nature Preserve</li><li class="ui-menu-item" id="ui-id-30" tabindex="-1" role="option">Fall Creek Gorge Natural Area</li><li class="ui-menu-item" id="ui-id-31" tabindex="-1" role="option">Fall Creek Valley North Natural Area</li><li class="ui-menu-item" id="ui-id-32" tabindex="-1" role="option">Fall Creek Valley South Natural Area</li><li class="ui-menu-item" id="ui-id-33" tabindex="-1" role="option">Finger Lakes Trail</li><li class="ui-menu-item" id="ui-id-34" tabindex="-1" role="option">Fischer Old-growth Forest Natural Area</li><li class="ui-menu-item" id="ui-id-35" tabindex="-1" role="option">F.R Newman Arboretum</li><li class="ui-menu-item" id="ui-id-36" tabindex="-1" role="option">Frost Ravine Natural Area</li><li class="ui-menu-item" id="ui-id-37" tabindex="-1" role="option">Genung Nature Preserve</li><li class="ui-menu-item" id="ui-id-38" tabindex="-1" role="option">Habitat Preserve</li><li class="ui-menu-item" id="ui-id-39" tabindex="-1" role="option">Hammond Hill State Forest</li><li class="ui-menu-item" id="ui-id-40" tabindex="-1" role="option">Inlet Island Promenade</li><li class="ui-menu-item" id="ui-id-41" tabindex="-1" role="option">Ithaca College Natural Lands</li><li class="ui-menu-item" id="ui-id-42" tabindex="-1" role="option">Ithaca Falls</li><li class="ui-menu-item" id="ui-id-43" tabindex="-1" role="option">Jennings Pond</li><li class="ui-menu-item" id="ui-id-44" tabindex="-1" role="option">Kingsbury Woods Conservation Area</li><li class="ui-menu-item" id="ui-id-45" tabindex="-1" role="option">Lansing Center Trail</li><li class="ui-menu-item" id="ui-id-46" tabindex="-1" role="option">Lick Brook - Finger Lakes Land Trust</li><li class="ui-menu-item" id="ui-id-47" tabindex="-1" role="option">Lick Brook Natural Area</li><li class="ui-menu-item" id="ui-id-48" tabindex="-1" role="option">Lighthouse Point Natural Area</li><li class="ui-menu-item" id="ui-id-49" tabindex="-1" role="option">Lindsay-Parsons Biodiversity Preserve</li><li class="ui-menu-item" id="ui-id-50" tabindex="-1" role="option">Mann Library Slope Natural Area</li><li class="ui-menu-item" id="ui-id-51" tabindex="-1" role="option">Monkey Run Natural Area</li><li class="ui-menu-item" id="ui-id-52" tabindex="-1" role="option">Mundy Wildflower Garden</li><li class="ui-menu-item" id="ui-id-53" tabindex="-1" role="option">Northeast Ithaca Recreation Way</li><li class="ui-menu-item" id="ui-id-54" tabindex="-1" role="option">O.D. von Engeln Preserve at Malloryville</li><li class="ui-menu-item" id="ui-id-55" tabindex="-1" role="option">Palmer Woods Natural Area</li><li class="ui-menu-item" id="ui-id-56" tabindex="-1" role="option">Park Park</li><li class="ui-menu-item" id="ui-id-57" tabindex="-1" role="option">Polson Natural Area</li><li class="ui-menu-item" id="ui-id-58" tabindex="-1" role="option">Purvis Bog Natural Area</li><li class="ui-menu-item" id="ui-id-59" tabindex="-1" role="option">Renwick Slope Natural Area</li><li class="ui-menu-item" id="ui-id-60" tabindex="-1" role="option">Renwick Wildwoods</li><li class="ui-menu-item" id="ui-id-61" tabindex="-1" role="option">Ridgeway Swamp</li><li class="ui-menu-item" id="ui-id-62" tabindex="-1" role="option">Riemen Woods Nature Preserve</li><li class="ui-menu-item" id="ui-id-63" tabindex="-1" role="option">Ringwood Ponds Natural Area</li><li class="ui-menu-item" id="ui-id-64" tabindex="-1" role="option">Robert H. Treman State Park</li><li class="ui-menu-item" id="ui-id-65" tabindex="-1" role="option">Roy H. Park Preserve</li><li class="ui-menu-item" id="ui-id-66" tabindex="-1" role="option">Salt Point</li><li class="ui-menu-item" id="ui-id-67" tabindex="-1" role="option">Sapsucker Woods</li><li class="ui-menu-item" id="ui-id-68" tabindex="-1" role="option">Shindagin Hollow State Forest</li><li class="ui-menu-item" id="ui-id-69" tabindex="-1" role="option">Six Mile Creek Natural Area</li><li class="ui-menu-item" id="ui-id-70" tabindex="-1" role="option">Sixmile Creek Walk</li><li class="ui-menu-item" id="ui-id-71" tabindex="-1" role="option">Slim Jim Woods Natural Area</li><li class="ui-menu-item" id="ui-id-72" tabindex="-1" role="option">Smith Woods</li><li class="ui-menu-item" id="ui-id-73" tabindex="-1" role="option">South Danby to Tamarack Lean-to</li><li class="ui-menu-item" id="ui-id-74" tabindex="-1" role="option">South Hill Recreation Way</li><li class="ui-menu-item" id="ui-id-75" tabindex="-1" role="option">Stevenson Forest Preserve</li><li class="ui-menu-item" id="ui-id-76" tabindex="-1" role="option">Stewart Park</li><li class="ui-menu-item" id="ui-id-77" tabindex="-1" role="option">Tarr-Young Natural Area</li><li class="ui-menu-item" id="ui-id-78" tabindex="-1" role="option">Taughannock Falls State Park</li><li class="ui-menu-item" id="ui-id-79" tabindex="-1" role="option">Yellow Barn State Forest</li></ul></div>"""
START_URL = "https://ithacatrails.org/site/"

test_site = "Abbott Loop East"
def convert_to_url(site):
    return '%20'.join(site.split(" "))

def scrape_trail(section):
    trail = {}
    # trail['Ithacatrails ID'] = id
    trail['Name'] = section.find('h1').get_text()
    for link in section.find_all('p', limit=2):
        text = link.get_text()
        if text.startswith('Trail distance'):
            trail['Distance'] = float(re.findall(r"[-+]?\d*\.\d+|\d+", text)[0])
        elif text.startswith('Difficulty'):
            trail['Difficulty'] = text.split(": ")[1].split('\n')[0]

    #get description
    # description_link = section.find(text = 'Part of the ').findNext('a').get('href')
    # r = requests.get(description_link)
    # soup = BeautifulSoup(r.content, "html5lib")
    # description_section = soup.find(True, {"class": "trail-info two-thirds column"})
    # trail['Description'] = description_section.find_all('p', limit=5)[4].get_text()
    trail['Description'] = section.find_all('p', limit = 5)[4].get_text()
    #get gps coords
    coords = section.findNext('h3').findNext('p').get_text()
    trail['GPS'] = [float(coord) for coord in re.findall(r"[-+]?\d*\.\d+|\d+", coords)] 
    # get parking locations
    locations = {}
    for link in section.findNext(text = 'Parking Locations').findNext('ul').findAll('li'):
        kind, spot = link.get_text().split(': ')[:2]
        kind = kind[:-1].lower()
        spots = locations.get(kind, [])
        spots.append(spot)
        locations[kind] = spots
    trail['Parking Locations'] = locations
    #get trail attributes
    attributes = []
    for link in section.findNext(text = 'Trail Attributes').findNext('ul').findAll('li'):
        attributes.append(link.get_text())
    trail['Trail Attributes'] = attributes
    #get more info
    extras = []
    for link in section.find('h3', text = 'More Info').findNextSiblings('p', {"class": None}):
        extras.append(" ".join(link.get_text().split()))
    trail['More Info'] = extras
    return trail

def scrape_all_sites():
    sites = {}
    site_names = []
    soup = BeautifulSoup(dropdown, "html5lib")

    for link in soup.find_all('li'):
        site_names.append(link.get_text())
    site_names = site_names[2:]
    print(site_names)
    for site in site_names:
        trail_url = START_URL + convert_to_url(site)
        r = requests.get(trail_url)
        site_soup = BeautifulSoup(r.content, "html5lib")
        section = site_soup.find(True, {"class": "trail-info two-thirds column"})
        if section:
            name = section.find('h1').get_text()
            # print(name)
            sites[name] = scrape_trail(section)
    with open('ithacatrails.json', 'w') as fout:
            json.dump(sites, fout, indent=4)
    print(sites['Abbott Loop East'])

scrape_all_sites()
# print(convert_to_url(test_site))