# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import twilio.rest



#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
account_sid = 'AC3d4b7ce0b7510818c7ee21fa3cb61c61'
auth_token = '7384a81381e98d77598ae38a27d3f778'

client = twilio.rest.Client(account_sid,auth_token)

client.api.account.messages.create(
    to="+8613701304797",
    from_="+13158475197",
    body="Hello there!")