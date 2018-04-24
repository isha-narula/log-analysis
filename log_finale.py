# importing psycopg2 from python standard library
import psycopg2
DBNAME = "news"

# returns result


def get_query_result(c):

    # Connect to a Database
    db = psycopg2.connect(database=DBNAME)
    # Cursor opened to perform Database Operations
    a = db.cursor()
    a.execute(c)
    answer = a.fetchall()
    # Database closed
    db.close()
    return answer

query_1_ans = dict()
query_1_result['title'] = """1.The most popular articles
                            according to views are:\n"""

query_2_ans = dict()
query_2_result['title'] = """\n2.The most popular authors
                        according to views are:\n"""

query_3_ans = dict()
query_3_result['title'] = """\n3.Percentage Error is: \n"""

# First query


def popular_article():

    c = """select articles.title, count(*)
    as num from articles inner join log
    on log.path like concat('%',articles.slug,'%')
    group by articles.title order by num desc limit 3;"""

    final = get_query_result(c)
    i = 1
    print(query_1_ans['title'])
    for x in final:
        num1 = str(i) + '. "'
        head = x[0]
        view = '" -- ' + str(x[1]) + " views"
        print(num1 + head + view)
        i = i + 1


# Second Query
def popular_author():
    c = """select authors.name,count(*) as num
          from authors join articles
          on authors.id = articles.author join log
          on log.path like concat('%',articles.slug,'%')
          group by authors.name order by num desc limit 3; """

    final = get_query_result(c)
    i = 1
    print(query_2_ans['title'])
    for y in final:
        print(str(i) + '.' + y[0] + ' -- ' + str(y[1]) + " views")
        i += 1


# Third Query
def per_error():
    c = """select two.day,((errors.er*100)/two.errs)as per
    from ( select date_trunc('day', time) "day", count(*)
        as er from log where status = '404 NOT FOUND' group by day) as errors
    join( select date_trunc('day',time) "day", count(*) as errs
        from log
          group by day) as two on two.day =  errors.day
          where (((errors.er*100)/two.errs)>1)
          order by per desc;"""
    final = get_query_result(c)
    print(query_3_ans['title'])
    for z in final:
        date = z[0].strftime('%B %d, %Y')
        error = str(z[1]) + "%" + " errors"
        print(date + " -- " + error)

# Defined functions are called
popular_article()
popular_author()
per_error()
