from qreader import QReader
from datetime import datetime
import cv2


def reader_id(id_backside_picture):
    qreader = QReader()

    image = cv2.cvtColor(cv2.imread(id_backside_picture), cv2.COLOR_BGR2RGB)

    decoded_text = list(filter(str, qreader.detect_and_decode(image=image)[0].replace('<', ' ').split('\n')))
    nationality = decoded_text[0][2:5]
    card_number = decoded_text[0][5:14]
    personal_number = decoded_text[0][14:]
    surname = decoded_text[-1].split()[0]
    name = decoded_text[-1].split()[1]

    birth_date = decoded_text[1][:6]
    gender = decoded_text[1][7:8]
    expiration_date = decoded_text[1][8:14]

    day_birth = birth_date[-2:]
    month_birth = birth_date[2:4]
    year_birth = birth_date[:2]

    if int(year_birth) > datetime.now().year:
        year_birth = "19" + year_birth
    else:
        year_birth = "20" + year_birth

    birth_date = f"{day_birth}.{month_birth}.{year_birth}"

    day_expiration = expiration_date[-2:]
    month_expiration = expiration_date[2:4]
    year_expiration = expiration_date[:2]

    expiration_date = f"{day_expiration}.{month_expiration}.20{year_expiration}"

    data = {
        "nationality": nationality,
        "card_number": card_number,
        "personal_number": personal_number,
        "surname": surname,
        "name": name,
        "birth_date": birth_date,
        "gender": gender,
        "expiration_date": expiration_date,
    }
    return data
