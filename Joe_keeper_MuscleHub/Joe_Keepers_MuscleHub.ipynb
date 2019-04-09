{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Capstone Project 1: MuscleHub AB Test"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1: Get started with SQL"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Like most businesses, Janet keeps her data in a SQL database.  Normally, you'd download the data from her database to a csv file, and then load it into a Jupyter Notebook using Pandas.\n",
    "\n",
    "For this project, you'll have to access SQL in a slightly different way.  You'll be using a special Codecademy library that lets you type SQL queries directly into this Jupyter notebook.  You'll have pass each SQL query as an argument to a function called `sql_query`.  Each query will return a Pandas DataFrame.  Here's an example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "metadata": {},
   "outputs": [],
   "source": [
    "# This import only needs to happen once, at the beginning of the notebook\n",
    "from codecademySQL import sql_query"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
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
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>visit_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Karen</td>\n",
       "      <td>Manning</td>\n",
       "      <td>Karen.Manning@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Annette</td>\n",
       "      <td>Boone</td>\n",
       "      <td>AB9982@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Salvador</td>\n",
       "      <td>Merritt</td>\n",
       "      <td>SalvadorMerritt12@outlook.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Martha</td>\n",
       "      <td>Maxwell</td>\n",
       "      <td>Martha.Maxwell@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Andre</td>\n",
       "      <td>Mayer</td>\n",
       "      <td>AndreMayer90@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                          email  gender  \\\n",
       "0      0      Karen   Manning        Karen.Manning@gmail.com  female   \n",
       "1      1    Annette     Boone               AB9982@gmail.com  female   \n",
       "2      2   Salvador   Merritt  SalvadorMerritt12@outlook.com    male   \n",
       "3      3     Martha   Maxwell       Martha.Maxwell@gmail.com  female   \n",
       "4      4      Andre     Mayer         AndreMayer90@gmail.com    male   \n",
       "\n",
       "  visit_date  \n",
       "0     5-1-17  \n",
       "1     5-1-17  \n",
       "2     5-1-17  \n",
       "3     5-1-17  \n",
       "4     5-1-17  "
      ]
     },
     "execution_count": 191,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Here's an example of a query that just displays some data\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM visits\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Here's an example where we save the data to a DataFrame\n",
    "df = sql_query('''\n",
    "SELECT *\n",
    "FROM applications\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2: Get your dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's get started!\n",
    "\n",
    "Janet of MuscleHub has a SQLite database, which contains several tables that will be helpful to you in this investigation:\n",
    "- `visits` contains information about potential gym customers who have visited MuscleHub\n",
    "- `fitness_tests` contains information about potential customers in \"Group A\", who were given a fitness test\n",
    "- `applications` contains information about any potential customers (both \"Group A\" and \"Group B\") who filled out an application.  Not everyone in `visits` will have filled out an application.\n",
    "- `purchases` contains information about customers who purchased a membership to MuscleHub.\n",
    "\n",
    "Use the space below to examine each table."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
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
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>visit_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Karen</td>\n",
       "      <td>Manning</td>\n",
       "      <td>Karen.Manning@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Annette</td>\n",
       "      <td>Boone</td>\n",
       "      <td>AB9982@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Salvador</td>\n",
       "      <td>Merritt</td>\n",
       "      <td>SalvadorMerritt12@outlook.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Martha</td>\n",
       "      <td>Maxwell</td>\n",
       "      <td>Martha.Maxwell@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Andre</td>\n",
       "      <td>Mayer</td>\n",
       "      <td>AndreMayer90@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                          email  gender  \\\n",
       "0      0      Karen   Manning        Karen.Manning@gmail.com  female   \n",
       "1      1    Annette     Boone               AB9982@gmail.com  female   \n",
       "2      2   Salvador   Merritt  SalvadorMerritt12@outlook.com    male   \n",
       "3      3     Martha   Maxwell       Martha.Maxwell@gmail.com  female   \n",
       "4      4      Andre     Mayer         AndreMayer90@gmail.com    male   \n",
       "\n",
       "  visit_date  \n",
       "0     5-1-17  \n",
       "1     5-1-17  \n",
       "2     5-1-17  \n",
       "3     5-1-17  \n",
       "4     5-1-17  "
      ]
     },
     "execution_count": 193,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Examine visits here\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM visits\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
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
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>fitness_test_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Kim</td>\n",
       "      <td>Walter</td>\n",
       "      <td>KimWalter58@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-07-03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Tom</td>\n",
       "      <td>Webster</td>\n",
       "      <td>TW3857@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Marcus</td>\n",
       "      <td>Bauer</td>\n",
       "      <td>Marcus.Bauer@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Roberta</td>\n",
       "      <td>Best</td>\n",
       "      <td>RB6305@hotmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-07-02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Carrie</td>\n",
       "      <td>Francis</td>\n",
       "      <td>CF1896@hotmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-07-05</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                   email  gender  \\\n",
       "0      0        Kim    Walter   KimWalter58@gmail.com  female   \n",
       "1      1        Tom   Webster        TW3857@gmail.com    male   \n",
       "2      2     Marcus     Bauer  Marcus.Bauer@gmail.com    male   \n",
       "3      3    Roberta      Best      RB6305@hotmail.com  female   \n",
       "4      4     Carrie   Francis      CF1896@hotmail.com  female   \n",
       "\n",
       "  fitness_test_date  \n",
       "0        2017-07-03  \n",
       "1        2017-07-02  \n",
       "2        2017-07-01  \n",
       "3        2017-07-02  \n",
       "4        2017-07-05  "
      ]
     },
     "execution_count": 194,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Examine fitness_tests here\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM fitness_tests\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
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
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>application_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Roy</td>\n",
       "      <td>Abbott</td>\n",
       "      <td>RoyAbbott32@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-08-12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Agnes</td>\n",
       "      <td>Acevedo</td>\n",
       "      <td>AgnesAcevedo1@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-09-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Roberta</td>\n",
       "      <td>Acevedo</td>\n",
       "      <td>RA8063@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-09-15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Darren</td>\n",
       "      <td>Acosta</td>\n",
       "      <td>DAcosta1996@hotmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Vernon</td>\n",
       "      <td>Acosta</td>\n",
       "      <td>VAcosta1975@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-14</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                    email  gender  \\\n",
       "0      0        Roy    Abbott    RoyAbbott32@gmail.com    male   \n",
       "1      1      Agnes   Acevedo  AgnesAcevedo1@gmail.com  female   \n",
       "2      2    Roberta   Acevedo         RA8063@gmail.com  female   \n",
       "3      3     Darren    Acosta  DAcosta1996@hotmail.com    male   \n",
       "4      4     Vernon    Acosta    VAcosta1975@gmail.com    male   \n",
       "\n",
       "  application_date  \n",
       "0       2017-08-12  \n",
       "1       2017-09-29  \n",
       "2       2017-09-15  \n",
       "3       2017-07-26  \n",
       "4       2017-07-14  "
      ]
     },
     "execution_count": 195,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Examine applications here\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM applications\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
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
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>purchase_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Roy</td>\n",
       "      <td>Abbott</td>\n",
       "      <td>RoyAbbott32@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-08-18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Roberta</td>\n",
       "      <td>Acevedo</td>\n",
       "      <td>RA8063@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-09-16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Vernon</td>\n",
       "      <td>Acosta</td>\n",
       "      <td>VAcosta1975@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Darren</td>\n",
       "      <td>Acosta</td>\n",
       "      <td>DAcosta1996@hotmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Dawn</td>\n",
       "      <td>Adkins</td>\n",
       "      <td>Dawn.Adkins@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-08-24</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                    email  gender purchase_date\n",
       "0      0        Roy    Abbott    RoyAbbott32@gmail.com    male    2017-08-18\n",
       "1      1    Roberta   Acevedo         RA8063@gmail.com  female    2017-09-16\n",
       "2      2     Vernon    Acosta    VAcosta1975@gmail.com    male    2017-07-20\n",
       "3      3     Darren    Acosta  DAcosta1996@hotmail.com    male    2017-07-27\n",
       "4      4       Dawn    Adkins    Dawn.Adkins@gmail.com  female    2017-08-24"
      ]
     },
     "execution_count": 196,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Examine purchases here\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM purchases\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# We'd like to download a giant DataFrame containing all of this data.  You'll need to write a query that does the following things:\n",
    "\n",
    "1. Not all visits in  `visits` occurred during the A/B test.  You'll only want to pull data where `visit_date` is on or after `7-1-17`.\n",
    "\n",
    "2. You'll want to perform a series of `LEFT JOIN` commands to combine the four tables that we care about.  You'll need to perform the joins on `first_name`, `last_name`, and `email`.  Pull the following columns:\n",
    "\n",
    "\n",
    "- `visits.first_name`\n",
    "- `visits.last_name`\n",
    "- `visits.gender`\n",
    "- `visits.email`\n",
    "- `visits.visit_date`\n",
    "- `fitness_tests.fitness_test_date`\n",
    "- `applications.application_date`\n",
    "- `purchases.purchase_date`\n",
    "\n",
    "Save the result of this query to a variable called `df`.\n",
    "\n",
    "Hint: your result should have 5004 rows.  Does it?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
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
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>gender</th>\n",
       "      <th>email</th>\n",
       "      <th>visit_date</th>\n",
       "      <th>fitness_test_date</th>\n",
       "      <th>application_date</th>\n",
       "      <th>purchase_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Kim</td>\n",
       "      <td>Walter</td>\n",
       "      <td>female</td>\n",
       "      <td>KimWalter58@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>2017-07-03</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Tom</td>\n",
       "      <td>Webster</td>\n",
       "      <td>male</td>\n",
       "      <td>TW3857@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>2017-07-02</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Edward</td>\n",
       "      <td>Bowen</td>\n",
       "      <td>male</td>\n",
       "      <td>Edward.Bowen@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>None</td>\n",
       "      <td>2017-07-04</td>\n",
       "      <td>2017-07-04</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Marcus</td>\n",
       "      <td>Bauer</td>\n",
       "      <td>male</td>\n",
       "      <td>Marcus.Bauer@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>2017-07-01</td>\n",
       "      <td>2017-07-03</td>\n",
       "      <td>2017-07-05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Roberta</td>\n",
       "      <td>Best</td>\n",
       "      <td>female</td>\n",
       "      <td>RB6305@hotmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>2017-07-02</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Joseph</td>\n",
       "      <td>Foley</td>\n",
       "      <td>male</td>\n",
       "      <td>JosephFoley81@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Carrie</td>\n",
       "      <td>Francis</td>\n",
       "      <td>female</td>\n",
       "      <td>CF1896@hotmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>2017-07-05</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Sharon</td>\n",
       "      <td>William</td>\n",
       "      <td>female</td>\n",
       "      <td>Sharon.William@outlook.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Teresa</td>\n",
       "      <td>Yates</td>\n",
       "      <td>female</td>\n",
       "      <td>TYates1988@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>2017-07-02</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Salvador</td>\n",
       "      <td>Cardenas</td>\n",
       "      <td>male</td>\n",
       "      <td>SCardenas1980@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>2017-07-07</td>\n",
       "      <td>2017-07-06</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Glen</td>\n",
       "      <td>Barker</td>\n",
       "      <td>male</td>\n",
       "      <td>GBarker1976@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Valerie</td>\n",
       "      <td>Munoz</td>\n",
       "      <td>female</td>\n",
       "      <td>VMunoz1998@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>2017-07-03</td>\n",
       "      <td>2017-07-05</td>\n",
       "      <td>2017-07-06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Jeremy</td>\n",
       "      <td>Howe</td>\n",
       "      <td>male</td>\n",
       "      <td>JHowe1982@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>2017-07-06</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Joel</td>\n",
       "      <td>Combs</td>\n",
       "      <td>male</td>\n",
       "      <td>JC9481@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>2017-07-01</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Oscar</td>\n",
       "      <td>Forbes</td>\n",
       "      <td>male</td>\n",
       "      <td>Oscar.Forbes@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>Darryl</td>\n",
       "      <td>Albert</td>\n",
       "      <td>male</td>\n",
       "      <td>DAlbert1975@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Armando</td>\n",
       "      <td>Valenzuela</td>\n",
       "      <td>male</td>\n",
       "      <td>ArmandoValenzuela67@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>June</td>\n",
       "      <td>Ayers</td>\n",
       "      <td>female</td>\n",
       "      <td>JA2612@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Nancy</td>\n",
       "      <td>Morin</td>\n",
       "      <td>female</td>\n",
       "      <td>Nancy.Morin@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>2017-07-05</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>Lorraine</td>\n",
       "      <td>Lindsay</td>\n",
       "      <td>female</td>\n",
       "      <td>LL3161@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>2017-07-05</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   first_name   last_name  gender                          email visit_date  \\\n",
       "0         Kim      Walter  female          KimWalter58@gmail.com     7-1-17   \n",
       "1         Tom     Webster    male               TW3857@gmail.com     7-1-17   \n",
       "2      Edward       Bowen    male         Edward.Bowen@gmail.com     7-1-17   \n",
       "3      Marcus       Bauer    male         Marcus.Bauer@gmail.com     7-1-17   \n",
       "4     Roberta        Best  female             RB6305@hotmail.com     7-1-17   \n",
       "5      Joseph       Foley    male        JosephFoley81@gmail.com     7-1-17   \n",
       "6      Carrie     Francis  female             CF1896@hotmail.com     7-1-17   \n",
       "7      Sharon     William  female     Sharon.William@outlook.com     7-1-17   \n",
       "8      Teresa       Yates  female           TYates1988@gmail.com     7-1-17   \n",
       "9    Salvador    Cardenas    male        SCardenas1980@gmail.com     7-1-17   \n",
       "10       Glen      Barker    male          GBarker1976@gmail.com     7-1-17   \n",
       "11    Valerie       Munoz  female           VMunoz1998@gmail.com     7-1-17   \n",
       "12     Jeremy        Howe    male            JHowe1982@gmail.com     7-1-17   \n",
       "13       Joel       Combs    male               JC9481@gmail.com     7-1-17   \n",
       "14      Oscar      Forbes    male         Oscar.Forbes@gmail.com     7-1-17   \n",
       "15     Darryl      Albert    male          DAlbert1975@gmail.com     7-1-17   \n",
       "16    Armando  Valenzuela    male  ArmandoValenzuela67@gmail.com     7-1-17   \n",
       "17       June       Ayers  female               JA2612@gmail.com     7-1-17   \n",
       "18      Nancy       Morin  female          Nancy.Morin@gmail.com     7-1-17   \n",
       "19   Lorraine     Lindsay  female               LL3161@gmail.com     7-1-17   \n",
       "\n",
       "   fitness_test_date application_date purchase_date  \n",
       "0         2017-07-03             None          None  \n",
       "1         2017-07-02             None          None  \n",
       "2               None       2017-07-04    2017-07-04  \n",
       "3         2017-07-01       2017-07-03    2017-07-05  \n",
       "4         2017-07-02             None          None  \n",
       "5               None             None          None  \n",
       "6         2017-07-05             None          None  \n",
       "7               None             None          None  \n",
       "8         2017-07-02             None          None  \n",
       "9         2017-07-07       2017-07-06          None  \n",
       "10              None             None          None  \n",
       "11        2017-07-03       2017-07-05    2017-07-06  \n",
       "12        2017-07-06             None          None  \n",
       "13        2017-07-01             None          None  \n",
       "14              None             None          None  \n",
       "15              None             None          None  \n",
       "16              None             None          None  \n",
       "17              None             None          None  \n",
       "18        2017-07-05             None          None  \n",
       "19        2017-07-05             None          None  "
      ]
     },
     "execution_count": 197,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = sql_query('''\n",
    "SELECT visits.first_name, visits.last_name,visits.gender,visits.email,visits.visit_date,\n",
    "   fitness_tests.fitness_test_date,\n",
    "   applications.application_date,\n",
    "   purchases.purchase_date\n",
    "FROM visits \n",
    "    left join fitness_tests on \n",
    "        visits.first_name = fitness_tests.first_name and \n",
    "        visits.last_name = fitness_tests.last_name and \n",
    "        visits.email = fitness_tests.email\n",
    "    left join applications on\n",
    "        visits.first_name = applications.first_name and \n",
    "        visits.last_name = applications.last_name and \n",
    "        visits.email = applications.email\n",
    "    left join purchases on\n",
    "        visits.first_name = purchases.first_name and \n",
    "        visits.last_name = purchases.last_name and \n",
    "        visits.email = purchases.email\n",
    "where visits.visit_date >= '7-1-17'  \n",
    "''')\n",
    "df.head(20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3: Investigate the A and B groups"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We have some data to work with! Import the following modules so that we can start doing analysis:\n",
    "- `import pandas as pd`\n",
    "- `from matplotlib import pyplot as plt`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from matplotlib import pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We're going to add some columns to `df` to help us with our analysis.\n",
    "\n",
    "Start by adding a column called `ab_test_group`.  It should be `A` if `fitness_test_date` is not `None`, and `B` if `fitness_test_date` is `None`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 199,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['ab_test_group']= df.fitness_test_date.apply(lambda date: 'A' if date is not None else 'B')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's do a quick sanity check that Janet split her visitors such that about half are in A and half are in B.\n",
    "\n",
    "Start by using `groupby` to count how many users are in each `ab_test_group`.  Save the results to `ab_counts`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 200,
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
       "      <th>ab_test_group</th>\n",
       "      <th>first_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>2504</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>2500</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  ab_test_group  first_name\n",
       "0             A        2504\n",
       "1             B        2500"
      ]
     },
     "execution_count": 200,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ab_counts= df.groupby('ab_test_group').first_name.count().reset_index()\n",
    "ab_counts"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We'll want to include this information in our presentation.  Let's create a pie cart using `plt.pie`.  Make sure to include:\n",
    "- Use `plt.axis('equal')` so that your pie chart looks nice\n",
    "- Add a legend labeling `A` and `B`\n",
    "- Use `autopct` to label the percentage of each group\n",
    "- Save your figure as `ab_test_pie_chart.png`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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siILrVkn5n299ORtfe4ZwZIVWZXexn1PvECLq/rQsecgOvYcxN8nTDEBdOvWrfWhQ4fMhw4dMmdmZio5Xt9sNqfbbLaU1q1bp7Zt2zbF4XA09ng8533Mpk2bot577736NRTxLDJl4RspZGH4oLt/t/fQkgveJTYmmjULjXWLv1qygucy32bprIlVeppLmjbm5XEf0rdXt4sIaXhj1BMM6HOD8Y050g2wdOnSrWAU3IcfftjIbrcfvOgnuEjR0dHejRs35gDs3r074o477mjpcrnMb7311p7fesyWLVuip02bVv/hhx8+UnNJT5ERsm8KVQcQAiAvv5B6ljpVflyHlDZY6tRi4Xffn/WzxctWcXmvwbS7/k7uf8pBSUnphTeomT0AzZo1a7d3796Ip59++pKdO3dG22y2lOHDh18yf/782p07d2570003tWzRokVqv379Wpw4NXnZsmVxV155ZdvU1NTka665ps2OHTsiwVhWs1WrVqlJSUkpffr0aQngdDpr2Wy2FJvNlpKcnJxy9OjR83ZZs2bN3BMnTsz96KOPGnm9XjZt2hSVnp7eNiUlJTklJSV54cKF8QAjR45slpWVVctms6X87W9/a+R2uxk+fPglaWlpyUlJSSlvvPFGQtX+hatGRsi+qfylFITws+PFJXTsOYjiklL2HjjEN9Pfu6jtjHr8QUa9Pp6ev7/q5G3FxSXc96SDxdPeI6lVc+4Z8Vfe/XgGTwy766zH/9/ovzP6H8bIfNI/3/B0bJR88mdjx47d1adPn9gTI9X58+fX3rBhQ+yaNWt+tVqtZenp6baFCxfW6t69e+GIESMuczqdWxMTE90TJkyo98wzzzSbMWNG7rhx45rs2LFjfWxsrH7o0CFz+XabjBs3bkevXr0KXS6XKS4u7oJHvKSkpJR6vV52794dkZiY6F62bNnmuLg4ff369dGDBw9umZ2dveHll1/ePXbs2MbffvvtVoAxY8YkWCwWT3Z29objx49rV155pa1v3755NputEr+dqk4K2Te/+aePENXt9CmLlVlruefx58n+ZkaVr/V3bRfjwunLVq0+edumbTtocVkiSa2aA3DvHX345+Tp5yzkClMWsfVKzrrDGdq1a1fYqlWrMoDU1NSibdu2RdWvX9+9ZcuW2Ouuuy4JjAWFGjZsWAbQtm3b47fddluLfv36HbvrrruO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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig=plt.figure()\n",
    "plt.pie(ab_counts.first_name, labels=['A','B'], autopct='%1.2f%%')\n",
    "plt.axis('equal')\n",
    "plt.legend(labels=['A - Fitness Date Set','B - No Fitness Date'], loc='center right')\n",
    "plt.show()\n",
    "fig.savefig('ab_test_pie_chart.png')\n",
    "plt.close('all')\n",
    "\n",
    "\n",
    "                                               \n",
    "                                                  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Who picks up an application?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Recall that the sign-up process for MuscleHub has several steps:\n",
    "1. Take a fitness test with a personal trainer (only Group A)\n",
    "2. Fill out an application for the gym\n",
    "3. Send in their payment for their first month's membership\n",
    "\n",
    "Let's examine how many people make it to Step 2, filling out an application.\n",
    "\n",
    "Start by creating a new column in `df` called `is_application` which is `Application` if `application_date` is not `None` and `No Application`, otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['is_application'] = df.application_date.apply(lambda date: 'Application' if date is not None else 'No Application')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, using `groupby`, count how many people from Group A and Group B either do or don't pick up an application.  You'll want to group by `ab_test_group` and `is_application`.  Save this new DataFrame as `app_counts`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 203,
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
       "      <th>ab_test_group</th>\n",
       "      <th>is_application</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>gender</th>\n",
       "      <th>email</th>\n",
       "      <th>visit_date</th>\n",
       "      <th>fitness_test_date</th>\n",
       "      <th>application_date</th>\n",
       "      <th>purchase_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>Application</td>\n",
       "      <td>250</td>\n",
       "      <td>250</td>\n",
       "      <td>250</td>\n",
       "      <td>250</td>\n",
       "      <td>250</td>\n",
       "      <td>250</td>\n",
       "      <td>250</td>\n",
       "      <td>200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>A</td>\n",
       "      <td>No Application</td>\n",
       "      <td>2254</td>\n",
       "      <td>2254</td>\n",
       "      <td>2254</td>\n",
       "      <td>2254</td>\n",
       "      <td>2254</td>\n",
       "      <td>2254</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>B</td>\n",
       "      <td>Application</td>\n",
       "      <td>325</td>\n",
       "      <td>325</td>\n",
       "      <td>325</td>\n",
       "      <td>325</td>\n",
       "      <td>325</td>\n",
       "      <td>0</td>\n",
       "      <td>325</td>\n",
       "      <td>250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>B</td>\n",
       "      <td>No Application</td>\n",
       "      <td>2175</td>\n",
       "      <td>2175</td>\n",
       "      <td>2175</td>\n",
       "      <td>2175</td>\n",
       "      <td>2175</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  ab_test_group  is_application  first_name  last_name  gender  email  \\\n",
       "0             A     Application         250        250     250    250   \n",
       "1             A  No Application        2254       2254    2254   2254   \n",
       "2             B     Application         325        325     325    325   \n",
       "3             B  No Application        2175       2175    2175   2175   \n",
       "\n",
       "   visit_date  fitness_test_date  application_date  purchase_date  \n",
       "0         250                250               250            200  \n",
       "1        2254               2254                 0              0  \n",
       "2         325                  0               325            250  \n",
       "3        2175                  0                 0              0  "
      ]
     },
     "execution_count": 203,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "app_counts = df.groupby(['ab_test_group','is_application']).count().reset_index()\n",
    "app_counts"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We're going to want to calculate the percent of people in each group who complete an application.  It's going to be much easier to do this if we pivot `app_counts` such that:\n",
    "- The `index` is `ab_test_group`\n",
    "- The `columns` are `is_application`\n",
    "Perform this pivot and save it to the variable `app_pivot`.  Remember to call `reset_index()` at the end of the pivot!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
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
       "      <th>is_application</th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>Application</th>\n",
       "      <th>No Application</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>250</td>\n",
       "      <td>2254</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>325</td>\n",
       "      <td>2175</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "is_application ab_test_group  Application  No Application\n",
       "0                          A          250            2254\n",
       "1                          B          325            2175"
      ]
     },
     "execution_count": 204,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "app_pivot=app_counts.pivot(columns = 'is_application', index = 'ab_test_group', values= 'first_name').reset_index()\n",
    "app_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Define a new column called `Total`, which is the sum of `Application` and `No Application`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
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
       "      <th>is_application</th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>Application</th>\n",
       "      <th>No Application</th>\n",
       "      <th>Total</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>250</td>\n",
       "      <td>2254</td>\n",
       "      <td>2504</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>325</td>\n",
       "      <td>2175</td>\n",
       "      <td>2500</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "is_application ab_test_group  Application  No Application  Total\n",
       "0                          A          250            2254   2504\n",
       "1                          B          325            2175   2500"
      ]
     },
     "execution_count": 205,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "app_pivot['Total']=app_pivot['Application'] + app_pivot['No Application']\n",
    "app_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Calculate another column called `Percent with Application`, which is equal to `Application` divided by `Total`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
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
       "      <th>is_application</th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>Application</th>\n",
       "      <th>No Application</th>\n",
       "      <th>Total</th>\n",
       "      <th>Percent_with_Application</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>250</td>\n",
       "      <td>2254</td>\n",
       "      <td>2504</td>\n",
       "      <td>9.984026</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>325</td>\n",
       "      <td>2175</td>\n",
       "      <td>2500</td>\n",
       "      <td>13.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "is_application ab_test_group  Application  No Application  Total  \\\n",
       "0                          A          250            2254   2504   \n",
       "1                          B          325            2175   2500   \n",
       "\n",
       "is_application  Percent_with_Application  \n",
       "0                               9.984026  \n",
       "1                              13.000000  "
      ]
     },
     "execution_count": 206,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "app_pivot['Percent_with_Application'] = app_pivot['Application'] *100 / app_pivot['Total']\n",
    "app_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like more people from Group B turned in an application.  Why might that be?\n",
    "\n",
    "We need to know if this difference is statistically significant.\n",
    "\n",
    "Choose a hypothesis tests, import it from `scipy` and perform it.  Be sure to note the p-value.\n",
    "Is this result significant?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.0009647827600722304"
      ]
     },
     "execution_count": 207,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "from scipy.stats import chi2_contingency\n",
    "x=[[250, 2254],[325, 2175]]\n",
    "a,pval,b,c = chi2_contingency(x)\n",
    "pval"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Who purchases a membership?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Of those who picked up an application, how many purchased a membership?\n",
    "\n",
    "Let's begin by adding a column to `df` called `is_member` which is `Member` if `purchase_date` is not `None`, and `Not Member` otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['is_member'] = df.purchase_date.apply([lambda x: 'Member' if x is not None else 'Not Member'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, let's create a DataFrame called `just_apps` the contains only people who picked up an application."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 209,
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
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>gender</th>\n",
       "      <th>email</th>\n",
       "      <th>visit_date</th>\n",
       "      <th>fitness_test_date</th>\n",
       "      <th>application_date</th>\n",
       "      <th>purchase_date</th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>is_application</th>\n",
       "      <th>is_member</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>570</th>\n",
       "      <td>4944</td>\n",
       "      <td>Frances</td>\n",
       "      <td>Kerr</td>\n",
       "      <td>female</td>\n",
       "      <td>FK7982@gmail.com</td>\n",
       "      <td>9-8-17</td>\n",
       "      <td>2017-09-12</td>\n",
       "      <td>2017-09-10</td>\n",
       "      <td>2017-09-15</td>\n",
       "      <td>A</td>\n",
       "      <td>Application</td>\n",
       "      <td>Member</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>571</th>\n",
       "      <td>4964</td>\n",
       "      <td>Raymond</td>\n",
       "      <td>Cantrell</td>\n",
       "      <td>male</td>\n",
       "      <td>Raymond.Cantrell@gmail.com</td>\n",
       "      <td>9-9-17</td>\n",
       "      <td>None</td>\n",
       "      <td>2017-09-13</td>\n",
       "      <td>2017-09-18</td>\n",
       "      <td>B</td>\n",
       "      <td>Application</td>\n",
       "      <td>Member</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>572</th>\n",
       "      <td>4972</td>\n",
       "      <td>Roberta</td>\n",
       "      <td>Acevedo</td>\n",
       "      <td>female</td>\n",
       "      <td>RA8063@gmail.com</td>\n",
       "      <td>9-9-17</td>\n",
       "      <td>None</td>\n",
       "      <td>2017-09-15</td>\n",
       "      <td>2017-09-16</td>\n",
       "      <td>B</td>\n",
       "      <td>Application</td>\n",
       "      <td>Member</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>573</th>\n",
       "      <td>4991</td>\n",
       "      <td>Suzanne</td>\n",
       "      <td>Humphrey</td>\n",
       "      <td>female</td>\n",
       "      <td>SuzanneHumphrey4@gmail.com</td>\n",
       "      <td>9-9-17</td>\n",
       "      <td>2017-09-09</td>\n",
       "      <td>2017-09-13</td>\n",
       "      <td>2017-09-18</td>\n",
       "      <td>A</td>\n",
       "      <td>Application</td>\n",
       "      <td>Member</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>574</th>\n",
       "      <td>5002</td>\n",
       "      <td>Ruben</td>\n",
       "      <td>Nielsen</td>\n",
       "      <td>male</td>\n",
       "      <td>RubenNielsen93@hotmail.com</td>\n",
       "      <td>9-9-17</td>\n",
       "      <td>None</td>\n",
       "      <td>2017-09-13</td>\n",
       "      <td>None</td>\n",
       "      <td>B</td>\n",
       "      <td>Application</td>\n",
       "      <td>Not Member</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     index first_name last_name  gender                       email  \\\n",
       "570   4944    Frances      Kerr  female            FK7982@gmail.com   \n",
       "571   4964    Raymond  Cantrell    male  Raymond.Cantrell@gmail.com   \n",
       "572   4972    Roberta   Acevedo  female            RA8063@gmail.com   \n",
       "573   4991    Suzanne  Humphrey  female  SuzanneHumphrey4@gmail.com   \n",
       "574   5002      Ruben   Nielsen    male  RubenNielsen93@hotmail.com   \n",
       "\n",
       "    visit_date fitness_test_date application_date purchase_date ab_test_group  \\\n",
       "570     9-8-17        2017-09-12       2017-09-10    2017-09-15             A   \n",
       "571     9-9-17              None       2017-09-13    2017-09-18             B   \n",
       "572     9-9-17              None       2017-09-15    2017-09-16             B   \n",
       "573     9-9-17        2017-09-09       2017-09-13    2017-09-18             A   \n",
       "574     9-9-17              None       2017-09-13          None             B   \n",
       "\n",
       "    is_application   is_member  \n",
       "570    Application      Member  \n",
       "571    Application      Member  \n",
       "572    Application      Member  \n",
       "573    Application      Member  \n",
       "574    Application  Not Member  "
      ]
     },
     "execution_count": 209,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "just_apps = df[df.is_application =='Application'].reset_index()\n",
    "just_apps.tail()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Great! Now, let's do a `groupby` to find out how many people in `just_apps` are and aren't members from each group.  Follow the same process that we did in Step 4, including pivoting the data.  You should end up with a DataFrame that looks like this:\n",
    "\n",
    "|is_member|ab_test_group|Member|Not Member|Total|Percent Purchase|\n",
    "|-|-|-|-|-|-|\n",
    "|0|A|?|?|?|?|\n",
    "|1|B|?|?|?|?|\n",
    "\n",
    "Save your final DataFrame as `member_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
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
       "      <th>is_member</th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>Member</th>\n",
       "      <th>Not Member</th>\n",
       "      <th>Total</th>\n",
       "      <th>Percent_Purchased</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>200</td>\n",
       "      <td>50</td>\n",
       "      <td>250</td>\n",
       "      <td>80.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>250</td>\n",
       "      <td>75</td>\n",
       "      <td>325</td>\n",
       "      <td>76.923077</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "is_member ab_test_group  Member  Not Member  Total  Percent_Purchased\n",
       "0                     A     200          50    250          80.000000\n",
       "1                     B     250          75    325          76.923077"
      ]
     },
     "execution_count": 210,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "member_counts = just_apps.groupby(['ab_test_group','is_member']).count().reset_index()\n",
    "member_pivot = member_counts.pivot(columns = 'is_member', index = 'ab_test_group', values= 'first_name').reset_index()\n",
    "member_pivot['Total']=member_pivot['Member'] + member_pivot['Not Member']\n",
    "member_pivot['Percent_Purchased'] = member_pivot['Member'] *100 / member_pivot['Total']\n",
    "member_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like people who took the fitness test were more likely to purchase a membership **if** they picked up an application.  Why might that be?\n",
    "\n",
    "Just like before, we need to know if this difference is statistically significant.  Choose a hypothesis tests, import it from `scipy` and perform it.  Be sure to note the p-value.\n",
    "Is this result significant?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 211,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.43258646051083327"
      ]
     },
     "execution_count": 211,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x=[[200, 50],[250, 75]]\n",
    "a,pval,b,c = chi2_contingency(x)\n",
    "pval"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Previously, we looked at what percent of people **who picked up applications** purchased memberships.  What we really care about is what percentage of **all visitors** purchased memberships.  Return to `df` and do a `groupby` to find out how many people in `df` are and aren't members from each group.  Follow the same process that we did in Step 4, including pivoting the data.  You should end up with a DataFrame that looks like this:\n",
    "\n",
    "|is_member|ab_test_group|Member|Not Member|Total|Percent Purchase|\n",
    "|-|-|-|-|-|-|\n",
    "|0|A|?|?|?|?|\n",
    "|1|B|?|?|?|?|\n",
    "\n",
    "Save your final DataFrame as `final_member_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
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
       "      <th>is_member</th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>Member</th>\n",
       "      <th>Not Member</th>\n",
       "      <th>Total</th>\n",
       "      <th>Percent_Purchased</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>200</td>\n",
       "      <td>2304</td>\n",
       "      <td>2504</td>\n",
       "      <td>7.98722</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>250</td>\n",
       "      <td>2250</td>\n",
       "      <td>2500</td>\n",
       "      <td>10.00000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "is_member ab_test_group  Member  Not Member  Total  Percent_Purchased\n",
       "0                     A     200        2304   2504            7.98722\n",
       "1                     B     250        2250   2500           10.00000"
      ]
     },
     "execution_count": 212,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_member_counts = df.groupby(['ab_test_group','is_member']).count().reset_index()\n",
    "final_member_pivot = final_member_counts.pivot(columns = 'is_member', index = 'ab_test_group', values= 'first_name').reset_index()\n",
    "final_member_pivot['Total']=final_member_pivot['Member'] + final_member_pivot['Not Member']\n",
    "final_member_pivot['Percent_Purchased'] = final_member_pivot['Member'] *100 / final_member_pivot['Total']\n",
    "final_member_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Previously, when we only considered people who had **already picked up an application**, we saw that there was no significant difference in membership between Group A and Group B.\n",
    "\n",
    "Now, when we consider all people who **visit MuscleHub**, we see that there might be a significant different in memberships between Group A and Group B.  Perform a significance test and check."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.014724114645783203"
      ]
     },
     "execution_count": 213,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x=[[200, 2304],[250, 2250]]\n",
    "a,pval,b,c = chi2_contingency(x)\n",
    "pval"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5: Summarize the acquisition funel with a chart"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We'd like to make a bar chart for Janet that shows the difference between Group A (people who were given the fitness test) and Group B (people who were not given the fitness test) at each state of the process:\n",
    "- Percent of visitors who apply\n",
    "- Percent of applicants who purchase a membership\n",
    "- Percent of visitors who purchase a membership\n",
    "\n",
    "Create one plot for **each** of the three sets of percentages that you calculated in `app_pivot`, `member_pivot` and `final_member_pivot`.  Each plot should:\n",
    "- Label the two bars as `Fitness Test` and `No Fitness Test`\n",
    "- Make sure that the y-axis ticks are expressed as percents (i.e., `5%`)\n",
    "- Have a title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "metadata": {},
   "outputs": [
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
    "fig = plt.figure(figsize=(6, 4))\n",
    "ax = plt.subplot()\n",
    "plt.bar(range(len(app_pivot)),\n",
    "        app_pivot.Percent_with_Application)\n",
    "ax.set_xticks(range(len(app_pivot)))\n",
    "ax.set_xticklabels(['Fitness Test','No Fitness Test'])\n",
    "plt.ylabel('Percentage of Applicatons')\n",
    "plt.title('Membership Applcations by Gym Visitors')\n",
    "plt.show()\n",
    "fig.savefig('ab_test_bar_chart_fittest_to_applic.png')\n",
    "plt.close('all')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "metadata": {},
   "outputs": [
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
    "fig=plt.figure(figsize=(6, 4))\n",
    "ax = plt.subplot()\n",
    "plt.bar(range(len(member_pivot)),\n",
    "        member_pivot.Percent_Purchased)\n",
    "ax.set_xticks(range(len(member_pivot)))\n",
    "ax.set_xticklabels(['Fitness Test(A)','No Fitness Test(B)'])\n",
    "plt.ylabel('Percentge Memberships Purchased')\n",
    "plt.title('Memberships Purchased by Applicants')\n",
    "plt.show()\n",
    "fig.savefig('ab_test_bar_chart_applc_to_member.png')\n",
    "plt.close('all')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "metadata": {},
   "outputs": [
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
    "fig = plt.figure(figsize=(6, 4))\n",
    "ax = plt.subplot()\n",
    "plt.bar(range(len(final_member_pivot)),\n",
    "        final_member_pivot.Percent_Purchased)\n",
    "ax.set_xticks(range(len(final_member_pivot)))\n",
    "ax.set_xticklabels(['Fitness Test','No Fitness Test'])\n",
    "plt.ylabel('Percentage Memberships Purchased')\n",
    "plt.title('Membership Purchase by Visitors to the Gym')\n",
    "plt.show()\n",
    "fig.savefig('ab_test_bar_chart_visitor_to_member.png')\n",
    "plt.close('all')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
