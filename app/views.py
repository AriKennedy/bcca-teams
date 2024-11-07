from django.shortcuts import render # type: ignore
from dataclasses import dataclass

@dataclass

class Team:
    name: str
    description: str
    members: str

team_view = {
    'management' : Team('Management', 'As the Management team we are required to manage all of the chores for each day and who does them.', ['Chris', 'Tanner', 'Kilan', 'Aidan']),
    'procurement' : Team('Procurement', 'We buy food to cook so that we can feed you guys at lunch time and we buy supplies like soap, trash, bags etc', ['Jacob', 'Aaron', 'Arthur', 'Markel']),
    'community' : Team('Community', 'Our job is to plan events that bring people together, build lasting relationships, and promote engagement.', ['Arianna', 'Peyton']),
    'documentation' : Team('Documentation', 'Documentation team is responsible for taking photos of guest speaker, community events , and unit projects after taking the pictures depending on the event happening in the photos determines which social media we post on we are also responsible for getting all the photos for the year book.', ['Patrick', 'Jason']),
    }


# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def team_views(request, team):
    if team == 'management' or team == 'procurement' or team == 'community' or team == 'documentation':
        return render(request, 'team_menu.html', {"team_data": team_view[team]})
    