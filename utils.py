def parsedata(data, separator='/', isdb=0):
    dataarray = data.split("-" if isdb else "/")
    dataarray.reverse()
    return "{}".format(separator).join(dataarray)