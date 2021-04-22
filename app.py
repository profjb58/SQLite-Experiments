import database

database.create_table()

# Insert records
#many_customers = [("john", "teehee", "john@yahoo.com"),
#                  ("I am god", "burn everything", "god@hotmail.com"),
#                  ("Henry", "The Hoover", "henry@gmail.com")
#                  ]


#database.add_many(many_customers)
database.delete('2')

database.show_all()
