{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "84190d3f-a0d7-4cf7-b357-529e2b20c56e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "70b9cd81-97a5-492e-9794-3fdba62d8fd7",
   "metadata": {},
   "outputs": [],
   "source": [
    "x= pd.read_csv('Admin.csv')"
   ]
  },
  {
   "cell_type": "raw",
   "id": "e3ca76fe-62aa-4566-8c1e-003137bedb22",
   "metadata": {},
   "source": [
    "admin credentials = Admin.csv\n",
    "Voter credentials=Voter_Credentials.csv\n",
    "\n",
    "Voter data=Voter_data.xlsx\n",
    "voter's vote=Voter_Vote_data.xlsx\n",
    "\n",
    "campaign data=campaign_data.xlsx\n",
    "\n",
    "\n",
    "candidate data=Candidate_data.xlsx"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "27893a36-1798-46e7-98ca-337c29e7937f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Password</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Shivani</td>\n",
       "      <td>123</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Aman</td>\n",
       "      <td>456</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Name  Password\n",
       "0  Shivani       123\n",
       "1     Aman       456"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#admin details \n",
    "x= pd.read_csv('Admin.csv')\n",
    "x= {'Name':['Shivani','Aman'],'Password':[123,456]}\n",
    "df= pd.DataFrame(data=x)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4682edbd-235e-4f1e-8b80-226960328b5e",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-ce6f9023e33e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     18\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Too many incorrect attempts. Login failed.\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     19\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 20\u001b[1;33m \u001b[0mAdmin_log\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-4-ce6f9023e33e>\u001b[0m in \u001b[0;36mAdmin_log\u001b[1;34m()\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mAdmin_log\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 8\u001b[1;33m         \u001b[0mname\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Enter name: '\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      9\u001b[0m         \u001b[0mpassw\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Enter password: '\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[1;34m(self, prompt)\u001b[0m\n\u001b[0;32m    858\u001b[0m                 \u001b[1;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    859\u001b[0m             )\n\u001b[1;32m--> 860\u001b[1;33m         return self._input_request(str(prompt),\n\u001b[0m\u001b[0;32m    861\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    862\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[1;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[0;32m    902\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    903\u001b[0m                 \u001b[1;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 904\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Interrupted by user\"\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    905\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    906\u001b[0m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Invalid Message:\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "#1.1 Admin_login\n",
    "import pandas as pd\n",
    "\n",
    "# Assuming you have loaded your DataFrame 'df' from the CSV file\n",
    "\n",
    "def Admin_log():\n",
    "    for i in range(3):\n",
    "        name = input('Enter name: ')\n",
    "        passw = int(input('Enter password: '))\n",
    "        \n",
    "        # Check if the entered name and password exist in any row of the DataFrame\n",
    "        if any((df['Name'] == name) & (df['Password'] == passw)):\n",
    "            print(\"Login successful!\")\n",
    "            return Admin_portal()\n",
    "        else:\n",
    "            print(\"Invalid credentials. Please try again.\")\n",
    "\n",
    "    print(\"Too many incorrect attempts. Login failed.\")\n",
    "    return None\n",
    "Admin_log()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "f8b32e0f-874f-4872-9f61-535af05232f7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Login ID</th>\n",
       "      <th>Password</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>100</td>\n",
       "      <td>123</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>101</td>\n",
       "      <td>234</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>102</td>\n",
       "      <td>345</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>103</td>\n",
       "      <td>456</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>104</td>\n",
       "      <td>567</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Login ID  Password\n",
       "0       100       123\n",
       "1       101       234\n",
       "2       102       345\n",
       "3       103       456\n",
       "4       104       567"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#voter predefined credentials \n",
    "v=pd.read_csv('Voter_Credentials.csv')\n",
    "vf= pd.DataFrame(data=v)\n",
    "\n",
    "vf\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "5da5124f-26eb-4681-bcfd-0a53bcfe4cc6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter yout login id 100\n",
      "enter password 123\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Voter Login successful!\n",
      "welcome voter, please select your preference \n",
      "1: see live campaign\n",
      "2: vote for campaign\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter preference 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hey! Voter, Are you ready to decide whose gonna rule the world??\n",
      "  party_name  Campaign Name\n",
      "0        CNG  shivani nagar\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your name Shivani Nagar\n",
      "enter your id 100\n",
      "enter to which party you want to succeed  BJP\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You Sucessfully Voted\n"
     ]
    }
   ],
   "source": [
    "#1.2\n",
    "def voter_login():\n",
    "    for i in range(3):\n",
    "        login_id= int(input('enter yout login id'))\n",
    "        password= int(input('enter password'))\n",
    "        \n",
    "        # Check if the entered login id and password exist in any row of the voter DataFrame\n",
    "        if any((vf['Login ID'] == login_id) & (df['Password'] == password)):\n",
    "            print(\"Voter Login successful!\")\n",
    "            return voter_portal()\n",
    "        else:\n",
    "            print(\"Invalid credentials. Please try again.\")\n",
    "\n",
    "    print(\"Too many incorrect attempts. Login failed.\")\n",
    "    return None  \n",
    "    \n",
    "voter_login()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a72ee692-1809-4f0e-881c-d716d589630e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "welcome voter, please select your preference \n",
      "1: see live campaign\n",
      "2: vote for campaign\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter preference 2\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'give_vote' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-7-644bb13f38a0>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     14\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 15\u001b[1;33m \u001b[0mvoter_portal\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     16\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-7-644bb13f38a0>\u001b[0m in \u001b[0;36mvoter_portal\u001b[1;34m()\u001b[0m\n\u001b[0;32m     10\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mlive_camp\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     11\u001b[0m     \u001b[1;32melif\u001b[0m \u001b[0mvoter_input\u001b[0m\u001b[1;33m==\u001b[0m\u001b[1;34m'2'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 12\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mgive_vote\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     13\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     14\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'give_vote' is not defined"
     ]
    }
   ],
   "source": [
    "#1.2.1 when voter login sucessfull then\n",
    "def voter_portal():\n",
    "    print('welcome voter, please select your preference ')\n",
    "    print('1: see live campaign')\n",
    "    print('2: vote for campaign')\n",
    "    \n",
    "    voter_input=input('enter preference')\n",
    "    \n",
    "    if voter_input=='1':\n",
    "        return live_camp()\n",
    "    elif voter_input=='2':  \n",
    "        return give_vote()       \n",
    "    \n",
    "        \n",
    "voter_portal() \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4405c71b-0c85-46bb-a5a4-3586bc4994cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Campaign Heading</th>\n",
       "      <th>Campaign Name</th>\n",
       "      <th>Start Date</th>\n",
       "      <th>End Date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Hum sath</td>\n",
       "      <td>For us</td>\n",
       "      <td>2022-03-01 12:02:03</td>\n",
       "      <td>2025-1-1 12:2:2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Campaign Heading Campaign Name          Start Date         End Date\n",
       "1         Hum sath        For us 2022-03-01 12:02:03  2025-1-1 12:2:2"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#1.2.1.1\n",
    "\n",
    "\n",
    "import datetime \n",
    "from datetime import datetime\n",
    "x=datetime.now()\n",
    "formatted_current_date = x.strftime('%Y-%m-%d %H:%M:%S')\n",
    "#formatted_current_date = x.strftime('%Y-%m-%d')\n",
    "#formatted_current_datetime = x.strftime('%Y-%m-%d %H:%M:%S')\n",
    "\n",
    "def live_camp():\n",
    "    #campaign_data_file=pd.read_excel(r'C:\\Users\\shivani\\Python\\voting system\\Campaign_data.xlsx' )\n",
    "    #count_data=campaign_data_file\n",
    "    #return count_data'''\n",
    "    \n",
    "    #lest see all live campaigns for vote \n",
    "    campaign_data_file=pd.read_excel(r'C:\\Users\\shivani\\Python\\voting system\\Campaign_data.xlsx' )\n",
    "    count_data=campaign_data_file\n",
    "    x= count_data\n",
    "    # return count_data\n",
    "    return x[x['End Date']>formatted_current_date]\n",
    "\n",
    "\n",
    "live_camp()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e28f2a43-e985-4e0f-8e25-b994fcc4bd77",
   "metadata": {},
   "outputs": [],
   "source": [
    "#our result are here\n",
    "#'C:\\Users\\shivani\\Python\\voting system\\Votes_Vote_data.xlsx"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "a9040a0e-de85-4df3-bc35-7f168ab8a1fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hey! Voter, Are you ready to decide whose gonna rule the world??\n",
      "  party_name  Campaign Name\n",
      "0        CNG  shivani nagar\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your name Shivani\n",
      "enter your id 123\n",
      "enter to which party you want to succeed  CNG\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You Sucessfully Voted\n"
     ]
    }
   ],
   "source": [
    "#1.2.1.2\n",
    "\n",
    "#df\n",
    "#vf\n",
    "excel_file=r'C:\\Users\\shivani\\Python\\voting system\\Votes_Vote_data.xlsx'\n",
    "\n",
    "def give_vote():\n",
    "    print(\"Hey! Voter, Are you ready to decide whose gonna rule the world??\")\n",
    "    print(show_candidate_parties())\n",
    "    \n",
    "    voter_name= input(\"enter your name\")   \n",
    "    voter_id= int(input(\"enter your id\")) \n",
    "    vote_for=input('enter to which party you want to succeed ')    \n",
    "           \n",
    "    excel_file=r'C:\\Users\\shivani\\Python\\voting system\\Votes_Vote_data.xlsx' \n",
    "    enter_data= {r'voter_name':[voter_name],'voter_id':[voter_id] ,'vote_for':[vote_for]}\n",
    "    entry_df= pd.DataFrame(enter_data)\n",
    "    \n",
    "    try:\n",
    "        exist_data= pd.read_excel(excel_file)\n",
    "        update_data=exist_data.append(entry_df,ignore_index=True)\n",
    "        update_data.to_excel(excel_file, index= False)\n",
    "        print('You Sucessfully Voted')\n",
    "    except:\n",
    "        entry_df.to_excel(excel_file, index= False)\n",
    "        print('file not created , create new one')\n",
    "        \n",
    "        \n",
    "#add count for counting votes \n",
    "\n",
    "give_vote()    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5dde0094-1d50-4962-9884-11a7b3310340",
   "metadata": {},
   "outputs": [],
   "source": [
    "#piblish result after calculating all votes from candidate\n",
    "\n",
    "import matplotlib \n",
    "from matplotlib import pyplot as plt\n",
    "res=pd.read_excel(r'C:\\Users\\shivani\\Python\\voting system\\Campaign_data.xlsx') \n",
    "res"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f9f62313-b5ff-4952-9e26-de4ab2bcfb32",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>party_name</th>\n",
       "      <th>Campaign Name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>CNG</td>\n",
       "      <td>shivani nagar</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  party_name  Campaign Name\n",
       "0        CNG  shivani nagar"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def show_candidate_parties():\n",
    "           \n",
    "    all_candidate_file=pd.read_excel(r'C:\\Users\\shivani\\Python\\voting system\\Candidate_data.xlsx')\n",
    "    af=pd.DataFrame(all_candidate_file)\n",
    "    return af[['party_name','Campaign Name']]\n",
    "    \n",
    "show_candidate_parties()    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "6d461c5c-8f17-45d8-8ed9-e077142c4bbd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Campaign Heading</th>\n",
       "      <th>Campaign Name</th>\n",
       "      <th>Start Date</th>\n",
       "      <th>End Date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Hum sath</td>\n",
       "      <td>For us</td>\n",
       "      <td>2022-03-01 12:02:03</td>\n",
       "      <td>2025-1-1 12:2:2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Campaign Heading Campaign Name          Start Date         End Date\n",
       "1         Hum sath        For us 2022-03-01 12:02:03  2025-1-1 12:2:2"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "campaign_data_file=pd.read_excel(r'C:\\Users\\shivani\\Python\\voting system\\Campaign_data.xlsx' )\n",
    "count_data=campaign_data_file\n",
    "x= count_data\n",
    "x[x['End Date']>formatted_current_date]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "5d3e1ad4-d135-4b05-8423-b6b5730bbbc9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Who you are, a user or an admin?  admin\n",
      "Enter name:  Alex\n",
      "Enter password:  098\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Invalid credentials. Please try again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter name:  Shivani\n",
      "Enter password:  123\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Login successful!\n",
      "select from the below actions\n",
      "1: Start new campaign\n",
      "2: Old Result\n",
      "3: Add Candidate\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your action 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you want to Start new campaign\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter camp heading A\n",
      "campaign name B\n",
      "enter start date 2024-1-23 11:2:3\n",
      "start end_date_time 2024-4-12 11:2:3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Campaign Added Succesfully.\n"
     ]
    }
   ],
   "source": [
    "# 1.Portal main \n",
    "def reg():\n",
    "    x = input(\"Who you are, a user or an admin? \")\n",
    "    if x.lower() == 'admin':\n",
    "        return Admin_log()\n",
    "    elif x.lower()=='voter':\n",
    "        return voter_login()\n",
    "    else:\n",
    "        return None\n",
    "\n",
    "# Call the reg() function\n",
    "reg()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "c947f060-0ac6-4f97-b657-c5f27e19f630",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Select from the below actions\n",
      "1: Start new campaign\n",
      "2: Old Result\n",
      "3: Add Candidate\n",
      "4: View Votes Result\n",
      "5: Graphical Representation of result \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your action 5\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<BarContainer object of 3 artists>"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def Admin_portal():\n",
    "    print(\"Select from the below actions\")\n",
    "    print(\"1: Start new campaign\")\n",
    "    print(\"2: Old Result\")\n",
    "    print(\"3: Add Candidate\")\n",
    "    print(\"4: View Votes Result\")\n",
    "    print(\"5: Graphical Representation of result \")\n",
    "\n",
    "    admin_enter = int(input('Enter your action'))\n",
    "    if admin_enter == 1:\n",
    "        return start_cam()\n",
    "    elif admin_enter == 2:\n",
    "        return old_result()\n",
    "    elif admin_enter == 3:\n",
    "        return add_candidate()\n",
    "    elif admin_enter == 4:\n",
    "        return view_votes_result()\n",
    "    elif admin_enter == 5:\n",
    "        return graph_rep()\n",
    "\n",
    "# Function to view votes result (visible only to Admin)\n",
    "def view_votes_result():\n",
    "    votes_result = calculate_votes()\n",
    "    print(\"Votes Result:\")\n",
    "    print(votes_result)\n",
    "\n",
    "# Call Admin Portal\n",
    "Admin_portal()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "8ecc8142-5531-4b23-8760-b135efc9b7c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you want to Start new campaign\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-16-1e35f974aa20>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     28\u001b[0m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'file not created , create new one'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     29\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 30\u001b[1;33m \u001b[0mstart_cam\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-16-1e35f974aa20>\u001b[0m in \u001b[0;36mstart_cam\u001b[1;34m()\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mstart_cam\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"you want to Start new campaign\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m     \u001b[0mcampaign_head\u001b[0m\u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'enter camp heading'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      7\u001b[0m     \u001b[0mc_name\u001b[0m\u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'campaign name'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m     \u001b[0mstart_date_time\u001b[0m\u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'enter start date'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[1;34m(self, prompt)\u001b[0m\n\u001b[0;32m    858\u001b[0m                 \u001b[1;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    859\u001b[0m             )\n\u001b[1;32m--> 860\u001b[1;33m         return self._input_request(str(prompt),\n\u001b[0m\u001b[0;32m    861\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    862\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[1;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[0;32m    902\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    903\u001b[0m                 \u001b[1;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 904\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Interrupted by user\"\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    905\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    906\u001b[0m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Invalid Message:\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "#2.1 start campaign \n",
    "import datetime \n",
    "from datetime import datetime\n",
    "def start_cam():\n",
    "    print(\"you want to Start new campaign\")\n",
    "    campaign_head= input('enter camp heading')\n",
    "    c_name= input('campaign name')\n",
    "    start_date_time= input('enter start date')\n",
    "    end_date_time=input('start end_date_time')\n",
    "    \n",
    "    try:\n",
    "        start_date_time= datetime.strptime(start_date_time,\"%Y-%m-%d %H:%M:%S\")\n",
    "    except ValueError:\n",
    "        print('invalid format')\n",
    "        return\n",
    "    \n",
    "    excel_file=r'C:\\Users\\shivani\\Python\\voting system\\Campaign_data.xlsx' \n",
    "    enter_data= {r'Campaign Heading':[campaign_head],'Campaign Name':[c_name] ,'Start Date':[start_date_time],'End Date':[end_date_time] }\n",
    "    entry_df= pd.DataFrame(enter_data)\n",
    "    \n",
    "    try:\n",
    "        exist_data= pd.read_excel(excel_file)\n",
    "        update_data=exist_data.append(entry_df,ignore_index=True)\n",
    "        update_data.to_excel(excel_file, index= False)\n",
    "        print('Campaign Added Succesfully.')\n",
    "    except:\n",
    "        entry_df.to_excel(excel_file, index= False)\n",
    "        print('file not created , create new one')\n",
    "        \n",
    "start_cam()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "82254fbc-f67b-4e59-99da-e396c3c6abcb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Campaign Heading    3\n",
       "Campaign Name       3\n",
       "Start Date          3\n",
       "End Date            3\n",
       "dtype: int64"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#2.2 see older campaign file  \n",
    "def old_result():\n",
    "    campaign_data_file=pd.read_excel(r'C:\\Users\\shivani\\Python\\voting system\\Campaign_data.xlsx' )\n",
    "    count_data=campaign_data_file.count()\n",
    "    return count_data\n",
    "    \n",
    "old_result()    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "737ce65f-3587-4715-a7d0-abe00621d014",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "93eb62ab-8aa4-4537-8cbf-74a631d6eb3a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You need to fill all the details for adding a candidate\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-18-40948e91a4de>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     22\u001b[0m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'file not created , create new one'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     23\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 24\u001b[1;33m \u001b[0madd_candidate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     25\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-18-40948e91a4de>\u001b[0m in \u001b[0;36madd_candidate\u001b[1;34m()\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0madd_candidate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'You need to fill all the details for adding a candidate'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m     \u001b[0mcandidate_id\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'enter candidate id'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m     \u001b[0mcandidate_name\u001b[0m\u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'enter candidate name'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m     \u001b[0mcandidate_age\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'age'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[1;34m(self, prompt)\u001b[0m\n\u001b[0;32m    858\u001b[0m                 \u001b[1;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    859\u001b[0m             )\n\u001b[1;32m--> 860\u001b[1;33m         return self._input_request(str(prompt),\n\u001b[0m\u001b[0;32m    861\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    862\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[1;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[0;32m    902\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    903\u001b[0m                 \u001b[1;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 904\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Interrupted by user\"\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    905\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    906\u001b[0m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Invalid Message:\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "#2.3 add candidate\n",
    "\n",
    "def add_candidate():\n",
    "    print('You need to fill all the details for adding a candidate')\n",
    "    candidate_id = int(input('enter candidate id'))\n",
    "    candidate_name= input('enter candidate name')\n",
    "    candidate_age=int(input('age'))\n",
    "    party_name= input('enterparty name of candidate')\n",
    "    campaign_involve=input('enter in which campaign candidate stood')\n",
    "    \n",
    "    excel_file=r'C:\\Users\\shivani\\Python\\voting system\\Candidate_data.xlsx' \n",
    "    enter_data= {r'candidate_id':[candidate_id],'Campaign Name':[candidate_name] ,'candidate_age':[candidate_age],'party_name':[party_name],'campaign_involve':[campaign_involve] }\n",
    "    entry_df= pd.DataFrame(enter_data)\n",
    "    \n",
    "    try:\n",
    "        exist_data= pd.read_excel(excel_file)\n",
    "        update_data=exist_data.append(entry_df,ignore_index=True)\n",
    "        update_data.to_excel(excel_file, index= False)\n",
    "        print('Candidate Added Succesfully.')\n",
    "    except:\n",
    "        entry_df.to_excel(excel_file, index= False)\n",
    "        print('file not created , create new one')\n",
    "        \n",
    "add_candidate()\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "64308dc4-fbd5-4eb0-84bc-a1b5030a6bca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>vote_for</th>\n",
       "      <th>votes_count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>BJP</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>CNG</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>bjp</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  vote_for  votes_count\n",
       "0      BJP            2\n",
       "1      CNG            1\n",
       "2      bjp            2"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Function to calculate votes grouped by candidates noly seen by Admin\n",
    "votes_df = pd.read_excel(r'C:\\Users\\shivani\\Python\\voting system\\Votes_Vote_data.xlsx')\n",
    "\n",
    "def calculate_votes():\n",
    "    votes_result = votes_df.groupby('vote_for').size().reset_index(name='votes_count')\n",
    "    return votes_result\n",
    "calculate_votes()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "602bc079-cc6c-41bc-9c8f-c2a01e7f8778",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<BarContainer object of 3 artists>"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#graphical reprenstaion \n",
    "import matplotlib \n",
    "from matplotlib import pyplot as plt\n",
    "def graph_rep():\n",
    "    x=votes_result['vote_for']\n",
    "    y=votes_result['votes_count']\n",
    "    z= plt.bar(x,y)\n",
    "    return z\n",
    "graph_rep()    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d65e8bbd-a385-4b68-950c-de7bc2fce61a",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bbe0a6b4-973b-4307-a59b-0d82ece0a977",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "6932c854-8308-42e2-b446-02f22b2db2b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: nbconvert in c:\\users\\shivani\\anaconda3\\lib\\site-packages (6.0.7)\n",
      "Requirement already satisfied: pandocfilters>=1.4.1 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbconvert) (1.4.3)\n",
      "Requirement already satisfied: jupyterlab-pygments in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbconvert) (0.1.2)\n",
      "Requirement already satisfied: jupyter-core in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbconvert) (4.7.1)\n",
      "Requirement already satisfied: mistune<2,>=0.8.1 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbconvert) (0.8.4)\n",
      "Requirement already satisfied: testpath in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbconvert) (0.4.4)\n",
      "Requirement already satisfied: entrypoints>=0.2.2 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbconvert) (0.3)\n",
      "Requirement already satisfied: nbclient<0.6.0,>=0.5.0 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbconvert) (0.5.3)\n",
      "Requirement already satisfied: traitlets>=4.2 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbconvert) (5.0.5)\n",
      "Requirement already satisfied: pygments>=2.4.1 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbconvert) (2.8.1)\n",
      "Requirement already satisfied: bleach in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbconvert) (3.3.0)\n",
      "Requirement already satisfied: nbformat>=4.4 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbconvert) (5.1.3)\n",
      "Requirement already satisfied: jinja2>=2.4 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbconvert) (2.11.3)\n",
      "Requirement already satisfied: defusedxml in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbconvert) (0.7.1)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from jinja2>=2.4->nbconvert) (1.1.1)\n",
      "Requirement already satisfied: jupyter-client>=6.1.5 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbclient<0.6.0,>=0.5.0->nbconvert) (6.1.12)\n",
      "Requirement already satisfied: async-generator in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbclient<0.6.0,>=0.5.0->nbconvert) (1.10)\n",
      "Requirement already satisfied: nest-asyncio in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbclient<0.6.0,>=0.5.0->nbconvert) (1.5.1)\n",
      "Requirement already satisfied: python-dateutil>=2.1 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from jupyter-client>=6.1.5->nbclient<0.6.0,>=0.5.0->nbconvert) (2.8.1)\n",
      "Requirement already satisfied: tornado>=4.1 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from jupyter-client>=6.1.5->nbclient<0.6.0,>=0.5.0->nbconvert) (6.1)\n",
      "Requirement already satisfied: pyzmq>=13 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from jupyter-client>=6.1.5->nbclient<0.6.0,>=0.5.0->nbconvert) (20.0.0)\n",
      "Requirement already satisfied: pywin32>=1.0 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from jupyter-core->nbconvert) (227)\n",
      "Requirement already satisfied: ipython-genutils in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbformat>=4.4->nbconvert) (0.2.0)\n",
      "Requirement already satisfied: jsonschema!=2.5.0,>=2.4 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from nbformat>=4.4->nbconvert) (3.2.0)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.4->nbconvert) (20.3.0)\n",
      "Requirement already satisfied: six>=1.11.0 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.4->nbconvert) (1.15.0)\n",
      "Requirement already satisfied: pyrsistent>=0.14.0 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.4->nbconvert) (0.17.3)\n",
      "Requirement already satisfied: setuptools in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.4->nbconvert) (52.0.0.post20210125)\n",
      "Requirement already satisfied: packaging in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from bleach->nbconvert) (20.9)\n",
      "Requirement already satisfied: webencodings in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from bleach->nbconvert) (0.5.1)\n",
      "Requirement already satisfied: pyparsing>=2.0.2 in c:\\users\\shivani\\anaconda3\\lib\\site-packages (from packaging->bleach->nbconvert) (2.4.7)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install nbconvert"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "cd361b2c-ed76-4909-b3d2-b8cdeb90fb5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import nbconvert"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "1a129b03-f69c-40a7-9a16-e70845fab450",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-39-0007cd3a1617>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-39-0007cd3a1617>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    jupyter nbconvert --to Voting_System.py Voting_System.ipynb\u001b[0m\n\u001b[1;37m            ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "jupyter nbconvert --to Voting_System.py Voting_System.ipynb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "e856ddae-59be-403b-aba6-eea8d85befa3",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-42-4ff870a32099>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-42-4ff870a32099>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    jupyter nbconvert --to script Voting_System.ipynb\u001b[0m\n\u001b[1;37m            ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "jupyter nbconvert --to script Voting_System.ipynb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4511d23-998b-4999-bb62-3d5bb4031bc7",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
