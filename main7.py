from chat import spy,Spy,ChatMessage,friends,maintain
from steganography.steganography import Steganography
from datetime import datetime
#from list import my_class


STATUS_MESSAGES = ["Stay hungry Stay foolish"]
print "---------welcome to spy chat secret application--------"





#add status-

def add_status(current_status_message):

    updated_status_message = None

    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("Enter status message do you want to set? ")


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message



#   #####------     add new friends-----------####

def add_friend():

 spy.name=raw_input("enter your friend name:")
 while spy.name.isalpha()!= False:

     spy.salutation = raw_input("what you prefer for your friend \"Mr or Ms. \" :")
     value = True
     while value :
         if spy.salutation == 'mr' or spy.salutation =='Mr' or spy.salutation == 'MR' or spy.salutation == 'MS' :
            value =False
         else :
             spy.salutation = raw_input("Please enter the valid salutation \"Mr or Ms. \": ")

     spy.salutation = 'M' +spy.salutation [1:]
     while len(spy.name) <= 0:
         spy.name= raw_input("pleae enter valid name")
         spy.name = spy.salutation + " " + spy.name
         print("WELCOME" + spy.name)
     spy.name =spy.salutation + " " + spy.name

     confirmAge = raw_input(
          "hello spy if your age is in B/W (12-50) years ? if yes then press 'y',if not the press any other option:")
     if confirmAge.upper() !='Y':
         print("sorry ! you can't become a spy.")
         exit()
     else:
         spy.age = int(raw_input("enter your friend age: "))
         while spy.age > 50 or spy.age < 12 :
             spy.age = int(raw_input("Incorrect Age .please enter again"))

         spy.rating =float(raw_input("enter your friend rating: "))
     while spy.rating < 0 or spy.rating > 5:
         spy.rating = float(raw_input("incorrect rating .please enter again : "))

     spyisonline = True
     friends.append(spy)
     print("Now your friend '" + " "+spy.name+"' is online..")
     return len(friends)


#---------select a friend-------

def select_a_friend() :
        print("  list of your friends   ")
        count = 1
        for temp in friends :
            print(str(count)+". "+ temp.salutation +" "+temp.name)
            count +=1

        totalfriends =len(friends)
        select  = int(raw_input("select a  friend:"))
        while select > totalfriends or select <=0 :
            select =int(raw_input("Sorry No name exist in  this position in your friend list. please enter again :"))

        return select-1

# ------------send a secret message----------

def send_a_secret_message():
    #receiver=0
    select = select_a_friend()
   # receiver = select
    original_image= raw_input("Please enter the name of the image:")
    original_image = original_image
    new_img = raw_input("new name of the image:")
    new_img = str(new_img)

    text = raw_input("enter the message you want to send to your friend:")
    Steganography.encode(original_image, new_img, text)
    new_chat = ChatMessage(text,True)


    friends[select].chats.append(new_chat)

    print "Your have successfully send your message"
    print "Choose 4 option to read a secret message"

            ######## ***********read a messsage***********

def read_message():
        sender = select_a_friend()

        output_path = raw_input("what is the name of the file ?")

        secret_text = Steganography.decode(output_path)

        new_chat= ChatMessage(secret_text , False)

        friends[sender].chats.append(new_chat)

       # print secret_text

        if(secret_text== "SOS"):
            print "fight time !!  BE READY,%s is in trouble" % (spy.name)

        if(secret_text== "ST" ):
            print "IT'S SHOW TIME!!  BE READY,%s LET'S PLAY WITH THEM" % (spy.name)

        if(secret_text == "SAVE ME"):
            print "HELP ME!!  GET READY,%s is in trouble" % (spy.name)

        else:
            print" your secret message is " + secret_text

        words= len(secret_text.split())
        if (words >100):
             del friends[sender]
             print"you have lot of chat, now last active spy will get out"
             print"you have %d friends remaining." %(len(friends))
             count=1
             for f in friends:
                 print "%d, %s" %(count,f.name)
                 count+=1
                 maintain_words = maintain(secret_text)


####-----read a chat history-------

def read_history():
    from colorama import init,Fore,Style,Back
    read_for=select_a_friend()

    init(autoreset=True)

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print  '[%s] %s  %s %s: %s' % (chat.time.strftime("%d %B %y"),Fore.BLUE+chat.time.strftime("%H : %M : %S"),  Fore.RED+spy.name         ,  Fore.BLACK +"said :",  chat.message)
        else:
            print  '[%s]  %s %s   %s:   %s' % ( chat.time.strftime("%d %B %y"),Fore.BLUE+chat.time.strftime("%H : %M : %S"), Fore.RED + friends[read_for].name, Fore.BLACK + "received:",  chat.message)

            init(autoreset=False)

#####**********chat historyy function ends*******


def start_chat(spy):


    current_status_message = None


    spy_name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50:


        print "Authentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " +str(spy.rating)+ " Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "**What do you want to do?** \n 1.*** Add a status update*** \n 2.*** Add a friend ***\n 3.*** Send a secret message*** \n 4.*** Read a secret message *** \n 5.*** Read Chats history *** \n 6.*** Close Application *** \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    current_status_message = add_status(current_status_message)
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_a_secret_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice==5:
                    read_history()
                elif menu_choice==6:
                    break
                else:
                    show_menu = False
    else:
        print 'Sorry you dont have correct age to be a spy'

var = True
while var:

    question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
    existing = raw_input(question)

        # if existing.upper()=='Y' or existing.upper() == 'Y':
    if existing=='Y':
            print("name: " + spy.salutation + spy.name)
            var = False
            start_chat(spy)

            # we are happy with your value

    elif existing== 'N':
        var =0
        spy = Spy('','',0,0.0)

        spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)

        spy_is_online = True

        start_chat(spy)

    else:
        print"please enter in Capital letter"

###-----project end----------






























