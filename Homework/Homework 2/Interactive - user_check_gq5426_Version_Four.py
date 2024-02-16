{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "isInteractiveWindowMessageCell": true
   },
   "source": [
    "Connected to Python 3.12.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'str' object has no attribute 'copy'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32mc:\\Users\\Phill\\OneDrive\\Desktop\\Programming For Cool Kids\\CSC 4110\\Homework\\Homework 2\\user_check_gq5426_Version_Threepy.py\u001b[0m in \u001b[0;36mline 55\n\u001b[0;32m     <a href='file:///c%3A/Users/Phill/OneDrive/Desktop/Programming%20For%20Cool%20Kids/CSC%204110/Homework/Homework%202/user_check_gq5426_Version_Threepy.py?line=43'>44</a>\u001b[0m             tempstr \u001b[39m+\u001b[39m\u001b[39m=\u001b[39m i        \n\u001b[0;32m     <a href='file:///c%3A/Users/Phill/OneDrive/Desktop/Programming%20For%20Cool%20Kids/CSC%204110/Homework/Homework%202/user_check_gq5426_Version_Threepy.py?line=45'>46</a>\u001b[0m \u001b[39m    \u001b[39m\u001b[39m\"\"\"   \u001b[39;00m\n\u001b[0;32m     <a href='file:///c%3A/Users/Phill/OneDrive/Desktop/Programming%20For%20Cool%20Kids/CSC%204110/Homework/Homework%202/user_check_gq5426_Version_Threepy.py?line=46'>47</a>\u001b[0m \u001b[39m    #Routine B, don't use a forloop, but do the same thing\u001b[39;00m\n\u001b[0;32m     <a href='file:///c%3A/Users/Phill/OneDrive/Desktop/Programming%20For%20Cool%20Kids/CSC%204110/Homework/Homework%202/user_check_gq5426_Version_Threepy.py?line=47'>48</a>\u001b[0m \u001b[39m    temp = len(user_input)\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m     <a href='file:///c%3A/Users/Phill/OneDrive/Desktop/Programming%20For%20Cool%20Kids/CSC%204110/Homework/Homework%202/user_check_gq5426_Version_Threepy.py?line=52'>53</a>\u001b[0m \u001b[39m        i += 1\u001b[39;00m\n\u001b[0;32m     <a href='file:///c%3A/Users/Phill/OneDrive/Desktop/Programming%20For%20Cool%20Kids/CSC%204110/Homework/Homework%202/user_check_gq5426_Version_Threepy.py?line=53'>54</a>\u001b[0m \u001b[39m    \"\"\"\u001b[39;00m\n\u001b[1;32m---> <a href='file:///c%3A/Users/Phill/OneDrive/Desktop/Programming%20For%20Cool%20Kids/CSC%204110/Homework/Homework%202/user_check_gq5426_Version_Threepy.py?line=54'>55</a>\u001b[0m     ml\u001b[39m.\u001b[39mappend(tempstr\u001b[39m.\u001b[39;49mcopy())\n\u001b[0;32m     <a href='file:///c%3A/Users/Phill/OneDrive/Desktop/Programming%20For%20Cool%20Kids/CSC%204110/Homework/Homework%202/user_check_gq5426_Version_Threepy.py?line=56'>57</a>\u001b[0m     user_input \u001b[39m=\u001b[39m \u001b[39minput\u001b[39m(\u001b[39m\"\u001b[39m\u001b[39mPlease enter a username:\u001b[39m\u001b[39m\"\u001b[39m )\n\u001b[0;32m     <a href='file:///c%3A/Users/Phill/OneDrive/Desktop/Programming%20For%20Cool%20Kids/CSC%204110/Homework/Homework%202/user_check_gq5426_Version_Threepy.py?line=57'>58</a>\u001b[0m \u001b[39m#END\u001b[39;00m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'str' object has no attribute 'copy'"
     ]
    }
   ],
   "source": [
    "#Revision 2 BEGIN\n",
    "#May Wandyez 1/25/2024\n",
    "\"\"\"\n",
    "ASSIGNMENT:\n",
    "Write a program (programs) that prompts y\n",
    "ou to add a username \n",
    "to a sequence (collection) of stored names.\n",
    "\n",
    " It must continuously prompt for more user names\n",
    " until a condition, such as typing ‘exit’ is met\n",
    " .\n",
    "\n",
    "The company you work for has a policy that says\n",
    "“no characters such as “#,^% or digits such as \n",
    "1,2,3,4,5,6,7 are ever used in usernames,” \n",
    "and all characters other than letters are \n",
    "filtered (see Version One and Version \n",
    "Two below for further detail).\n",
    "\n",
    "VERSION 1\n",
    "A ‘for loop’ is used to filter out unwanted characters; \n",
    "a STRING is used to store, add, and maintain users. \n",
    "This is to be referred to as ‘Routine A’ in your comments.\n",
    "\n",
    "VERSION 2\n",
    "You must NOT use a ‘for loop.’ Like Routine A, a STRING is used to store, add, and maintain users. \n",
    "This is to be referred to as ‘Routine B’ in your comments.\n",
    "\n",
    "VERSION 3\n",
    "It's version 1 except with a list instead of a string\n",
    "\"\"\"\n",
    "#master list to store users for version 1\n",
    "ml = []\n",
    "#initial user input to initiate loop\n",
    "user_input = input(\"Please enter a username:\" )\n",
    "\n",
    "#loop to continuously add usernames\n",
    "while(user_input != \"end\" and user_input != \"exit\"):\n",
    "    \n",
    "    #Routine A use a for loop to filter, string used to add\n",
    "    tempstr = \"\"\n",
    "    for i in user_input:\n",
    "        if(i.isalpha()):\n",
    "            tempstr += i        \n",
    "    \n",
    "    \"\"\"   \n",
    "    #Routine B, don't use a forloop, but do the same thing\n",
    "    temp = len(user_input)\n",
    "    i = 0\n",
    "    while(i<temp):\n",
    "        if(user_input[i].isalpha()):\n",
    "            ml += user_input[i] \n",
    "        i += 1\n",
    "    \"\"\"\n",
    "    ml.append(tempstr.copy())\n",
    "    \n",
    "    user_input = input(\"Please enter a username:\" )\n",
    "#END"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Revision 2 BEGIN\n",
    "#May Wandyez 1/25/2024\n",
    "\"\"\"\n",
    "ASSIGNMENT:\n",
    "Write a program (programs) that prompts y\n",
    "ou to add a username \n",
    "to a sequence (collection) of stored names.\n",
    "\n",
    " It must continuously prompt for more user names\n",
    " until a condition, such as typing ‘exit’ is met\n",
    " .\n",
    "\n",
    "The company you work for has a policy that says\n",
    "“no characters such as “#,^% or digits such as \n",
    "1,2,3,4,5,6,7 are ever used in usernames,” \n",
    "and all characters other than letters are \n",
    "filtered (see Version One and Version \n",
    "Two below for further detail).\n",
    "\n",
    "VERSION 1\n",
    "A ‘for loop’ is used to filter out unwanted characters; \n",
    "a STRING is used to store, add, and maintain users. \n",
    "This is to be referred to as ‘Routine A’ in your comments.\n",
    "\n",
    "VERSION 2\n",
    "You must NOT use a ‘for loop.’ Like Routine A, a STRING is used to store, add, and maintain users. \n",
    "This is to be referred to as ‘Routine B’ in your comments.\n",
    "\n",
    "VERSION 3\n",
    "It's version 1 except with a list instead of a string\n",
    "\"\"\"\n",
    "#master list to store users for version 1\n",
    "ml = []\n",
    "#initial user input to initiate loop\n",
    "user_input = input(\"Please enter a username:\" )\n",
    "\n",
    "#loop to continuously add usernames\n",
    "while(user_input != \"end\" and user_input != \"exit\"):\n",
    "    \n",
    "    #Routine A use a for loop to filter, string used to add\n",
    "    tempstr = \"\"\n",
    "    for i in user_input:\n",
    "        if(i.isalpha()):\n",
    "            tempstr += i        \n",
    "    \n",
    "    \"\"\"   \n",
    "    #Routine B, don't use a forloop, but do the same thing\n",
    "    temp = len(user_input)\n",
    "    i = 0\n",
    "    while(i<temp):\n",
    "        if(user_input[i].isalpha()):\n",
    "            ml += user_input[i] \n",
    "        i += 1\n",
    "    \"\"\"\n",
    "    ml.append(tempstr)\n",
    "    \n",
    "    user_input = input(\"Please enter a username:\" )\n",
    "#END"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Hamtaro', 'Jamiroquai', 'ApplesauceMcGee']"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ml"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
