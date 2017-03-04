'''
generates an HTML file given an id for the url
'''
import requests
from urllib.error import HTTPError
import json
from six.moves import reduce



def main():
    glob_html = "<! doctype html>"+"<meta charset='utf-8' />"+"<html>"
    glob_html+= "<head>"+'<link rel="stylesheet" href="./style.css"/>'+"</head>"+"<body>"+'<div id="tables" />'

    
    ids = ['mc-o0168316']; #add the ids here

    url_gen = lambda id:"https://littleapp.in/menu/outlet/"+id
    urls = [url_gen(id) for id in ids]
    inp_elems = []
     # make get requests
    for i in range(len(urls)):
        try:
            r = requests.get(urls[i]).text;
        except HTTPError as e:
            print('Cant fetch: '+str(e))
        else:
            inp_elems.append(form_html_inp(r))

    # create an html file named display.html
    inp_div = reduce_to_div(inp_elems)
    glob_html += inp_div+'<script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha256-/SIrNqv8h6QGKDuNoLGA4iret+kyesCkHGzVUUV0shc=" crossorigin="anonymous"></script>'
    glob_html += '<script type="text/javascript" src="./json2table.js"></script>'
    glob_html += "</body></html>"
    with open('./result.html','wb') as f:
        f.write(bytes(glob_html,'UTF-8'))
    print("Open result.html to view the table.. and buy me a beer ;)")


def form_html_inp(val):
    return "<input type='hidden' class='ltable' value='"+val+"'></input>"

def reduce_to_div(inp_elems):
    combine_inps = lambda i1,i2: i1+i2
    concat_inp = reduce(combine_inps,inp_elems)
    return '<div>'+concat_inp+'</div>'



if __name__ == '__main__':
    main()
