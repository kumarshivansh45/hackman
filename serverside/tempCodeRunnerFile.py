def make_query(query_text):
    with engine.connect() as connection:
        the_query = connection.execute(text(query_text))
        return the_query
    
a = (make_query("select * from captcha_data;"))
for x in a :
    print(x)