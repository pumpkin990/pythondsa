import re
import keyword


def identifiers(fname):
    try:
        afile = open(fname, "r")
        s = afile.readlines()
        my_list = []
        for line in s:

            var = deal_with_var(line)
            if var and len(var) == 1 and var != keyword.kwlist:
                my_list.extend([var[0].strip()])

            quotation = deal_with_quotation(line)
            if quotation and len(quotation) == 1 and quotation != keyword.kwlist:
                my_list.extend([quotation[0].strip()])
        return list(set(my_list))
    except:
        print("***Trouble loading %s***" % fname)


def deal_with_var(s):
    vars = []
    r = re.compile(r'''\b\w+(?=\s=)''', re.X)
    vars.extend(r.findall(s))

    r = re.compile(r'''(?<=for\s)\w+\s(?=in)''', re.X)
    vars.extend(r.findall(s))

    #r = re.compile(r"""["'](.+?)["']""", re.X)
    # vars.extend(r.findall(s))

    return vars


def deal_with_quotation(s):
    quotations = []
    results = []
    r = re.compile(r"""["'](.+?)["']""", re.X)
    quotations.extend(r.findall(s))
    identifier = re.compile(r"^[^\d\W]\w*\Z", re.UNICODE)
    for test in quotations:
        regex = re.match(identifier, test)
        #print("%s\t= %s" % (test, (regex is not None)), type(regex))

        if regex is not None:
            results.extend([test])
    return results


string = "'[\\bEUR\\d.\\d\\b]' 'EUR[^E]+' 'Nan' 'Wu'"

print(identifiers("test.py"))  # return the list
# print(deal_with_quotation(string))
