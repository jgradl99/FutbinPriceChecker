# FutbinPriceChecker
A simple python program to get the current price of one or whole list more players. 

# Install
- you need to have TOR installed -> otherwise you are limited in the amount of request you can do in a short amount
- open the project inside your python IDE, install all modules
- Futbin ids and EA ids are the same -> include the corresponding ids of the player you want to get the price of inside the 'id' list
- update your console (default is 'ps' = playstation) and, if needed the year of the Futbin URL and you are ready to go

# Output example
its all JSON 
  {
    "224348": {
        "prices": {
            "pc": {
                "LCPrice": "700",
                "LCPrice2": "700",
                "LCPrice3": "700",
                "LCPrice4": "700",
                "LCPrice5": "700",
                "MaxPrice": "10,000",
                "MinPrice": "300",
                "PRP": "4",
                "updated": "6 hours ago"
            },
            "ps": {
                "LCPrice": "700",
                "LCPrice2": "800",
                "LCPrice3": "800",
                "LCPrice4": "800",
                "LCPrice5": "800",
                "MaxPrice": "10,000",
                "MinPrice": "300",
                "PRP": "4",
                "updated": "11 mins ago"
            },
            "xbox": {
                "LCPrice": "850",
                "LCPrice2": "850",
                "LCPrice3": "850",
                "LCPrice4": "850",
                "LCPrice5": "950",
                "MaxPrice": "10,000",
                "MinPrice": "300",
                "PRP": "5",
                "updated": "3 hours ago"
            }
        }
    }
}
