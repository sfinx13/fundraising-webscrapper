FUNDRAISER_URL = "https://www.cotizup.com"

URLS_TO_SCRAP = [
    'https://www.cotizup.com/campaigns/solidarite',
    'https://www.cotizup.com/campaigns/humanitaire',
    'https://www.cotizup.com/campaigns/evenements',
    'https://www.cotizup.com/campaigns/projets',
    'https://www.cotizup.com/campaigns/medical',
    'https://www.cotizup.com/campaigns/religion',
    'https://www.cotizup.com/campaigns/animaux',
    'https://www.cotizup.com/campaigns/sports',
    'https://www.cotizup.com/campaigns/autres',
    'https://www.cotizup.com/campaigns?search=pour-moh1'
]

CSV_HEADER = [
    'title',
    'fundraiser',
    'amount_raised',
    'nb_people',
    'amount_total',
    'percentage_raised',
    'average_raised',
    'launched_at'
]

CSV_OUTPUT_FILEPATH = "output/"