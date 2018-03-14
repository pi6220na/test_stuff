dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]

country_specialities_zip = zip(dishes,countries)
print(list(country_specialities_zip))
print(list(country_specialities_zip))



country_specialities_list = list(country_specialities_zip)
print(country_specialities_list)

country_specialities_dict = dict(country_specialities_list)  #was _list
print(country_specialities_dict)

myList = list(zip(dishes,countries))

print(myList)
for item in myList:
    for x in item:
        print(x)
    print(item)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def ifib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


myfib = fib(5)
print(myfib)


# Flask test of cache
# relies on modified this.py python module

# import time
# import random
#
# # from this import s, d
# # from string import translate, maketrans
# import this
#
# from flask.ext.cache import Cache
# from flask import Flask
#
# app = Flask(__name__)
# app.config['CACHE_TYPE'] = 'simple'
# app.cache = Cache(app)
#
#
# @app.cache.cached(timeout=10, key_prefix="current_time")
# def get_current_time():
#     return time.ctime()
#
#
# def random_zen_quote():
#     """Pick a random quote from the Zen of Python"""
#     # transtable = str.maketrans("".join(d.keys()), "".join(d.values()))
#     # #return random.choice(translate(s, transtable).split("\n")[2:])
#     #
#     # print(random.choice(s.translate(transtable)).split("\n")[2:])
#     # return random.choice(s.translate(transtable)).split("\n")[2:]
#
#     return this.random()
#
#
# @app.route("/")
# def zen():
#     return ("""
#     <ul>
#         <li><strong>It is cached:</strong> {cached}</li>
#         <li><strong>It is not cached:</strong> {not_cached}</li>
#     </ul>
#     """).format(
#         cached=get_current_time(),
#         not_cached=random_zen_quote()
#     )
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
#
