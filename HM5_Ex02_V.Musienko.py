name_recipient = input('\nИмя получателя >>> ')
last_name_recipient = input('Фамилия получателя >>> ')

name_sender = input('Имя отправителя >>> ')
last_name_sender = input('Фамилию отправителя >>> ')

senders_position = input('Введите свою должность в компании >>> ')

def message_sender(name_recipient, last_name_recipient, name_sender, last_name_sender,
senders_position):

    mailling_list = f"""
\nDear {name_recipient} {last_name_recipient},
We are lorem ipsum dolor sit amet, consectetur adipiscing elit.
Vestibulum in faucibus massa.
Suspendisse at ex varius, porttitor eros sit amet, sagittis nibh.
In vel est a tortor tempor luctus a.
________________________________________________________________
{name_sender} {last_name_sender}
{senders_position}.\n"""

    print(mailling_list)

message_sender(name_recipient, last_name_recipient, name_sender, last_name_sender,
senders_position)
