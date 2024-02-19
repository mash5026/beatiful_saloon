from django.core.exceptions import ValidationError

# >-----create choice list for choosing type of agency-----<
OFFICIAL = "official"
OTHER = "other"
LIST_STATUS = [
    ('OFFICIAL',"رسمی"),('OTHER',"متفرقه")
]

MALE = 'm'
FEMALE = 'f'
OTHER = 'o'

CHOICES_LIST = [(MALE,'مرد'),(FEMALE,'بانو'),(OTHER,'دیگر')]

ON_GOING = 'con'
NEGATIVE = 'no'
POSITIVE = 'yes'
NOANSWER = 'not'

LIST_ANSWER = [(ON_GOING, 'در حال پیگیری'), (NEGATIVE, 'عدم تمایل جهت مراجعه'), (POSITIVE, 'پذیرش ثبت وقت'), (NOANSWER, 'عدم پاسخ')]

# >-----create path for saving image with selfname-----<
def path_client(instance,filename):
    return 'jokar/images/{}.{}'.format(instance.name, filename.split(".")[-1])

# >-----create validator for check size image-----<
def validat_image(file):
    if (file.size>20097152):
        raise ValidationError("سایز فایل شما می بایست کمتر از20مگابایت باشد")