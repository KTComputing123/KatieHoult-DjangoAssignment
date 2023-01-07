from django.db import models
import uuid
from django.core.exceptions import ValidationError

# Create your models here.

MONTHS = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
    )

YEARS = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
    ("13", "13"),
    ("14", "14"),
    ("15", "15"),
    ("16", "16"),
    ("17", "17"),
    ("18", "18"),
    ("19", "19"),
    ("20", "20"),
    ("21", "21"),
    ("22", "22"),
    ("23", "23"),
    ("24", "24"),
    ("25", "25"),
    ("26", "26"),
    ("27", "27"),
    ("28", "28"),
    ("29", "29"),
    ("30", "30"),
    ("31", "31"),
    ("32", "32"),
    ("33", "33"),
    ("34", "34"),
    ("35", "35"),
    ("36", "36"),
    ("37", "37"),
    ("38", "38"),
    ("39", "39"),
    ("40", "40"),
    ("41", "41"),
    ("42", "42"),
    ("43", "43"),
    ("44", "44"),
    ("45", "45"),
    ("46", "46"),
    ("47", "47"),
    ("48", "48"),
    ("49", "49"),
    ("50", "50"),
    ("51", "51"),
    ("52", "52"),
    ("53", "53"),
    ("54", "54"),
    ("55", "55"),
    ("56", "56"),
    ("57", "57"),
    ("58", "58"),
    ("59", "59"),
    ("60", "60"),
    ("61", "61"),
    ("62", "62"),
    ("63", "63"),
    ("64", "64"),
    ("65", "65"),
    ("66", "66"),
    ("67", "67"),
    ("68", "68"),
    ("69", "69"),
    ("70", "70"),
    ("71", "71"),
    ("72", "72"),
    ("73", "73"),
    ("74", "74"),
    ("75", "75"),
    ("76", "76"),
    ("77", "77"),
    ("78", "78"),
    ("79", "79"),
    ("80", "80"),
    ("81", "81"),
    ("82", "82"),
    ("83", "83"),
    ("84", "84"),
    ("85", "85"),
    ("86", "86"),
    ("87", "87"),
    ("88", "88"),
    ("89", "89"),
    ("90", "90"),
    ("91", "91"),
    ("92", "92"),
    ("93", "93"),
    ("94", "94"),
    ("95", "95"),
    ("96", "96"),
    ("97", "97"),
    ("98", "98"),
    ("99", "99"),
    )

#register student club model for dummy data to test account manager functionality
class studentClub(models.Model):
    clubName = models.CharField(max_length=20)
  #  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.clubName

#function to validate name field, surname and first intial of first name
def validate_acc_name(value):
    count = 0
    for i in range(0, len(value)):
        if value[i] == ' ':
            count += 1
            i += i
        else:
            i += i
    if count >= 1:
        surnameSplit = value.split(' ', 1)
        print(surnameSplit)
        first, second = surnameSplit
        print(first)
        print(second)
        if len(second) != 1:
            raise ValidationError('Invalid fomrat - please follow correct format')
        else:
            return value
    else:
        raise ValidationError('Invalid format - please follow correct format')#

#function to validate the card number being 16 digits in length
def validate_acc_cardNumber(data):
    if data.isnumeric() == False:
        raise ValidationError('Card number must only contain numerical digits')
    if len(data) != 16:
        raise ValidationError('Invalid initial - please follow correct format')
    else:
        return data

#register the manage account model to allow account managers to input the required data
class ManageAccount(models.Model):
    clubName = models.ForeignKey(studentClub, on_delete=models.SET_NULL, null=True, verbose_name = 'Club Name', help_text="Select registered club")
    acc_name = models.CharField(blank=False, max_length=20, validators=[validate_acc_name], verbose_name = 'Card holder name', help_text="Enter Surname and first name intial e.g Hoult K")
    acc_cardNumber = models.CharField(blank=False, max_length=16, validators=[validate_acc_cardNumber], verbose_name = 'Card number', help_text="Enter card number")
    acc_cardExpiryMonth = models.CharField(blank=False, max_length=2, verbose_name = 'Card expiry month', help_text="Enter expiry month on card MM", choices=MONTHS)
    acc_cardExpiryYear = models.CharField(blank=False, max_length=2, verbose_name = 'Card expiry year', help_text="Enter expiry year on card YY", choices=YEARS)
    acc_discountRate = models.DecimalField(blank=False, decimal_places=0, max_digits=2, verbose_name ='Discount Rate', help_text="Enter discount rate %")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    #format the expiry date field to display month/year as mm/yy
    @property
    def acc_cardExpiryDate(self):
        return '{0} / {1}'.format(self.acc_cardExpiryMonth, self.acc_cardExpiryYear)

    def __str__(self):
        return self.acc_name
