from advertisment import Advertisment
from equipment_entry import EquipmentEntry
from equipment_register import *

ads=[
    # sound ads
    Advertisment(
        title='Soundpaket One',
        price=49.0,
        equipment=[
            EquipmentEntry(top_big, 1)
        ],
        description_intro='none'
    ),
    Advertisment(
        title='Soundpaket Basic',
        price=99.0,
        equipment=[
            EquipmentEntry(sub, 1),
            EquipmentEntry(top_big, 1)
        ],
        description_intro='none'
    ),
    Advertisment(
        title='Soundpaket Party',
        price=119.0,
        equipment=[
            EquipmentEntry(sub, 1),
            EquipmentEntry(top_small, 2)
        ],
        description_intro='none'
    ),
    Advertisment(
        title='Soundpaket Party+',
        price=159.0,
        equipment=[
            EquipmentEntry(sub, 2),
            EquipmentEntry(top_small, 2)
        ],
        description_intro='none'
    ),
    Advertisment(
        title='Soundpaket Pro',
        price=259.0,
        equipment=[
            EquipmentEntry(sub, 4),
            EquipmentEntry(top_small, 2),
            EquipmentEntry(top_big, 1)
        ],
        description_intro='none'
    ),

    # light ads
    Advertisment(
        title='Lichtpaket Ambient Light',
        price=79.0,
        equipment=[
            EquipmentEntry(ali_pair, 8)
        ],
        description_intro='none'
    ),
    Advertisment(
        title='Lichtpaket Table Light',
        price=59.0,
        equipment=[
            EquipmentEntry(ali_pair, 4),
            EquipmentEntry(led_bar, 2),
            EquipmentEntry(superfly, 2),
        ],
        description_intro='none'
    ),
    Advertisment(
        title='Lichtpaket Party',
        price=79.0,
        equipment=[
            EquipmentEntry(ali_pair, 4),
            EquipmentEntry(superfly, 2),
            EquipmentEntry(multi_fx_bar, 1),
            EquipmentEntry(light_pole, 1),
        ],
        description_intro='none'
    ),
    Advertisment(
        title='Lichtpaket Party+',
        price=129.0,
        equipment=[
            EquipmentEntry(traverse_mid, 1),
            EquipmentEntry(ali_pair, 8),
            EquipmentEntry(led_bar, 2),
            EquipmentEntry(superfly, 2),
            EquipmentEntry(multi_fx_bar, 1),
        ],
        description_intro='none'
    ),
    Advertisment(
        title='Lichtpaket Pro',
        price=219.0,
        equipment=[
            EquipmentEntry(traverse_big, 1),
            EquipmentEntry(ali_pair, 8),
            EquipmentEntry(led_bar, 2),
            EquipmentEntry(superfly, 2),
            EquipmentEntry(multi_fx_bar, 1),
            EquipmentEntry(laser, 1),
            EquipmentEntry(strobe, 1),
            EquipmentEntry(moving_head, 2),
        ],
        description_intro='none'
    )
]

desc_outro = ('Des Weiteren bieten wir von einer kompletten Musikanlage über einzelne Fullrange Lautsprecher und Subwoofer bis hin zum Rundum-sorglos-Paket alles an. Auch mit vielen weiteren Lichtern, Nebelmaschine, kabelgebundenem Mikrofon und Funkmikrofon sind wir ausgestattet.\n'+
              'Lass dich von unseren Bildern inspirieren.\n'+
              'instagram.com/threebpm/\n'+
              'www.threebpm.de\n'+
              'Wenn Du noch keinen DJ hast, kannst du unseren DJ Veit von – 3 BPM – direkt mitbuchen.\n'+
              'Wir freuen uns auf Deine Anfrage')
