<p align="center">
  <img width="460" height="300" src="https://github.com/Mario181091/Mario_content/blob/master/Senza%20titolo4.jpg">
</p>

# PitE-GameRoom

[![Build Status](https://travis-ci.org/mark91m12/PitE-GameRoom.svg?branch=master)](https://travis-ci.org/mark91m12/PitE-GameRoom)      [![Coverage Status](https://coveralls.io/repos/github/mark91m12/PitE-GameRoom/badge.svg?branch=master)](https://coveralls.io/github/mark91m12/PitE-GameRoom?branch=master)     [![HitCount](http://hits.dwyl.io/mark91m12/PitE-GameRoom.svg)](http://hits.dwyl.io/mark91m12/PitE-GameRoom)

This is the fourth homework of the course "Python in the Enterprise", as requested has been implemented an exention of the Tic Tac Toe multiplayer version (for the previous version you can find further information in this [page](https://github.com/mark91m12/PitE-TicTacToeMultiplayer)), in particular has been implemented a Game Room in which user can choose to play between two type of games ( each in single or multiplayer ).

Is developed Guess the Number game, it is a fun game that challenges users to find a number based on greater than or less than certain number, in eight attempts. First user that guess the number, ein the game

## Features

* possibility to choose Tic Ta Toe game or Guess the number game 
* possibility to choose single or multiplayer game, for both game 
* 1 Vs PC mode
* Player1 Vs Player2 multiplayer mode


## Getting Started

**Prerequisites**
* In order to run this project is important to use python version 3 or upper.                                                    
  Install it with:
  
  ```shell
  $ sudo apt-get install python3
  ```
  now check your version: 
  ```shell
  $ python --version
  ```
## Basic Usage
**Server Side**
* Running this command to start the Server : 

  ```shell
  $ python3 Server.py
  ```
  
  ```shell
     Server listening.
     10.205.12.240
  ```
 

**Client Side**
* Running this command to start the Game : 

  ```shell
  $ python3 Client.py
  ```
  
  ```shell
    ************************************************
    *****               Game Room             ******
    ************************************************
    *                                              *
    *               Play single player  --- s      *
    *                                              *
    *               Play multi player   --- m      *
    *                                              *
    ************************************************


    Please, choose one mode ( s or m ) ---->    



  ```
 
* If user must enter the single type of game he have to choose the type of game he want


   ```shell
    ************************************************
    *                                              *
    *               Play tic tac toe      --- t    *
    *                                              *
    *               Play guess a number   --- g    *
    *                                              *
    ************************************************
    
    Please, choose one game ( t or g ) ---->    


   ```
    
 * If user must enter the multi player type of game he create connection with server and wait for an opponent
    
    
   ``` shell
    please insert ip address of the game server
   >10.205.12.240
    please insert Port number of the game server
   >9999
    waiting for server connection...
    Welcome ('127.0.1.1', 59346)
    Please insert your name
   >Mario
    Prepare to play againts Marco
   ```
   
 * If the opponent come, he is invited to join the match
    
    
   ``` shell
    please insert ip address of the game server
    >10.205.12.240
    please insert Port number of the game server
    >9999
    waiting for server connection...
    Welcome ('10.205.15.69', 55095)
    Please insert your name
    >Marco
    At the moment the server is hosting a guess a number game 
    If you want to join Mario insert 1

   ```
   
   
## Game Screen

In this section are proprosed some screenshots of game, about Tic Tac Toe you can check this [page](https://github.com/mark91m12/PitE-TicTacToeMultiplayer)), about Guess the number follow screenshoots

* In case that user don't match winner number
<p align="center">
  <img width="660" height="300" src="https://github.com/Mario181091/Mario_content/blob/master/fail.png">
</p>


* In case that user win the match
<p align="center">
  <img width="660" height="300" src="https://github.com/Mario181091/Mario_content/blob/master/Schermata%20del%202018-04-16%2022-56-02.png">
</p>

* In case that user lose the match
<p align="center">
  <img width="660" height="300" src="https://github.com/Mario181091/Mario_content/blob/master/lose.png">
</p>


  
  
## Authors

* **Mario Egidio Carricato** - *Erasmus student AGH* - [other projects](https://github.com/mario181091)
* **Marco Amato** - *Erasmus student AGH* - [other projects](https://github.com/mark91m12)
