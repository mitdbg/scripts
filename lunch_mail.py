"""
lunch_mail.py

Lunch mail sends you the weekly group lunch email
It reads from group lunch spreadsheet on Google Sheets and sends the email via MIT SMTP
"""

""" --- Config Start --- """

MIT_SMTP_USERNAME = '' # Mit account username
MIT_SMTP_PASSWORD = '' # Mit account password

from_addr = "Anil Shanbhag <anils@mit.edu>" # Edit this
to_addr = "db@csail.mit.edu"

""" --- Config End --- """

found = False
to_name = ""
to_email = ""

lines = data.split('\n')
for line in lines:
  parts = line.split(',')
  if parts[0] == tomorrow:
    print(parts, line)
    found = True
    to_name = parts[1]
    to_email = parts[2]
    break

if not found:
  print("Didn't find entry for tomorrow")
else:
  smtp = SMTP(host='outgoing.mit.edu')
  smtp.set_debuglevel(debuglevel)
  smtp.connect('outgoing.mit.edu', 465)
  smtp.login(MIT_SMTP_USERNAME, MIT_SMTP_PASSWORD)

  subj = "Group Lunch Tomorrow"
  date = datetime.now().strftime( "%d/%m/%Y %H:%M" )

  message_text = """
%s will be ordering.

The budget is now $350. Make sure to order 1/3rd vegetarian.
As the number of people have increased, please ONLY order catering options. Make sure you  order a day in advance. Some places with catering options: Thelonious Monkfish, India Quality. I have created a section in the spreadsheet for places with catering: feel free to add to it.

Lunch Ordering Schedule: https://docs.google.com/spreadsheets/d/1DSsJprQqvNymSgq8jyukX4L5-iIElFf_TeUufgbN9qw/edit#gid=1196358037
""" % to_name
  # message_text = "\n%s will be ordering. See you there :)\n\n\n--------\nThe budget is now $300. Make sure you order 1/3rd vegetarian.\nLunch Ordering Schedule: https://docs.google.com/spreadsheets/d/1DSsJprQqvNymSgq8jyukX4L5-iIElFf_TeUufgbN9qw/edit#gid=1196358037\n" % to_name

  msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_addr, to_addr, subj, date, message_text )
  #msg = message_text

  smtp.sendmail(from_addr, to_addr, msg)
  smtp.quit()
