'''
Module 1: This module provides a reusable byline for the author's services
'''

# Import Dependencies
import math
import statistics

def main():
    

    # Define Variables
    company_name:str = "KB Complete Pet Store"
    company_description:str = "Fictional Pet Store which loves pets of all kinds!"
    company_city:str = 'Tonganoxie'
    company_state:str = 'Kansas'
    google_rating: float = 4.97
    sale_items:list = ['Nylon Bone', 'Rag Bone', 'Hamster Wheel', 'Squeaky Toy']
    cost_per_item: list = [4.95, 3.95, 6.95, 4.95]
    has_rewards_program:bool = True
    customers:list = ['Kathy', 'Kylie', 'Cory', 'Ahmed', 'Cecilia', 'Greg', 'Cierra', 'Joe']
    customer_ages:list = [24, 21, 45, 33, 19, 21, 23, 67]

# Multiline string with byline using f-string formatting
    byline: str = f"""
       About KB Complete Pet's Tonganoxie Location!
    Name: {company_name}
    Description: {company_description}
    City: {company_city}
    State: {company_state}
    Rating: {google_rating}
    Offers KB K9 Rewards: {has_rewards_program}
    
      About our Summer Sale!!!
    Number of Items on Sale: {len(sale_items)}
    Current Items on Sale: {sale_items}
    Lowest Prices Available: {min(cost_per_item)}
    The most you'll pay for sale items: {max(cost_per_item)}
    What our customers pay on average: {statistics.mean(cost_per_item)}
    
	  Some of Our Most Recent Customers
    Customer Names: {customers}
    Youngest Customer: {min(customer_ages)}
    Oldest Customer: {max(customer_ages)}
    Average Age of our Customers: {round(statistics.mean(customer_ages))}
    """


    print(byline)
   

# Call the main function to execute the code
if __name__ == '__main__':
    main()
