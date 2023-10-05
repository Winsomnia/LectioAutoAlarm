import lectio
import time
import datetime
import requests
import re

# configurables
Macrodroid_adress = "https://trigger.macrodroid.com/{indsæt_personligMacroDroidWebHookID}/"
RoutineCheckupDelaymin = 5
WakeUpDelay = 60
client = lectio.sdk(brugernavn="", adgangskode="", skoleId="")

#Hardcodes
i_morgen = datetime.date.today() + datetime.timedelta(days=1)
i_dag = datetime.date.today()
x = 0

while True:
    
    #Tjekker om klokken er over eller under 16. hvis over 16, tjekker den for den følgene dags modul, og sætter alarmen dertil, hvis ikke, tjekker den samme dags modul og sætter alarmen derti.
    if(datetime.datetime.now().hour>=16):
        skema = client.skema(uge=i_morgen.isocalendar()[1], år=i_morgen.year,id=client.elevId)
    else:
        skema = client.skema(uge=i_dag.isocalendar()[1], år=i_dag.year,id=client.elevId)
            
    #finder det første modul som ikke er aflyst og gemmer mødetiden for det modul.
    for module in skema["moduler"]:
        if module["status"] != "aflyst":
            mødetid = module["tidspunkt"]
            break

    # omdanner mødetiden fra 00:00 format til minutter(int)
    def extract_and_convert(time_string):
        # Extract the first time period using regex
        match = re.search(r'(\d{2}:\d{2})', time_string)
        if match:
            time_period = match.group(1)
            
            # Split hours and minutes
            hours, minutes = map(int, time_period.split(':'))
            
            # Convert to minutes
            minutes = (hours * 60) + minutes

            return minutes
    mødetid_in_minutes = extract_and_convert(mødetid)
    
    # tjekker om mødetiden er ændret (altså at et modul er blevet aflyst)
    if(x != mødetid_in_minutes):
        # udregner nuværende tid i minutter
        current_time = datetime.datetime.now()
        current_time_in_minutes = (current_time.hour * 60) + current_time.minute

        # bruger nuværende tid i minutter til at offset alarmen så den ringer når den skal
        # tjekker om den skal sætte alarmen til i dag (hvis Fx. modulet blev aflyst 6:00)
        # eller i morgen (Hvis Fx. modulet blev aflyst 19:00)
        if current_time.hour >= 16:
            timeInminutes = mødetid_in_minutes + (24 * 60) - current_time_in_minutes
        elif current_time.hour < 16:
            timeInminutes = mødetid_in_minutes - current_time_in_minutes

        # offsetter alarmen med mængden det tager brugeren at gøre sig klar og komme i skole om morgenen
        timeInminutes -= WakeUpDelay

        print(mødetid_in_minutes)
        print(timeInminutes)

        # Sender en post request til macrodroid webhooken med information om hvornår alarmen skal sættes til
        requests.post(Macrodroid_adress + f"LectioAlarm?LectioTimerMinutes={timeInminutes}")
    # sætter x til den nye mødetid så loopet kan ignorer den øvre proces hvis ikke mødetiden har ændret sig    
    x = mødetid_in_minutes
    # venter en bestemt mængde minutter før scriptet tjekker om et modul er blevet aflyst igen (default 5 minutter)
    time.sleep(RoutineCheckupDelaymin * 60)




