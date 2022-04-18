----------------------------------------------------------------------------------------------------------------------

Hello there!

				-------------------Dependencies-------------------

This code was built using Python 3.10 on Windows 10. Working on MacOS has not been tested.
Python should be added to your PATH variable.
Run "python --version" in a command prompt to check if it is active
Run "pip --version" in a command prompt to check if it is active
If on Linux RUn "python3 --version" in a command prompt to check if it is active
Please use python3 to run all code in Linux and python when running code in Windows.
Other modules imported are already installed in the native package. No need to explicitly install them.
Elevated Peer has a "doc.json" file. It contains the genesis block. If this information gets corrupted you will not be able
to move forward with the code. Please ensure that you make no modifications to any files before the intial run.

				-------------------Dependencies-------------------


----------------------------------------------------------------------------------------------------------------------


				-------------------Setting up the Code-------------------

Unzip the file into any folder on your local machine. 
The code has to be set up in 2 different directories which represent 2 different nodes on the network.
The elevated peer has the ability to manipulate the blockchain, peer does not.
There will be files on the main directory that can be used to demonstrate the functionality.
If for any reason, elevatedPeer is unable to connect to blockchain.py please eliminate the pycache folder
in the same directory and restart the program again. The pycache folder helps make the connection between the two modules
and will not be present before you run "elevatedPeer.py" for the first time.

`				-------------------Setting up the Code-------------------


----------------------------------------------------------------------------------------------------------------------


				-------------------Passwords-------------------

Enter the password enclosed in ' ' when prompted by the file in front of it.
elevatedPeer.py - 'admin'
These codes are not visible in the code. You will not be able to find them elsewhere. 
I did not add the functionality to change the password, to make sure if you have.

				-------------------Passwords-------------------


----------------------------------------------------------------------------------------------------------------------


			-------------------Typical execution format of each Script-------------------

1. Ask for password. - Authentication
2. Prompt users for various options. Calls functions accordingly.
3. Peers can add new data, update data, retrieve blockchain, perform calculations and exit.
4. Depending on the input from the user, it will connect to the elevatedPeer, or perform relevant functions automatically.

The code established a connection by itself as needed and the user must not be concerned with it.

			-------------------Typical execution format of each Script-------------------


----------------------------------------------------------------------------------------------------------------------


				-------------------Running the Program-------------------

To run this code on your laptop open the Command Prompt in the elevatedPeer and peer1 directories.
"--elevatedPeer" signifies that this command is run on the elevatedPeer Command Prompt.
"--peer" signifies that this command is run on the peer1 Command Prompt.
exact codes are enclosed within " " and and extra instruction within ().
Any instruction is to help you type the correct command and not to written onto the console.

"python elevatedPeer.py localhost 5001" --elevatedPeer
"admin" (On the prompt enter the password) --elevatedPeer
(The password will not be visible to you as you type it.) --elevatedPeer
(After authentication, you do not need to perform any more commands here.) --elevatedPeer
(This will log all activity even from the User's side of it.) --elevatedPeer

"python peer1.py localhost 5001" --peer
(Choose a username) --peer
"2" (To indicate you do not have an existing password) --peer
(Choose a password) --peer
(Now you will have 5 possible operations options listed.
It will be listed as below
Option 1: Send Data
Option 2: Recieve Updated Blockchain
Option 3: Calculate Stats Using Local Blockchain
Option 4: Validate Current Blockchain
Option 5: Close Application
Options 2-5 do not require any additional commands and work what they state.

For Option 1, we have these additional options
Option a: Enter New Vehicle
Option b: Enter Kilometers Traveled Since Last Entry (in most recently added vehicle)

On choosing a 
you will need to enter
the make model and year, and a unique ID that you can choose yourself.
Sample Make, Model and Year are
CITROEN | SUV | 2020
BMW | 118D | 2018
Honda | CIVIC 4DR | 2020
Porsche | Boxster | 2017
These are case sensitive and so please enter them exactly as listed them here.
If you enter a Made, Model, Year that does not exist in the database, the system will prompt
you, asking if you would like to add the vehicle to the database. If you select yes, the system
will prompt you to enter an emission rate in g/km. If you select no, the max emission rate in the database
will be assigned to the car you entered.
On choosing b 
Enter the name of the vehicle that you whose data you want to update.
Simply input the kilometers passed since last updation and press enter.
Enter the relevant options and follow the prompts from the command line application) --peer1

				-------------------Running the Program-------------------


----------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------------------------
